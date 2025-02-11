#!/bin/env python

import logging
import json
from pathlib import Path
from random import shuffle

from telegram import Update

from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import filters
from telegram.ext import ContextTypes
from telegram.ext import ConversationHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

MODE = {'ASK': 0, 'ANSWER': 1}

with Path('ids.json').open() as stream:
    UIDS = json.load(stream)

QUIZ = Path('quiz.json')
DATA = Path('data.json')

with QUIZ.open('r', encoding='utf-8') as stream:
    QUESTIONS = json.load(stream)
    shuffle(QUESTIONS)

def data_load():
    if DATA.exists():
        with DATA.open('r', encoding='utf-8') as stream:
            return json.load(stream)
    return {}


def data_save(data):
    with DATA.open('w') as stream:
        json.dump(data, stream)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['current_question'] = 0
    context.user_data['score'] = 0
    context.user_data['attempts'] = []
    uid = str(update.effective_user.id)
    if uid in UIDS and not UIDS[uid]['flag']:
        await update.message.reply_text(f"Hi {update.effective_user.first_name}! Welcome to todays quiz! Type /next to get your first question.")
        return MODE['ASK']
    await update.message.reply_text("ID is not valid or the test has already been completed!")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Quiz cancelled. Bye!")
    return ConversationHandler.END


async def save(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    uid = str(update.effective_user.id)
    if UIDS[uid]['flag'] is not None:
        UIDS[uid]['flag'] = 1
        with Path('ids.json').open('w') as stream:
            json.dump(UIDS, stream)
    user = update.effective_user
    results = data_load()
    results[str(user.id)] = {
        "username": user.username,
        "score": context.user_data.get('score', 0),
        "attempts": context.user_data.get('attempts', []),
        "total": len(QUESTIONS)
    }
    print(results)
    data_save(results)
    await update.message.reply_text("Your results have been saved.")


async def next(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    index = context.user_data.get('current_question', 0)
    if index >= len(QUESTIONS):
        await update.message.reply_text("Done!")
        await save(update, context)
        return ConversationHandler.END
    question = QUESTIONS[index]
    await update.message.reply_text(question["question"])
    for i, option in enumerate(question["options"]):
        await update.message.reply_text(f'{i + 1}: {option}')
    return MODE['ANSWER']


async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_answer, *_ = update.message.text.strip()
    try:
        user_answer = int(user_answer)
    except ValueError:
        await update.message.reply_text("Please send a number corresponding to your answer.")
        return MODE['ANSWER']
    index = context.user_data.get('current_question', 0)
    question_data = QUESTIONS[index]
    correct_answer = question_data["correct"]
    if user_answer == correct_answer:
        context.user_data['score'] += 1
    context.user_data['attempts'].append({
        "question": question_data["question"],
        "selected": user_answer,
        "correct": correct_answer
    })
    context.user_data['current_question'] += 1
    if context.user_data['current_question'] < len(QUESTIONS):
        await update.message.reply_text("Type /next for the next question.")
    else:
        await update.message.reply_text("Quiz complete! Thank you.")
        await save(update, context)
        return ConversationHandler.END
    return MODE['ASK']


def main() -> None:
    token = "TOKEN"
    application = Application.builder().token(token).build()
    handler = ConversationHandler(
            entry_points=[CommandHandler('start', start)],
            fallbacks=[CommandHandler('cancel', cancel)],
            states={
                MODE['ASK']: [CommandHandler('next', next)],
                MODE['ANSWER']: [MessageHandler(filters.TEXT & ~filters.COMMAND, answer)]
            }
        )
    application.add_handler(handler)
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()

