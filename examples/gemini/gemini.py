import argparse
parser = argparse.ArgumentParser(prog='gemini', description='Talk with gemini-pro')
parser.add_argument("message", type=str, help="input user message")
parser.add_argument('-r', '--reset-history', action='store_true', help='flag to reset conversation history')
parser.add_argument('-n', '--no-append', action='store_true', help='flag not to append current message to history')
args = parser.parse_args()

import pathlib
import json
import google.generativeai as genai

path = pathlib.Path('history.json')

if args.reset_history and path.exists():
    path.unlink()

if not path.exists():
    path.touch()
    path.write_text('[]')

text = []
if not args.reset_history:
    with path.open('r') as stream:
        text = json.load(stream)

text.append({'role':'user', 'parts': [args.message]})

safety_settings = [
    {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
]

model = genai.GenerativeModel('gemini-pro', safety_settings=safety_settings)
response = model.generate_content(text)
print(response.text)

if not args.no_append:
    text.append({'role':'model', 'parts': [response.text]})
    with path.open('w') as stream:
        json.dump(text, stream)
