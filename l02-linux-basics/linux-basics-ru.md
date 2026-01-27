<!--I.M. 2026  -->

<!-- РАЗДЕЛ  -->

# Содержание

* [00-Введение](#введение)
* [01-Описание файловой системы Linux и навигация](#описание-файловой-системы-linux-и-навигация)

  * [Всё — это файл](#всё--это-файл)
  * [Стандарт иерархии файловой системы (FHS)](#стандарт-иерархии-файловой-системы-fhs)
  * [Путь (абсолютный и относительный)](#путь-абсолютный-и-относительный)
  * [Соответствующие команды и примеры](#соответствующие-команды-и-примеры)
* [02-Просмотр и изменение файлов](#просмотр-и-изменение-файлов)

  * [Типы файлов](#типы-файлов)
  * [Права доступа](#права-доступа)
  * [Соответствующие команды и примеры](#соответствующие-команды-и-примеры-1)
* [03-Получение справки](#получение-справки)

  * [Является ли команда встроенной](#является-ли-команда-встроенной)
  * [Соответствующие команды и примеры](#соответствующие-команды-и-примеры-2)
* [04-Управление пакетами](#управление-пакетами)

  * [Пакет](#пакет)
  * [Соответствующие команды и примеры](#соответствующие-команды-и-примеры-3)
* [05-Управление пользователями](#управление-пользователями)

  * [Типовые задачи](#типовые-задачи)
  * [Контроль ресурсов](#контроль-ресурсов)
  * [Соответствующие команды и примеры](#соответствующие-команды-и-примеры-4)
* [06-Управление процессами и заданиями](#управление-процессами-и-заданиями)

  * [Процессы](#процессы)
  * [Задания](#задания)
  * [Соответствующие команды и примеры](#соответствующие-команды-и-примеры-5)
* [07-Мониторинг системы](#мониторинг-системы)

  * [Ресурсы](#ресурсы)
  * [Службы](#службы)
  * [Соответствующие команды и примеры](#соответствующие-команды-и-примеры-6)
* [08-Сетевые возможности](#сетевые-возможности)

  * [Компоненты сети](#компоненты-сети)
  * [Сетевые задачи](#сетевые-задачи)
  * [Соответствующие команды и примеры](#соответствующие-команды-и-примеры-7)

<!-- РАЗДЕЛ  -->

# Введение

[Наверх](#содержание)

Linux — критически важная часть научных исследований: он обеспечивает стабильность, гибкость и доступ к огромной экосистеме инструментов с открытым исходным кодом.
Его интерфейс командной строки и возможности скриптинга идеально подходят для работы с большими наборами данных, автоматизации рабочих процессов и запуска сложных симуляций.
Многие вычислительные кластеры высокой производительности (HPC), облачные исследовательские среды и научное программное обеспечение доступны только под Linux.
Владение Linux помогает исследователям эффективно управлять ресурсами, устранять неполадки и использовать передовые технологии.

Этот мини-курс дает вам базовые навыки Linux, ориентированные на научную работу:

* Файловая система и навигация: организация и навигация по наборам данных с использованием иерархической структуры Linux.
* Работа с файлами: обработка текстовых/данных с помощью команд `grep`, `awk` и `sed`.
* Управление пакетами: установка научного ПО через `apt`, `conda` или `pip`.
* Управление пользователями: защита общих лабораторных сред с помощью прав доступа и квот.
* Управление процессами: контроль длительных вычислений и параллельных задач.
* Мониторинг системы: оптимизация использования ресурсов (CPU, память, диск) для интенсивных задач.
* Сеть: безопасная передача данных (`scp` и `ssh`) и диагностика проблем соединения.

<!-- РАЗДЕЛ  -->

# Описание файловой системы Linux и навигация

[Наверх](#содержание)

## Всё — это файл

[Наверх](#содержание)

Идея «всё — это файл» — фундаментальный принцип проектирования Linux (и Unix-подобных систем).
В рамках этого принципа файлами считаются:

* Файлы
* Каталоги
* Ссылки
* Устройства
* Процессы
* Сокеты
* ...

## Стандарт иерархии файловой системы

[Наверх](#содержание)

Файловая система Linux устроена как иерархическое дерево каталогов, где корень обозначается `/`.
Эта иерархия определяется стандартом Filesystem Hierarchy Standard (FHS), который задаёт стандартные места для файлов и каталогов.
Следующая команда позволяет посмотреть содержимое каталога `/`.
Замечание: `->` означает, что каталог (или файл) на самом деле является ссылкой; куда она указывает, можно узнать командой `readlink`.

```bash
$ cd /
$ tree -L 1
.
├── bin -> usr/bin
├── bin.usr-is-merged
├── boot
├── cdrom
├── dev
├── etc
├── home
├── lib -> usr/lib
├── lib.usr-is-merged
├── lib64 -> usr/lib64
├── lost+found
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin -> usr/sbin
├── sbin.usr-is-merged
├── snap
├── srv
├── swap.img
├── sys
├── tmp
├── usr
└── var

26 directories, 1 file
```

Возможно, вам сначала нужно установить `tree`:

```bash
$ sudo apt install tree
```

| Каталог  | Описание                                                                                                                                        |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `/`      | Корневой каталог: всё находится внутри корня.                                                                                                   |
| `/bin`   | Пользовательские бинарники: содержит исполняемые файлы пользовательских команд.                                                                 |
| `/boot`  | Файлы загрузчика: содержит файлы загрузчика, такие как ядра, initrd (initial ram disk), а иногда и конфигурацию загрузчика.                     |
| `/dev`   | Файлы устройств: содержит файлы устройств, представляющие аппаратные компоненты, а также некоторые программные устройства.                      |
| `/etc`   | Конфигурационные файлы: конфигурации, нужные программам, а также скрипты запуска/остановки, используемые для управления отдельными программами. |
| `/home`  | Домашние каталоги: личные каталоги всех пользователей (у каждого пользователя есть свой каталог внутри `/home`).                                |
| `/lib`   | Системные библиотеки: основные разделяемые библиотеки, необходимые для загрузки системы и работы команд в корневой файловой системе.            |
| `/media` | Съёмные носители: подкаталоги, которые автоматически создаются/удаляются при монтировании/размонтировании съёмных устройств.                    |
| `/mnt`   | Каталог монтирования: используется для временно смонтированных файловых систем (например, сетевых или других временных).                        |
| `/opt`   | Дополнительные приложения: содержит приложения от сторонних поставщиков.                                                                        |
| `/proc`  | Информация о процессах: виртуальная файловая система, которая предоставляет информацию о процессах и ядре в виде файлов.                        |
| `/root`  | Домашний каталог root: домашний каталог пользователя root.                                                                                      |
| `/run`   | Переменные данные времени выполнения: содержит данные о работающей системе с момента последней загрузки (например, PID системы).                |
| `/sbin`  | Системные бинарники: важные исполняемые файлы, обычно предназначенные для root и администрирования системы.                                     |
| `/srv`   | Данные сервисов: содержит данные сервисов, предоставляемых системой.                                                                            |
| `/sys`   | Системные файлы: виртуальная файловая система с информацией о системе и подключённых устройствах (организация аппаратуры).                      |
| `/tmp`   | Временные файлы: предназначен для хранения временных файлов, которые очищаются при перезагрузке.                                                |
| `/usr`   | Пользовательские программы: большая часть утилит и приложений (бинарники, библиотеки, документация).                                            |
| `/var`   | Переменные файлы: файлы, которые ожидаемо растут (например, логи).                                                                              |

## Путь

[Наверх](#содержание)

Так как файловая система — это дерево, можно перейти к любому узлу, начиная от корня или от текущего рабочего каталога (или относительно домашнего каталога пользователя).

* **Абсолютный путь**

  ```bash
  $ cd /home/nstu
  $ pwd
  /home/nstu
  ```

* **Относительный путь**

  ```bash
  $ cd
  $ pwd
  /home/nstu
  $ cd ./Documents
  $ pwd
  /home/nstu/Documents
  $ cd ../..
  $ pwd
  /home
  $ cd ~/Documents
  /home/nstu/Documents
  ```

* **Как думаете, что произойдёт здесь?**

  ```bash
  $ cd
  $ cd ./Documents/../Downloads/
  $ pwd
  ```

## Соответствующие команды и примеры

[Наверх](#содержание)

* `pwd`: выводит текущий рабочий каталог.

* `ls`: выводит содержимое каталога.

  ```bash
  $ # Показать все файлы (включая скрытые) с подробной информацией
  $ cd /var
  $ ls -la
  total 60
  drwxr-xr-x 14 root root     4096 Feb  6 02:38 .
  drwxr-xr-x 23 root root     4096 Feb  6 01:37 ..
  -rw-r--r--  1 root root      208 Aug 27 22:37 .updated
  drwxr-xr-x  2 root root     4096 Feb  6 06:22 backups
  drwxr-xr-x 21 root root     4096 Feb  6 03:47 cache
  drwxrwsrwt  2 root whoopsie 4096 Aug 27 22:39 crash
  drwxr-xr-x 69 root root     4096 Feb  6 10:24 lib
  drwxrwsr-x  2 root staff    4096 Apr 22  2024 local
  lrwxrwxrwx  1 root root        9 Aug 27 22:37 lock -> /run/lock
  drwxrwxr-x 16 root syslog   4096 Feb  6 16:39 log
  drwxrwsr-x  2 root mail     4096 Aug 27 22:37 mail
  drwxrwsrwt  2 root whoopsie 4096 Aug 27 22:39 metrics
  drwxr-xr-x  2 root root     4096 Aug 27 22:37 opt
  lrwxrwxrwx  1 root root        4 Aug 27 22:37 run -> /run
  drwxr-xr-x 11 root root     4096 Aug 27 22:42 snap
  drwxr-xr-x  6 root root     4096 Aug 27 22:38 spool
  drwxrwxrwt 13 root root     4096 Feb  6 16:51 tmp
  ```

  ```bash
  $ # Показать файлы в каталоге
  $ ls /home/nstu
  Desktop  Documents  Downloads  Music  Pictures  Public  snap  Templates  Videos
  ```

  ```bash
  $ # Показать файлы и выбрать только скрытые
  $ cd
  $ ls -a | grep '^\.'
  .
  ..
  .bash_history
  .bash_logout
  .bashrc
  ...
  ```

* `tree`: показывает структуру каталогов в виде дерева.

  ```bash
  $ # Показать дерево (1 уровень) со сведениями о пользователе и размере
  $ tree -L 1 -uh ~
  [nstu      40K]  /home/nstu
  ├── [nstu     4.0K]  Desktop
  ├── [nstu     4.0K]  Documents
  ├── [nstu     4.0K]  Downloads
  ├── [nstu     4.0K]  Music
  ├── [nstu     4.0K]  Pictures
  ├── [nstu     4.0K]  Public
  ├── [nstu     4.0K]  snap
  ├── [nstu     4.0K]  Templates
  └── [nstu     4.0K]  Videos
  ```

* `cd`: меняет текущий каталог.

  ```bash
  $ # Переключение между двумя предыдущими каталогами
  $ cd
  $ pwd
  /home/nstu
  $ cd /
  $ pwd
  /
  $ cd -
  $ pwd
  /home/nstu
  $ cd -
  $ pwd
  /
  ```

* `mkdir`: создаёт новый каталог.

  ```bash
  $ # Создать вложенные каталоги
  $ mkdir -p backup/version-{1..5}
  $ tree ~/backup
  /home/nstu/backup
  ├── version-1
  ├── version-2
  ├── version-3
  ├── version-4
  └── version-5
  ```

  ```bash
  $ # Задать режим (права) для каталога
  $ # Можно посмотреть сам каталог
  $ # Но нельзя заглянуть внутрь каталога
  $ mkdir -m u-r test
  $ ls -ld test
  d-wxrwxr-x 2 nstu nstu 4096 Feb  1 11:02 test
  $ ls test
  ls: cannot open directory 'test': Permission denied
  ```

* `rmdir`: удаляет пустой каталог.

  ```bash
  $ # Удалить пустой каталог
  $ rmdir test
  ```

* `rm`: удаляет файлы или каталоги.

  ```bash
  $ # Удалить каталоги и их содержимое рекурсивно
  $ rm -r backup
  ```

  ```bash
  $ # Игнорировать отсутствующие файлы и не задавать вопросов
  $ rm test.txt
  rm: cannot remove 'test.txt': No such file or directory
  $ rm -f test.txt
  $ touch test.txt
  $ chmod u-w test.txt
  $ rm test.txt
  rm: remove write-protected regular empty file 'test.txt'? n
  $ ls test.txt
  test.txt
  $ rm -f test.txt
  ```

  ```bash
  $ # Удаление файлов с использованием шаблонов (wildcards), таких как `?` и `*`
  $ touch file-{01..10}.txt
  $ ls file-*.txt
  file-01.txt  file-02.txt  file-03.txt  file-04.txt  file-05.txt  file-06.txt  file-07.txt  file-08.txt  file-09.txt  file-10.txt
  $ rm file-*.txt
  ```

* `cp`: копирует файлы или каталоги.

  ```bash
  $ # Рекурсивное копирование с подробным выводом
  $ mkdir -p backup/version-{1..5}
  $ cp -vr backup copy
  'backup' -> 'copy'
  'backup/version-1' -> 'copy/version-1'
  'backup/version-2' -> 'copy/version-2'
  'backup/version-3' -> 'copy/version-3'
  'backup/version-4' -> 'copy/version-4'
  'backup/version-5' -> 'copy/version-5'
  $ tree backup/ copy/
  backup/
  ├── version-1
  ├── version-2
  ├── version-3
  ├── version-4
  └── version-5
  copy/
  ├── version-1
  ├── version-2
  ├── version-3
  ├── version-4
  └── version-5
  $ rm -r backup copy
  ```

  ```bash
  $ # Резервная копия при перезаписи (backup on copy)
  $ touch text.txt
  $ echo '1st msg' > text.txt 
  $ cp -b text.txt copy.txt
  $ ls *.txt*
  copy.txt  text.txt
  $ echo '2nd msg' > text.txt 
  $ cp -b text.txt copy.txt
  $ ls *.txt*
  copy.txt  copy.txt~  text.txt
  $ diff --side-by-side copy.txt*
  2nd msg                                                       | 1st msg
  $ rm text.txt copy.txt*
  ```

* `mv`: перемещает или переименовывает файлы/каталоги.

  ```bash
  $ # Перемещение/переименование
  $ touch text.txt
  $ mv text.txt data.txt
  $ ls *.txt
  data.txt
  $ rm data.txt 
  ```

  ```bash
  $ # Не перезаписывать существующий файл
  $ touch text.txt data.txt
  $ echo 'msg' > text.txt 
  $ cat text.txt 
  msg
  $ mv -n text.txt data.txt 
  $ cat data.txt 
  $ rm text.txt data.txt 
  ```

* `find`: поиск файлов в дереве каталогов.

  ```bash
  $ mkdir -p backup/version-{1..5}
  $ touch backup/version-{1..5}/readme.txt
  $ tree backup/
  backup/
  ├── version-1
  │   └── readme.txt
  ├── version-2
  │   └── readme.txt
  ├── version-3
  │   └── readme.txt
  ├── version-4
  │   └── readme.txt
  └── version-5
      └── readme.txt

  5 directories, 5 files
  $ find backup -name "*.txt"
  backup/version-4/readme.txt
  backup/version-1/readme.txt
  backup/version-5/readme.txt
  backup/version-2/readme.txt
  backup/version-3/readme.txt
  ```

  ```bash
  $ # Найти все каталоги
  $ find backup -type d
  backup
  backup/version-4
  backup/version-1
  backup/version-5
  backup/version-2
  backup/version-3
  ```

  ```bash
  $ # Найти и удалить все файлы *.txt
  $ find backup -name "*.txt" -exec rm {} \;
  $ tree backup/
  backup/
  ├── version-1
  ├── version-2
  ├── version-3
  ├── version-4
  └── version-5

  5 directories, 0 files
  $ rm -r backup/
  ```

  ```bash
  $ # Найти файлы определённого размера
  $ touch text-{1..5}.txt
  $ truncate -s 16M text-5.txt
  $ ls -lh text-?.txt
  -rw-rw-r-- 1 nstu nstu   0 Feb  1 11:25 text-1.txt
  -rw-rw-r-- 1 nstu nstu   0 Feb  1 11:25 text-2.txt
  -rw-rw-r-- 1 nstu nstu   0 Feb  1 11:25 text-3.txt
  -rw-rw-r-- 1 nstu nstu   0 Feb  1 11:25 text-4.txt
  -rw-rw-r-- 1 nstu nstu 16M Feb  1 11:25 text-5.txt
  $ find . -name "*.txt" -size +10M
  ./text-5.txt
  $ rm text-?.txt
  ```

<!-- РАЗДЕЛ  -->

# Просмотр и изменение файлов

[Наверх](#содержание)

Команды из предыдущего раздела, относящиеся к работе с файлами:

* `mkdir`: создать каталог
* `rmdir`: удалить каталог
* `cp`: копировать файл
* `mv`: переместить (или переименовать) файл
* `rm`: удалить файл

## Типы файлов

[Наверх](#содержание)

```bash
$ mkdir test
$ touch test.txt
$ touch test.sh && chmod u+x test.sh
$ ln -s test.sh test.link
$ ls -ldrh test*
-rw-rw-r-- 1 nstu nstu    0 Feb  1 11:30 test.txt
-rwxrw-r-- 1 nstu nstu    0 Feb  1 11:30 test.sh
lrwxrwxrwx 1 nstu nstu    7 Feb  1 10:24 test.link -> test.sh
drwxrwxr-x 2 nstu nstu 4,0K Feb  1 11:29 test
```

Файлы классифицируются не только по содержимому, но и по назначению и поведению. Существует несколько типов файлов, среди которых:

* **Обычный файл (-):** самый распространённый тип; может содержать текст, данные, инструкции программы и прочую информацию; бывает двоичным или человекочитаемым.
* **Каталог (d):** каталоги — это файлы, которые содержат список других файлов и каталогов.
* **Ссылка (l):** ссылка — это «ярлык» или указатель на другой файл или каталог.
* **Символьное устройство (c):** обеспечивает последовательный доступ к аппаратным устройствам.
* **Блочное устройство (b):** файл устройства с буферизованным доступом к аппаратным устройствам.
* **FIFO (p):** именованный канал (pipe), используется для межпроцессного взаимодействия.
* **Сокет (s):** используется для межпроцессного взаимодействия.

```bash
$ find /dev -type c
$ find /dev -type b
```

Чтобы определить тип файла, можно использовать команды `ls -l`, `file` или `stat`:

```bash
$ cd
$ ls -ldrg test*
-rw-rw-r-- 1 nstu    0 Feb  1 11:30 test.txt
-rwxrw-r-- 1 nstu    0 Feb  1 11:30 test.sh
drwxrwxr-x 2 nstu 4096 Feb  1 11:29 test
$ file test*
test:     directory
test.sh:  empty
test.txt: empty
$ stat test* 
File: test
Size: 4096            Blocks: 8          IO Block: 4096   directory
...
File: test.sh
Size: 0               Blocks: 0          IO Block: 4096   regular empty file
...
File: test.txt
Size: 0               Blocks: 0          IO Block: 4096   regular empty file
...
```

Для ссылок также можно использовать команду `readlink`, чтобы показать цель (target), на которую указывает ссылка.

## Права доступа

[Наверх](#содержание)

```bash
$ mkdir test
$ touch test.txt
$ touch test.sh && chmod u+x test.sh
$ ls -ldrh test*
-rw-rw-r-- 1 nstu nstu    0 Feb  1 11:30 test.txt
-rwxrw-r-- 1 nstu nstu    0 Feb  1 11:30 test.sh
drwxrwxr-x 2 nstu nstu 4,0K Feb  1 11:29 test
```

В Linux у каждого файла и каталога есть набор прав доступа, которые определяют, кто может **читать**, **записывать** и **выполнять** файл.

Типы прав:

* **Нет права (-):** соответствующая операция запрещена.
* **Чтение (r):** для файла — позволяет просматривать содержимое файла; для каталога — позволяет вывести список содержимого каталога.
* **Запись (w):** для файла — позволяет изменять и удалять файл; для каталога — позволяет добавлять, удалять и переименовывать файлы внутри каталога.
* **Выполнение (x):** для файла — позволяет запускать файл как программу или скрипт; для каталога — позволяет «войти» в каталог, т.е. получить доступ к его содержимому (команда смены каталога).

Категории (кто именно):

* **Пользователь (u):** владелец файла.
* **Группа (g):** пользователи, входящие в группу файла.
* **Остальные (o):** все остальные пользователи, не попадающие в категории user/group.

Замечание: командой `groups` можно посмотреть группы, участником которых вы являетесь.

Восьмеричная (octal) запись (одна цифра на владельца, группу и остальных):

* 0 — нет прав
* 1 — только выполнение
* 2 — только запись
* 3 — запись и выполнение (1+2)
* 4 — только чтение
* 5 — чтение и выполнение (4+1)
* 6 — чтение и запись (4+2)
* 7 — чтение, запись и выполнение (4+2+1)

Команду `stat` можно использовать, чтобы увидеть соответствие между буквенной и восьмеричной формой:

```bash
$ stat -c '%A %a %n' test*
drwxrwxr-x 775 test
-rwxrw-r-- 764 test.sh
-rw-rw-r-- 664 test.txt
```

Изменение прав (`chmod`):

* **Буквенный способ (используйте этот, но понимайте восьмеричную запись):**

  * `u` — user, `g` — group, `o` — others, `a` — all.
  * `+` — добавить право, `-` — убрать право, `=` — установить ровно эти права (и снять остальные).
  * `r` — read, `w` — write, `x` — execute.

  ```bash
  $ ls -l test.sh
  -rwxrw-r-- 1 nstu nstu 0 Feb  1 11:30 test.sh
  $ chmod g+x test.sh
  $ ls -l test.sh
  -rwxrwxr-- 1 nstu nstu 0 Feb  1 11:30 test.sh
  ```

* **Восьмеричный способ:**

  * 4 — чтение (r), 2 — запись (w), 1 — выполнение (x).
  * Эти значения складываются, чтобы задать несколько прав.

Смена владельца (`chown`):

* **Сменить владельца-пользователя:** `chown username filename`
* **Сменить владельца-группу:** `chown :groupname filename`
* **Сменить и пользователя, и группу:** `chown username:groupname filename`

Смена группы (`chgrp`):

* **Сменить группу файла:** `chgrp groupname filename` (список групп: `getent group | sort`)

## Соответствующие команды и примеры

[Наверх](#содержание)

* `touch`: создаёт пустой файл или обновляет временные метки существующего файла.

  ```bash
  $ # Создать пустой файл
  $ touch test.txt
  $ file test.txt
  test.txt: empty
  ```

  ```bash
  $ # Установить временную метку
  $ touch -t 197001010000 test.txt
  $ ls -l test.txt 
  -rw-rw-r-- 1 nstu nstu 0 Jan  1  1970 test.txt
  ```

  ```bash
  $ # Обновить время доступа
  $ touch -a test.txt && stat -c '%x' test.txt 
  2024-02-01 12:39:18.235509181 +0700
  $ touch -a test.txt && stat -c '%x' test.txt 
  2024-02-01 12:39:21.935509359 +0700
  ```

* `stat`: выводит подробную информацию о файле или файловой системе.

  ```bash
  $ # Подробная информация о файле
  $ stat test.txt 
  File: test.txt
  Size: 0               Blocks: 0          IO Block: 4096   regular empty file
  ...
  ```

  ```bash
  $ # Имя и размер в байтах
  $ truncate -s 16M text.txt
  $ stat -c '%n %s' text.txt 
  text.txt 16777216
  ```

  ```bash
  $ # Показать права доступа
  $ stat --format='%A' test.txt 
  -rw-rw-r--
  ```

  ```bash
  $ # Сортировка по размеру (по убыванию)
  $ touch text-{01..10}.txt
  $ files=($(ls text-*.txt))
  $ sizes=($(echo {01..10}))
  $ for i in $(seq 0 9); do truncate -s "${sizes[$i]}M" "${files[$i]}"; done
  $ ls -lh text-*.txt
  -rw-rw-r-- 1 nstu nstu 1,0M Feb  1 13:02 text-01.txt
  -rw-rw-r-- 1 nstu nstu 2,0M Feb  1 13:02 text-02.txt
  -rw-rw-r-- 1 nstu nstu 3,0M Feb  1 13:02 text-03.txt
  -rw-rw-r-- 1 nstu nstu 4,0M Feb  1 13:02 text-04.txt
  -rw-rw-r-- 1 nstu nstu 5,0M Feb  1 13:02 text-05.txt
  -rw-rw-r-- 1 nstu nstu 6,0M Feb  1 13:02 text-06.txt
  -rw-rw-r-- 1 nstu nstu 7,0M Feb  1 13:02 text-07.txt
  -rw-rw-r-- 1 nstu nstu 8,0M Feb  1 13:02 text-08.txt
  -rw-rw-r-- 1 nstu nstu 9,0M Feb  1 13:02 text-09.txt
  -rw-rw-r-- 1 nstu nstu  10M Feb  1 13:02 text-10.txt
  $ find ./*.txt -type f -exec stat -c '%n %s' {} + | sort -nrk 2
  ./text-10.txt 10485760
  ./text-09.txt 9437184
  ./text-08.txt 8388608
  ./text-07.txt 7340032
  ./text-06.txt 6291456
  ./text-05.txt 5242880
  ./text-04.txt 4194304
  ./text-03.txt 3145728
  ./text-02.txt 2097152
  ./text-01.txt 1048576
  $ rm text-*.txt
  ```

* `ln`: создаёт ссылки (жёсткие или символические) между файлами.

  ```bash
  $ # Создать жёсткую ссылку (указывает на те же данные на диске)
  $ touch test.txt
  $ for i in $(seq 10); do echo $i >> test.txt; done
  $ cat test.txt
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  $ ln test.txt link.txt
  $ file link.txt 
  link.txt: ASCII text
  $ readlink link.txt
  $ rm test.txt
  $ cat link.txt
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  rm link.txt
  ```

  ```bash
  $ # Создать символическую ссылку
  $ touch test.txt
  $ for i in $(seq 10); do echo $i >> test.txt; done
  $ ln -s test.txt link.txt
  $ file link.txt 
  link.txt: symbolic link to test.txt
  $ readlink link.txt
  test.txt
  $ rm test.txt
  $ cat link.txt
  cat: link.txt: No such file or directory
  $ [ -L link.txt ] && echo 'dangling'
  dangling
  $ rm link.txt
  ```

  ```bash
  $ # Изменить цель ссылки
  $ touch test.txt data.txt
  $ echo 'test' > test.txt 
  $ echo 'data' > data.txt 
  $ cat test.txt data.txt
  $ ln -s test.txt link.txt
  $ cat link.txt
  test
  $ ln -sf data.txt link.txt
  $ cat link.txt
  data
  $ rm {test,data,link}.txt
  ```

* `more`: просмотр содержимого файла.

  ```bash
  $ # Просмотр содержимого постранично
  $ touch test.txt
  $ for i in $(seq 10); do echo $i >> test.txt; done
  $ more test.txt
  $ rm test.txt
  ```

* `less`: просмотр содержимого файла (нажмите `h` для справки, `q` для выхода).

  ```bash
  $ # Просмотр содержимого постранично
  $ touch test.txt
  $ for i in $(seq 10); do echo $i >> test.txt; done
  $ less test.txt
  $ rm test.txt
  ```

* `cat`: объединяет и выводит содержимое файлов (см. также `tac` и `split`).

  ```bash
  $ # Показать содержимое файла
  $ touch test.txt
  $ echo 'test' > test.txt
  $ cat test.txt
  test
  ```

  ```bash
  $ # ConCATenates files (склеивает файлы)
  $ touch test.txt data.txt
  $ echo 'test' > test.txt
  $ echo 'data' > data.txt
  $ cat -n test.txt data.txt
      1  test
      2  data
  ```

* `head`: показывает начало файла.

  ```bash
  $ # Показать первые 5 строк
  $ rm -f test.txt ; touch test.txt
  $ for i in $(seq 10); do echo $i >> test.txt; done
  $ head -n 5 test.txt
  1
  2
  3
  4
  5
  ```

* `tail`: показывает конец файла.

  ```bash
  $ # Показать последние 5 строк
  $ rm -f test.txt ; touch test.txt
  $ for i in $(seq 10); do echo $i >> test.txt; done
  $ tail -n 5 test.txt 
  6
  7
  8
  9
  10
  ```

  ```bash
  $ # Отслеживать новые записи в syslog (или: sudo watch -n 1 tail -n 5 /var/log/syslog)
  $ # Нажмите Ctrl+C для выхода
  $ sudo tail -f /var/log/syslog
  ```

* `grep`: поиск по шаблону в файлах.

  ```bash
  $ # Поиск по шаблону
  $ rm -f test.txt ; touch test.txt
  $ for i in $(seq 100); do echo $i >> test.txt; done
  $ grep "0" test.txt
  10
  20
  30
  40
  50
  60
  70
  80
  90
  100
  ```

  ```bash
  $ # Поиск без учёта регистра
  $ echo 'pattern' > test.txt
  $ echo 'PATTERN' >> test.txt
  $ grep -i 'pattern' test.txt 
  pattern
  PATTERN
  ```

  ```bash
  $ # Поиск в нескольких файлах
  $ echo 'pattern' > test.txt
  $ echo 'pattern' > data.txt
  $ grep 'pattern' test.txt data.txt
  test.txt:pattern
  data.txt:pattern
  ```

  ```bash
  $ # Рекурсивный поиск
  $ mkdir -p backup/version
  $ echo 'pattern' > backup/readme.txt
  $ echo 'pattern' > backup/version/readme.txt
  $ tree backup
  backup/
  ├── readme.txt
  └── version
      └── readme.txt
  $ grep -r 'pattern' backup
  backup/version/readme.txt:pattern
  backup/readme.txt:pattern
  ```

* `diff`: сравнение файлов построчно.

  ```bash
  $ # Сравнение файлов (обычный формат и unified)
  $ cat <<EOF > test.txt
  > year: 2023
  > data: 01
  > file: test.txt
  > EOF
  $ cat <<EOF > data.txt
  > year: 2024
  > data: 01
  > list: 1
  > file: data.txt
  > EOF
  $ diff test.txt data.txt
  1c1
  < year: 2023
  ---
  > year: 2024
  3c3,4
  < file: test.txt
  ---
  > list: 1
  > file: data.txt
  $ diff -u test.txt data.txt
  --- test.txt    2024-02-01 14:29:44.151828844 +0700
  +++ data.txt    2024-02-01 14:30:01.191829666 +0700
  @@ -1,3 +1,4 @@
  -year: 2023
  +year: 2024
  data: 01
  -file: test.txt
  +list: 1
  +file: data.txt
  ```

  * Обычный (normal) формат

    ```bash
    1c1
    < year: 2023
    ---
    > year: 2024
    3c3,4
    < file: test.txt
    ---
    > list: 1
    > file: data.txt
    ```

    * `1c1`: строка 1 в первом файле изменена (`c`, change) на строку 1 во втором файле
    * `< year: 2023`: префикс `<` показывает содержимое строки 1 из первого файла
    * `---`: разделитель, который `diff` использует для отделения содержимого разных файлов
    * `> year: 2024`: префикс `>` показывает содержимое строки 1 из второго файла
    * Первый блок изменений читается как: "year: 2023" в `test.txt` заменено на "year: 2024" в `data.txt`
    * `3c3,4`: начиная со строки 3 в `test.txt` ( `3c` ) и затрагивая строки 3 и 4 в `data.txt` ( `3,4` )
    * `< file: test.txt`: содержимое строки 3 в `test.txt`
    * `> list: 1`: новое содержимое строки 3 в `data.txt`
    * `> file: data.txt`: новое содержимое строки 4 в `data.txt`
    * Второй блок изменений читается как: "file: test.txt" (строка 3) заменено на "list: 1" и "file: data.txt" (строки 3–4)

  * Unified формат

    ```bash
    --- test.txt ...
    +++ data.txt ...
    @@ -1,3 +1,4 @@
    -year: 2023
    +year: 2024
    data: 01
    -file: test.txt
    +list: 1
    +file: data.txt
    ```

    * `--- test.txt ...`: первый файл (`test.txt`)
    * `+++ data.txt ...`: второй файл (`data.txt`)
    * `@@ -1,3 +1,4 @@`: заголовок «куска» (hunk header), показывает где находятся изменения
    * `-1,3`: изменения начинаются с строки 1 и охватывают 3 строки в `test.txt`
    * `+1,4`: изменения начинаются с строки 1 и охватывают 4 строки в `data.txt`
    * Изменения перечислены после заголовка
    * Строки, начинающиеся с `-`, относятся к `test.txt`
    * Строки, начинающиеся с `+`, относятся к `data.txt`
    * Строки без `+`/`-` не менялись и приводятся как контекст
    * `-year: 2023`: строка была в `test.txt`, но удалена/изменена в `data.txt`
    * `+year: 2024`: строка добавлена/изменена в `data.txt`
    * `data: 01`: строка без изменений (контекст)
    * `-file: test.txt`: строка из `test.txt`, удалена/заменена
    * `+list: 1`: строка добавлена в `data.txt`
    * `+file: data.txt`: строка также добавлена в `data.txt`

* `sort`: сортировка строк в текстовых файлах.

  ```bash
  $ # Обычная и обратная сортировка (алфавитно-цифровая)
  $ rm -f test.txt ; touch test.txt
  $ for i in 1 5 10 15 20; do echo $i >> test.txt; done
  $ sort test.txt
  1
  10
  15
  20
  5
  $ sort -r test.txt
  5
  20
  15
  10
  1
  ```

  ```bash
  $ # Числовая сортировка
  $ sort -n test.txt
  1
  5
  10
  15
  20
  ```

  ```bash
  $ # Сортировка по второму полю (числовая)
  $ cat << EOF > test.txt
  > a:2023
  > b:2020
  > c:2021
  > d:2007
  > EOF
  $ sort -t: -n -k 2 test.txt 
  d:2007
  b:2020
  c:2021
  a:2023
  ```

* `cut`: «вырезает» части из каждой строки файла.

  ```bash
  $ # Вывести 2-е поле каждой строки (можно выбирать несколько полей)
  $ cut -d':' -f2 test.txt
  2023
  2020
  2021
  2007
  ```

  ```bash
  $ # Вывести 1-й символ
  $ cut -c1-1 test.txt 
  a
  b
  c
  d
  ```

* `uniq`: показывает или скрывает повторяющиеся строки.

  ```bash
  $ # Показать уникальные строки (схлопывает подряд идущие повторы)
  $ cat << EOF > test.txt
  > 1
  > 1
  > 1
  > 2
  > 2
  > 3
  > EOF
  $ uniq test.txt 
  1
  2
  3
  ```

  ```bash
  $ # Показать количество повторов, дубликаты и уникальные строки
  $ uniq -c test.txt 
      3 1
      2 2
      1 3
  $ uniq -d test.txt 
  1
  2
  $ uniq -u test.txt 
  3
  $ 
  ```

* `wc`: считает строки, слова и символы в файлах.

  ```bash
  $ # Посчитать количество строк в файле
  $ wc -l test.txt 
  6 test.txt
  ```

  ```bash
  $ # Посчитать количество слов в файле (для символов используйте -c)
  $ wc -w test.txt 
  6 test.txt
  ```

  ```bash
  $ # Посчитать количество каталогов
  $ find ~ -maxdepth 1 -name "*" ! -name ".*" -type d | wc -l
  10
  ```

* `tee`: читает из stdin и пишет в stdout и в файл(ы).

  ```bash
  $ # Записать промежуточный результат в файл
  $ echo $USER | tee user.log | wc -c
  4
  $ cat user.log
  nstu
  ```

  ```bash
  $ # Добавление в конец файла (append)
  $ echo 'line1' | tee file1.txt | tee -a file2.txt > /dev/null
  $ echo 'line2' | tee file1.txt | tee -a file2.txt > /dev/null
  $ cat file1.txt  file2.txt 
  line2
  line1
  line2
  ```

* `nl`: добавляет номера строк.

  ```bash
  $ # Добавить номера строк
  $ printf "a \nb \nc \nd" > test.txt
  $ nl test.txt
      1  a 
      2  b 
      3  c 
      4  d
  ```

* `ar`: утилита архивирования, используется для создания и изменения архивов.

  ```bash
  $ # Создать архив
  $ cat << EOF > foo.c
  int foo(){
  >   return 0 ;
  > }
  > EOF
  $ cat << EOF > bar.c
  int bar(){
  return 0 ;
  }
  EOF
  $ gcc -c foo.c bar.c
  $ ar -r foobar.a foo.o bar.o
  ar: creating foobar.a
  $ ar -t foobar.a 
  foo.o
  bar.o
  $ stat -c '%n %s' foo.o bar.o foobar.a 
  foo.o 1368
  bar.o 1368
  foobar.a 2944
  $ touch note.txt
  $ ar -rs foobar.a note.txt
  $ ar -t foobar.a
  foo.o
  bar.o
  note.txt
  ```

* `tar`, `zip`, `unzip`: работа с архивами.

  ```bash
  $ # Архивация с tar
  $ seq 100 > file1.txt
  $ seq 100 > file2.txt
  $ seq 100 > file3.txt
  $ tar -cf archive.tar file1.txt file2.txt
  $ tar -czf archive.tar.gz file1.txt file2.txt
  $ stat -c '%n %s' archive*
  archive.tar 10240
  archive.tar.gz 1837
  $ tar -xf archive.tar
  $ tar -xzf archive.tar.gz
  ```

  ```bash
  $ # Архивация с zip
  $ seq 100 > file1.txt
  $ seq 100 > file2.txt
  $ seq 100 > file3.txt
  $ zip archive.zip file1.txt file2.txt
  adding: file1.txt (deflated 51%)
  adding: file2.txt (deflated 53%)
  $ zip archive.zip file3.txt
  adding: file3.txt (deflated 51%)
  $ unzip -o archive.zip
  Archive:  archive.zip
  inflating: file1.txt
  inflating: file2.txt
  inflating: file3.txt
  ```

* `sed`: потоковый редактор для фильтрации и преобразования текста.

  ```bash
  $ # Замена
  $ printf "a \nb \nc \na \nb \nc" > test.txt
  $ sed 's/a/A/g' test.txt
  A 
  b 
  c 
  A 
  b 
  c
  ```

  ```bash
  $ # Вывести конкретную строку
  $ sed -n '5p' test.txt
  b
  ```

  ```bash
  $ # Удалить строки по шаблону
  $ sed '/[a,b]/d' test.txt
  c
  c
  ```

* `awk`: язык программирования, предназначенный для обработки текста.

  ```bash
  $ # Вывод поля
  $ printf "A 1\nB 2\nC 3\nD 4\nE 5" > test.txt
  $ awk '{print $1}' test.txt
  A
  B
  C
  D
  E
  $ awk '{print $2 " " $1}' test.txt
  1 A
  2 B
  3 C
  4 D
  5 E
  ```

  ```bash
  $ # Поиск по шаблону
  $ awk '/C/{print $2}' test.txt 
  3
  ```

  ```bash
  $ # Немного математики
  $ awk '{sum+=$2} END {print sum}' test.txt
  15
  $ awk '{if ($2 == 5) print $1}' test.txt
  E
  ```

* `nano`, `vim`, `vi`, `neovim`: текстовые редакторы в терминале (посмотрите kickstart `neovim` на GitHub).

  Основы `vim`:

  * `vim [file]`

  * **Normal Mode (нормальный режим)**:

    * режим по умолчанию
    * используется для навигации, копирования, вырезания, вставки и других команд редактирования
    * переход в Normal mode из других режимов — клавиша `Esc`

  * **Insert Mode (режим ввода)**:

    * для ввода текста
    * вход из Normal mode — клавиша `i`
    * выход в Normal mode — клавиша `Esc`

  * **Visual Mode (визуальный режим)**:

    * для выделения блоков текста
    * вход из Normal mode — `v` (символы), `V` (строки) или `Ctrl + v` (блочное выделение)
    * выход — `Esc`

  * **Replace Mode (режим замены)**:

    * для замены текста
    * вход из Normal mode — `R`
    * выход — `Esc`

  * **Command-Line Mode (командный режим)**:

    * для команд редактора (сохранение, выход)
    * вход из Normal mode — `:` (команды), `/` (поиск вперёд) или `?` (поиск назад)
    * выполнение команды — `Enter`, затем возврат в Normal mode
    * `:q` — выйти, `:q!` — выйти без сохранения, `:wq` — сохранить и выйти

* `curl` или `wget`: скачивание файлов из интернета (возможно, сначала нужно установить: `sudo apt install curl wget`)

  ```bash
  $ # Терминальный «браузер»
  $ curl "ipinfo.io"
  $ curl "wttr.in/Novosibirsk"
  ```

  ```bash
  $ # Скачивание файлов
  $ curl -O https://raw.githubusercontent.com/i-a-morozov/nstu-mini-tec-course/main/README.MD
  $ wget https://raw.githubusercontent.com/i-a-morozov/nstu-mini-tec-course/main/LICENSE
  ```

<!-- РАЗДЕЛ  -->

# Получение справки

[Наверх](#содержание)

В этом разделе мы научимся получать справку по командам.
Некоторые команды являются встроенными в оболочку (shell), например `cd`.
У таких команд, как правило, нет `man`-страниц, и их нельзя запускать через `sudo`.

```bash
$ sudo cd /
sudo: cd: command not found
sudo: "cd" is a shell built-in command, it cannot be run directly.
sudo: the -s option may be used to run a privileged shell.
sudo: the -D option may be used to run a command in a specific directory.
```

Для встроенных команд подробнее смотрите вывод `man builtins`.

## Является ли команда встроенной?

[Наверх](#содержание)

Оболочка, например `bash`, поставляется с набором встроенных команд (`man builtins`).

* `type`

  ```bash
  $ type cd
  cd is a shell builtin
  $ type ls
  ls is aliased to `ls --color=auto'
  ```

* `command` (без флагов — проверка наличия команды)

  ```bash
  $ command -V cd
  cd is a shell builtin
  $ command -V ls
  ls is aliased to `ls --color=auto'
  ```

* `help` (специфично для `bash`, работает для builtins)

  ```bash
  $ help cd
  cd: cd [-L|[-P [-e]] [-@]] [dir]
  ...
  $ help ls
  -bash: help: no help topics match `ls'.  Try `help help' or `man -k ls' or `info ls'.
  ```

## Соответствующие команды и примеры

[Наверх](#содержание)

* `man`: страницы руководства (manual pages).

  ```bash
  $ # Показать man-страницу для команды ls
  $ man ls
  ```

  ```bash
  $ # Документация по функциям языка C
  $ man malloc
  ```

  * **Разделы**: `man N ...`

    * (1) Общие команды
    * (2) Системные вызовы
    * (3) Функции стандартной C-библиотеки
    * (4) Специальные файлы и драйверы (/dev)
    * ...

* `whatis`: однострочное описание из man (`man -f`).

  ```bash
  $ # Обратите внимание: также печатается раздел
  $ whatis grep
  grep (1)             - print lines that match patterns
  ```

* `apropos`: поиск по именам и описаниям man-страниц (`man -k`).

  ```bash
  $ # Обратите внимание: также печатается раздел
  $ apropos udisks
  udisks (8)           - Disk Manager
  udisks2.conf (5)     - The udisks2 configuration file
  udisksctl (1)        - The udisks command line tool
  udisksd (8)          - The udisks system daemon
  umount.udisks2 (8)   - unmount file systems that have been mounted by UDisks2
  ```

* `whereis`: поиск расположения бинарника, исходников и man-страниц.

  ```bash
  $ whereis bash
  bash: /usr/bin/bash /usr/share/man/man1/bash.1.gz
  ```

* `info`: чтение документации в формате info.

  ```bash
  $ # Прочитать info про tar
  $ info tar
  ```

* `tldr`: упрощённые и поддерживаемые сообществом man-страницы (с примерами).

  ```bash
  $ # Обновить локальный кэш tldr-страниц (сделайте это сначала)
  $ tldr -u`: 
  ```

  ```bash
  $ # Показать примеры для grep
  $ tldr grep
  ```

* `command --help` или `command --help | less`

  ```bash
  $ man --help
  Usage: man [OPTION...] [SECTION] PAGE...
  ...
  ```

* Другое

  * [Unix & Linux StackExchange](https://unix.stackexchange.com/)
  * [Ask Ubuntu](https://askubuntu.com/)
  * LLM’ы

<!-- РАЗДЕЛ  -->

# Управление пакетами

[Наверх](#содержание)

## Некоторые определения

[Наверх](#содержание)

В Linux распространение и управление программным обеспечением в основном устроено через пакеты и пакетные менеджеры.
Такая система упрощает установку, обновление, настройку и удаление ПО.

* **Пакеты**:
  Пакет в Linux — это сжатый архив, содержащий все файлы, необходимые для работы конкретной программы.
  Обычно это исполняемый файл, документация, конфигурационные файлы и дополнительные зависимости, нужные для корректной работы.
  Распространённые форматы пакетов: `.deb` (Debian, Ubuntu) и `.rpm` (Red Hat).

* **Управление пакетами**:
  Управление пакетами — это процесс установки и сопровождения программного обеспечения системным образом.
  Это помогает легко устанавливать, обновлять, настраивать и удалять ПО.
  Пакеты хранятся в репозиториях — серверах, содержащих большое количество пакетов.
  Репозитории доступны через интернет и могут быть официальными (поддерживаются разработчиками дистрибутива) или сторонними.

* **Пакетные менеджеры**: пакетный менеджер — это набор инструментов, который автоматизирует установку, обновление, настройку и удаление пакетов в Linux.

## Соответствующие команды и примеры

[Наверх](#содержание)

* `apt`: Advanced package tool (пакеты уровня системы) (Debian, Ubuntu, ...).

  * `sudo apt update`: обновляет список доступных пакетов и их версий.
  * `sudo apt upgrade`: обновляет все установленные пакеты до последних версий.
  * `sudo apt install <package>`: устанавливает пакет.
  * `sudo apt remove <package>`: удаляет пакет без удаления конфигурационных файлов.
  * `sudo apt purge <package>`: удаляет пакет вместе с конфигурационными файлами.
  * `apt list`: список установленных пакетов (можно сохранить список в файл `sudo apt list > packages.txt` или передать в `less`/`grep`/...)

* `snap`: пакетный инструмент Ubuntu (Canonical) (пакеты уровня системы).

  * `sudo snap refresh`: обновляет все установленные snap-пакеты до последних версий.
  * `sudo snap install <package>`: устанавливает пакет.
  * `sudo snap remove <package>`: удаляет пакет.
  * `snap find "text"`: ищет snap-пакеты, связанные с "text".
  * `sudo snap revert <package>`: откатывает пакет на предыдущую версию.

* `flatpak`: независимый от дистрибутива инструмент: установка/сборка/запуск приложений (пакеты уровня системы) (`sudo apt install flatpak`).

  * `flatpak update`: обновляет все установленные приложения flatpak.
  * `flatpak list`: список всех установленных приложений flatpak.
  * `flatpak install flathub <application>`: устанавливает приложение из репозитория `flathub`.
  * `flatpak uninstall <application>`: удаляет приложение.
  * `flatpak run <application>`: запускает приложение.

* `dpkg`: низкоуровневый пакетный менеджер Debian (пакеты уровня системы) (`.deb` можно ставить через `apt`, и зависимости подтянутся автоматически).

  * `sudo dpkg -i <package.deb>`: устанавливает пакет из файла.
  * `sudo dpkg -r <package>`: удаляет пакет без удаления конфигурационных файлов.
  * `dpkg -l`: список всех установленных Debian-пакетов.

* `alien`: конвертер между форматами пакетов Linux (пакеты уровня системы) (`sudo apt install alien`).

  * `sudo alien package.rpm`: конвертирует `.rpm` в Debian-пакет `.deb`.
  * `sudo alien -i <package.rpm>`: конвертирует `.rpm` в `.deb` и устанавливает его.

* `aptitude`: `apt` с текстовым интерфейсом (пакеты уровня системы) (`sudo apt install aptitude`).

  * `sudo aptitude`: запуск в интерактивном режиме.
  * `sudo aptitude update`: обновляет список доступных пакетов.
  * `sudo aptitude install <package>`: устанавливает пакет.
  * `sudo aptitude remove <package>`: удаляет пакет без удаления конфигурационных файлов.
  * `sudo aptitude purge <package>`: удаляет пакет вместе с конфигурационными файлами.
  * `sudo aptitude search "text"`: ищет пакеты, связанные с "text".

* `synaptic`: `apt` с GUI (пакеты уровня системы) (`sudo apt install synaptic`).

* `conda`: пакетный менеджер Anaconda (пакеты уровня пользователя, не только для Python!).

  * `conda --help`: общая справка
  * `conda command --help`: справка по конкретной команде (`install`, `list`, ...)
  * `conda install <package>`: устанавливает пакет.
  * `conda update <package>`: обновляет пакет (например, `conda update conda`).
  * `conda create -n <name> python=<version>`: создаёт окружение conda с именем `name` и Python версии `version`.
  * `conda activate <name>`: активирует окружение `name`.
  * `conda deactivate`: деактивирует текущее окружение.
  * `conda list`: список пакетов в текущем окружении.

* `pip`: установщик Python-пакетов (пакеты уровня пользователя).

  * `pip --help`: общая справка
  * `pip command --help`: справка по команде (`install`, `list`, ...)
  * `pip install <package>`: устанавливает пакет.
  * `pip install --upgrade <package>`: устанавливает пакет или обновляет установленный.
  * `pip uninstall <package>`: удаляет пакет.
  * `pip list`: список установленных Python-пакетов.
  * `pip freeze > requirements.txt`: генерирует файл requirements.txt со всеми пакетами и их версиями.
  * `pip install -e .`: устанавливает пакет (и зависимости) из текущего каталога (`pyproject.toml`, `setup.py`, ...) в режиме редактирования (editable)
  * `pip install -r requirements`: устанавливает пакеты из requirements-файла.

* Другое: `sh`, `make` (следуйте инструкциям по установке; если их нет — сначала попробуйте без `sudo`)

  * `chmod +x <application>.sh`, `./<application>.sh`
  * `make`, `make install`
  * `ninja`, `meson` и другие системы сборки

<!-- РАЗДЕЛ  -->

# Управление пользователями

[Наверх](#содержание)

## Типовые задачи

[Наверх](#содержание)

```bash
$ # Добавить пользователя
$ sudo useradd student
```

```bash
$ # Установить (изменить) пароль пользователя
$ sudo passwd student
```

```bash
$ # Создать группу
$ sudo groupadd course
```

```bash
$ # Добавить пользователя в группу
$ sudo usermod -aG course student
$ groups student 
student : student course
```

```bash
$ # Вход/выход
$ sudo login
nstu login: student
Password: 
$ echo $USER
student
$ exit
```

```bash
$ # Удалить пользователя и соответствующий домашний каталог
$ sudo userdel -r student
```

```bash
$ # Создать пользователя с опциями
$ sudo useradd -m -d /home/student -s /bin/bash -G course student
$ sudo passwd student
```

## Контроль ресурсов

[Наверх](#содержание)

* `quota`: установка дисковых квот для пользователей (`sudo apt install quota`).

  * `sudo apt install quota`
  * `sudo nano /etc/fstab` (изменить `errors=remount-ro` на `errors=remount-ro,usrquota,grpquota`)
  * `sudo mount -o remount /`
  * `sudo quotacheck -cugm /` (инициализировать базу)
  * `sudo edquota -u student` (установить квоту, например 1048576 в soft & hard для 1G)
  * `sudo quotaon /` (включить квоты)
  * `sudo quota -u student` (проверить квоту)

  ```bash
  $ sudo login student
  $ dd if=/dev/zero of=tmp.log bs=1M count=1024
  dd: error writing 'tmp.log': Disk quota exceeded
  1024+0 records in
  1023+0 records out
  1073713152 bytes (1,1 GB, 1,0 GiB) copied, 0,459262 s, 2,3 GB/s
  ```

* `ulimit`: ресурсы, доступные оболочке и запущенным из неё процессам (для текущей сессии shell).

  * `ulimit -a`: посмотреть лимиты
  * `ulimit -u`: установить максимальное число процессов
  * `ulimit -t`: установить лимит CPU-времени в секундах
  * `ulimit -f`: установить лимит размера файлов
  * `ulimit -s`: установить лимит размера стека (для задач, активно использующих память, можно `ulimit -s unlimited`)
  * `ulimit -m`: установить лимит памяти (`-v` — для виртуальной памяти)
  * `sudo nano /etc/security/limits.conf`: установить лимиты для пользователя (обычный пользователь может уменьшать лимиты, но не увеличивать)

  ```bash
  $ # Посмотреть текущие лимиты пользователя
  $ ulimit -a
  real-time non-blocking time  (microseconds, -R) unlimited
  core file size              (blocks, -c) 0
  data seg size               (kbytes, -d) unlimited
  scheduling priority                 (-e) 0
  file size                   (blocks, -f) unlimited
  pending signals                     (-i) 7535
  max locked memory           (kbytes, -l) 250684
  max memory size             (kbytes, -m) unlimited
  open files                          (-n) 1024
  pipe size                (512 bytes, -p) 8
  POSIX message queues         (bytes, -q) 819200
  real-time priority                  (-r) 0
  stack size                  (kbytes, -s) 8192
  cpu time                   (seconds, -t) unlimited
  max user processes                  (-u) 7535
  virtual memory              (kbytes, -v) unlimited
  file locks                          (-x) unlimited
  ```

## Соответствующие команды и примеры

[Наверх](#содержание)

* `sudo`: выполняет команду от имени другого пользователя, обычно суперпользователя.

  ```bash
  $ # Запуск команды от имени суперпользователя
  $ sudo apt update
  $ sudo apt upgrade
  ```

  ```bash
  $ # Выполнить команду от имени пользователя
  $ sudo -u student touch /home/student/password
  $ ls /home/student/
  ls: cannot open directory '/home/student/': Permission denied
  $ sudo -u student ls /home/student/
  password
  ```

  ```bash
  $ # Запустить shell-сессию от имени суперпользователя
  $ sudo -s
  # id
  uid=0(root) gid=0(root) groups=0(root)
  # exit
  exit
  ```

  ```bash
  $ # Повторно выполнить предыдущую команду от имени суперпользователя
  $ cat /etc/sudoers
  cat: /etc/sudoers: Permission denied
  $ sudo !!
  sudo cat /etc/sudoers
  #
  # This file MUST be edited with the 'visudo' command as root.
  #
  ...
  ```

* `su`: переключает текущего пользователя.

  ```bash
  $ # Сменить пользователя
  $ su student
  Password: 
  $ id
  uid=1003(student) gid=1004(student) groups=1004(student),1002(course)
  $ exit
  exit
  ```

* `useradd`: создаёт нового пользователя или обновляет настройки по умолчанию для новых пользователей.

  ```bash
  $ # Добавить пользователя
  $ sudo useradd <user>
  ```

  ```bash
  $ # Добавить пользователя и создать домашний каталог
  $ sudo useradd -m <user>
  ```

  ```bash
  $ # Добавить пользователя и включить в группу
  $ sudo useradd -G <group> <user>
  ```

  ```bash
  $ # Добавить пользователя и задать shell
  $ sudo useradd -s /bin/bash <user>
  ```

  ```bash
  $ # Добавить пользователя и задать дату окончания учётной записи
  $ sudo useradd -e 2025-01-01 <user>
  ```

* `userdel`: удаляет учётную запись и связанные файлы.

  ```bash
  $ # Удалить пользователя
  $ sudo userdel <user>
  ```

  ```bash
  $ # Удалить пользователя вместе с домашним каталогом и mail spool
  $ sudo userdel -r <user>
  ```

  ```bash
  $ # Удалить пользователя вместе с домашним каталогом и mail spool, но сохранить резервные копии файлов
  $ sudo userdel --backup -r <user>
  ```

* `usermod`: изменяет параметры учётной записи пользователя.

  ```bash
  $ # Переименовать пользователя
  $ usermod -l <user> <new-user>
  ```

  ```bash
  $ # Добавить в группу
  $ usermod -aG <group> <user>
  ```

  ```bash
  $ # Заблокировать учётную запись
  $ usermod -L <user>
  ```

* `passwd`: меняет пароль пользователя.

  ```bash
  $ # Изменить пароль текущего пользователя (Ctrl+D для отмены)
  $ sudo passwd
  ```

  ```bash
  $ # Изменить пароль пользователя
  $ sudo passwd <user>
  ```

  ```bash
  $ # Принудительная смена пароля при следующем входе
  $ sudo passwd -e <user>
  ```

* `login`: начинает сессию на системе.

  ```bash
  $ # Войти
  $ login
  ```

  ```bash
  $ # Войти как пользователь
  $ sudo login <user>
  ```

  ```bash
  $ # Выйти
  $ logout
  ```

* `adduser`, `newusers`: интерфейсы для добавления пользователей.

  ```bash
  $ # Добавить пользователя
  $ sudo adduser <user>
  ```

  ```bash
  $ # Добавить пользователя(ей) из файла (username:password:UID:GID:User Info:/home/username:/bin/bash)
  $ sudo newusers < <(echo '<user>:<password>::<GID>:,,,:/home/<user>:/bin/bash')
  ```

* `chown`: меняет владельца и группу файла.

  ```bash
  $ # Сменить владельца
  $ touch data.log
  $ ls -l data.log 
  -rw-rw-r-- 1 nstu nstu ...
  $ sudo chown student data.log 
  $ ls -l data.log 
  -rw-rw-r-- 1 student nstu ...
  ```

  ```bash
  $ # Сменить владельца и группу
  $ sudo chown student:course data.log 
  $ ls -l data.log 
  -rw-rw-r-- 1 student course ...
  ```

* `chmod`: меняет права доступа.

  ```bash
  $ # Добавить право выполнения для пользователя
  $ touch data.sh
  $ ls -l data.sh 
  -rw-rw-r-- 1 nstu nstu 0 ...
  $ chmod u+x data.sh 
  $ ls -l data.sh 
  -rwxrw-r-- 1 nstu nstu 0 ...
  ```

  ```bash
  $ # Рекурсивно убрать право записи для пользователя
  $ mkdir -p backup/version-{1..5}/src
  $ tree -p backup/
  [drwxrwxr-x]  backup/
  ├── [drwxrwxr-x]  version-1
  │   └── [drwxrwxr-x]  src
  ├── [drwxrwxr-x]  version-2
  │   └── [drwxrwxr-x]  src
  ├── [drwxrwxr-x]  version-3
  │   └── [drwxrwxr-x]  src
  ├── [drwxrwxr-x]  version-4
  │   └── [drwxrwxr-x]  src
  └── [drwxrwxr-x]  version-5
      └── [drwxrwxr-x]  src
  $ chmod -R u-w backup/version-*
  $ tree -p backup/
  [drwxrwxr-x]  backup/
  ├── [dr-xrwxr-x]  version-1
  │   └── [dr-xrwxr-x]  src
  ├── [dr-xrwxr-x]  version-2
  │   └── [dr-xrwxr-x]  src
  ├── [dr-xrwxr-x]  version-3
  │   └── [dr-xrwxr-x]  src
  ├── [dr-xrwxr-x]  version-4
  │   └── [dr-xrwxr-x]  src
  └── [dr-xrwxr-x]  version-5
      └── [dr-xrwxr-x]  src
  $ rm -r  backup/version-1/src/
  rm: remove write-protected directory 'backup/version-1/src/'? y
  rm: cannot remove 'backup/version-1/src/': Permission denied
  $ sudo rm -r backup/
  ```

* `groups`: показывает, в какие группы входит пользователь.

  ```bash
  $ # Группы текущего пользователя
  $ groups
  nstu sudo vboxsf
  ```

  ```bash
  $ # Группы конкретного пользователя
  $ groups student
  student : student course
  ```

* `chgrp`: меняет группу-владельца файла.

  ```bash
  $ # Сменить группу файла
  $ sudo chgrp nstu data.log
  $ ls -l data.log 
  -rw-rw-r-- 1 student nstu ...
  ```

<!-- РАЗДЕЛ  -->

# Управление процессами и заданиями

[Наверх](#содержание)

## Процессы

[Наверх](#содержание)

Процесс — это запущенный экземпляр программы.
Каждый процесс имеет уникальный идентификатор (PID).
Каждый запущенный процесс в системе представлен каталогом в `/proc`, имя которого равно PID процесса.
Например, `/proc/1` содержит информацию о процессе с PID 1.

```bash
$ cd /proc/1
$ sudo ls
arch_status  cgroup      coredump_filter     environ  gid_map            limits     mem         net        oom_score      personality  schedstat  smaps_rollup  status          timers
attr         clear_refs  cpu_resctrl_groups  exe      io                 loginuid   mountinfo   ns         oom_score_adj  projid_map   sessionid  stack         syscall         timerslack_ns
autogroup    cmdline     cpuset              fd       ksm_merging_pages  map_files  mounts      numa_maps  pagemap        root         setgroups  stat          task            uid_map
auxv         comm        cwd                 fdinfo   ksm_stat           maps       mountstats  oom_adj    patch_state    sched        smaps      statm         timens_offsets  wchan
```

* `/proc/[PID]/cmdline`: содержит полную командную строку процесса
* `/proc/[PID]/exe`: символическая ссылка на исполняемый файл процесса
* `/proc/[PID]/comm`: имя (filename) выполняемой команды
* `/proc/[PID]/status`: статус (ID, ID родителя, ...) и состояние (running, sleeping, ...), использование памяти, ...
* `/proc/[PID]/maps`: карта памяти процесса (адреса отображённых файлов и областей памяти)
* `/proc/[PID]/smaps`: расширенная версия maps с более подробной статистикой использования памяти
* `/proc/[PID]/mem`: фактическое содержимое памяти процесса (можно читать по определённым смещениям)
* `/proc/[PID]/io`: информация об операциях ввода/вывода процесса
* `/proc/[PID]/limits`: ограничения по ресурсам (размер файлов, CPU time, память и т.д.), которые может потреблять процесс
* `/proc/[PID]/oom_score`: «оценка», которую ядро использует, чтобы выбрать процесс для убийства при нехватке памяти (OOM)
* `/proc/[PID]/fd`: каталог со ссылками на все открытые файловые дескрипторы процесса (файлы, сокеты, каналы и т.д.)
* `/proc/[PID]/fdinfo`: подробная информация о файловых дескрипторах
* `/proc/[PID]/environ`: переменные окружения процесса
* `/proc/[PID]/sched`: информация планировщика для процесса
* `/proc/[PID]/stat`: статус процесса в формате, удобном для парсинга программами (время жизни, число потоков и т.д.)
* `/proc/[PID]/net`: сетевые статистики и конфигурация процесса (например, если он создал network namespace)
* ...

Процесс в Linux может находиться в одном из следующих состояний:

* **Running (R)**: процесс выполняется на CPU или ожидает выполнения, как только CPU станет доступен.
* **Interruptible Sleep (S)**: процесс ждёт завершения события или доступности ресурса; может быть прерван сигналом.
* **Uninterruptible Sleep (D)**: процесс ждёт завершения I/O (диск, сеть и т.п.) и не может быть прерван.
* **Stopped (T)**: выполнение процесса остановлено (например, сигналом `SIGSTOP`).
* **Zombie (Z)**: процесс завершился, но запись о нём остаётся в таблице процессов, чтобы родитель мог считать код завершения.
* ...

Взаимодействие ядра и процессов:

* **Планировщик процессов (Process Scheduler)**:
  Планировщик отвечает за распределение CPU-времени между процессами.
  По умолчанию Linux использует Completely Fair Scheduler (CFS), который стремится «честно» распределять CPU-время на основе приоритета и истории выполнения.

* **Создание процессов (Process Creation)**:
  Процессы создаются системными вызовами `fork()` или `clone()`, которые дублируют существующий процесс.
  Затем `exec()` может заменить образ (image) процесса на новую программу.

* **Завершение процессов (Process Termination)**:
  Процесс завершается либо добровольно, вызывая `exit()`, либо принудительно — когда другой процесс посылает сигнал (например, `SIGKILL`).

* **Межпроцессное взаимодействие (IPC)**:
  Linux предоставляет несколько механизмов IPC: каналы (pipes), очереди сообщений, разделяемую память и семафоры — для обмена данными и синхронизации.

* **Иерархия процессов и «осиротевшие» процессы**:
  Каждый процесс (кроме первоначального init/systemd) создаётся другим процессом (родителем).
  Если родитель завершается раньше дочерних процессов, они становятся «сиротами» и усыновляются процессом init/systemd.

* **Сигналы (Signals)**:
  Сигналы — форма межпроцессного взаимодействия, уведомляющая процесс о событии.
  Сигналами можно остановить, продолжить или завершить процесс и т.д.

* **Контрольные группы (cgroups)**:
  Функция ядра, позволяющая организовывать процессы в иерархические группы для управления и ограничения ресурсов.

* **Пространства имён (Namespaces)**:
  Механизм изоляции и виртуализации системных ресурсов между процессами.
  Например, PID namespaces изолируют пространство PID, так что процессы в разных PID namespaces могут иметь одинаковые PID.

## Задания (Jobs)

[Наверх](#содержание)

Задание (job) — это один или несколько процессов, запущенных из одной и той же сессии shell/терминала, которыми можно управлять как единым целым.
Команда `jobs` показывает список текущих заданий.

* Задания можно останавливать, запускать и управлять ими напрямую из оболочки с помощью команд управления заданиями.
* Задания имеют job ID внутри оболочки, которые отличаются от PID.
* Задания могут выполняться на переднем плане (foreground) или в фоне (background) терминала.

## Соответствующие команды и примеры

[Наверх](#содержание)

* `top` (`htop`): показывает процессы и состояние системы.

  ```bash
  $ # Показать процессы пользователя
  $ top -u nstu
  ```

  ```bash
  $ # Мониторить процесс по PID
  $ top -p 1
  ```

* `ps`: выводит информацию об активных процессах.

  ```bash
  $ # Показать процессы пользователя
  $ ps -u nstu
  ```

  ```bash
  $ # Показать дерево процессов (для текущей сессии терминала)
  $ ps --forest
  ```

  ```bash
  $ # Показать информацию по PID
  $ ps -p 1
  ```

  ```bash
  $ # Показать все процессы с подробной информацией
  $ ps -aux
  ```

* `pidof`: получить PID процесса по имени (см. также `pgrep`).

  ```bash
  $ pidof bash
  ```

* `pstree`: показывает дерево процессов.

  ```bash
  $ # Показать дерево для PID
  $ pstree 1
  ```

  ```bash
  $ # Дерево текущей shell-сессии (с PID, владельцем)
  $ pstree -pu $$
  ```

  ```bash
  $ # Дерево процессов пользователя
  $ pstree nstu
  ```

* `kill`: отправляет сигнал процессу (часто используется для завершения процессов).

  ```bash
  $ # Завершить процесс по PID (мягко)
  $ kill -SIGTERM <PID>
  ```

  ```bash
  $ # Завершить процесс по PID (жёстко)
  $ kill -SIGKILL <PID>
  ```

  ```bash
  $ # Список сигналов
  $ kill -l
  ```

* `killall`: завершает процессы по имени.

  ```bash
  $ # Завершить по имени
  $ killall <name>
  ```

  ```bash
  $ # Завершить процессы пользователя (жёстко)
  $ killall -u <user> -SIGKILL
  ```

* `time`: запускает программу и показывает затраты системных ресурсов.

  ```bash
  $ # Измерить время выполнения
  $ time sleep 1

  real    0m1.005s
  user    0m0.001s
  sys     0m0.004s
  ```

* `nice` (`renice`): изменяет приоритет процесса.

  * Диапазон приоритета: от -20 до 19 (от самого высокого к самому низкому), приоритет пользовательских процессов по умолчанию — 0
  * Планировщик ядра решает, какой процесс запускать следующим, исходя из этих значений приоритета
  * Команда `nice` запускает процесс с изменённым приоритетом планирования
  * При запуске через `nice` можно указать уровень «niceness» (значение, добавляемое к приоритету процесса)
  * Команда `renice` изменяет приоритет уже работающего процесса

  ```bash
  $ # Запустить с (пониженным) приоритетом
  $ sleep 100 &
  $ top -n 1 -u nstu | grep "$(pidof sleep)"
  ... nstu      20   0    8696   2048   2048 S   0,0   0,1   0:00.00 sleep
  $ killall sleep
  $ nice -n 10 sleep 100 &
  $ top -n 1 -u nstu | grep "$(pidof sleep)"
  ... nstu      30  10    8696   2048   2048 S   0,0   0,1   0:00.00 sleep 
  ```

  ```bash
  $ # Renice
  $ renice -n 20 -p $(pidof sleep)
  26964 (process ID) old priority 10, new priority 19
  $ top -n 1 -u nstu | grep "$(pidof sleep)"
  ... nstu      39  19    8696   2048   2048 S   0,0   0,1   0:00.00 sleep 
  ```

* `fg`: переводит задание на передний план (используйте `Ctrl+Z`, чтобы остановить).

  ```bash
  $ # Вернуть самое недавнее фоновое задание на передний план
  $ # Нажмите Ctrl+C, чтобы прервать sleep
  $ sleep 100 &
  $ fg
  sleep 100
  ^C
  ```

  ```bash
  $ # По ID (можно для нескольких)
  $ # Нажмите Ctrl+C, чтобы прервать sleep
  $ sleep 100 &
  $ fg 1
  sleep 100
  ^C
  ```

  ```bash
  $ # По имени (можно для нескольких)
  $ # Нажмите Ctrl+C, чтобы прервать sleep
  $ fg "%sleep" 
  sleep 100
  ^C
  ```

* `bg`: продолжает выполнение задания в фоне.

  ```bash
  $ # Продолжить самое недавнее задание в фоне
  $ sleep 100
  ^Z
  [1]+  Stopped                 sleep 100
  $ bg
  [1]+ sleep 100 &
  $ fg
  sleep 100
  ^C
  ```

  ```bash
  $ # По ID (можно для нескольких)
  $ sleep 100
  ^Z
  [1]+  Stopped                 sleep 100
  $ bg 1
  [1]+ sleep 100 &
  $ fg
  sleep 100
  ^C
  ```

  ```bash
  $ # По имени (можно для нескольких)
  $ sleep 100
  ^Z
  [1]+  Stopped                 sleep 100
  $ bg "%sleep"
  [1]+ sleep 100 &
  $ fg
  sleep 100
  ^C
  ```

* `jobs`: показывает задания, выполняющиеся или остановленные.

  ```bash
  $ # Показать все текущие задания вместе с PID
  $ sleep 100 &
  $ sleep 200 &
  $ sleep 300 &
  $ jobs -l
  [1]  26991 Running                 sleep 100 &
  [2]- 26992 Running                 sleep 200 &
  [3]+ 26993 Running                 sleep 300 &
  $ killall sleep
  [1]   Terminated              sleep 100
  [2]-  Terminated              sleep 200
  [3]+  Terminated              sleep 300
  $ jobs
  ```

* `at`: выполняет команды в указанное время.

  ```bash
  $ # Выполнить в выбранное время, например HH:MM [AM/PM] MM DD
  $ # Введите команд(ы) и нажмите `Ctrl + D`
  $ at now + 1 hour
  ```

  ```bash
  $ # Показать очередь запланированных заданий
  $ atq
  ```

  ```bash
  $ # Удалить задание из очереди
  $ atrm 1
  ```

  ```bash
  $ # Выполнить, когда нагрузка системы опустится ниже заданного уровня
  $ # Введите команд(ы) и нажмите `Ctrl + D`
  $ batch
  ```

* `crontab`: планирование периодических фоновых заданий (см. [crontab guru](https://crontab.guru/)).

  ```bash
  $ # Редактировать crontab текущего пользователя
  $ crontab -e
  ```

  ```bash
  $ # Показать crontab текущего пользователя
  $ crontab -l
  ```

  ```bash
  $ # Удалить crontab текущего пользователя
  $ crontab -r
  ```

<!-- РАЗДЕЛ  -->

# Мониторинг системы

[Наверх](#содержание)

## Ресурсы

[Наверх](#содержание)

* **Управление процессами**: `ps`, `top`, `htop`, `pstree`
* **Использование CPU**: `top`, `htop`
* **Использование памяти**: `free`, `vmstat`, `top`, `htop`
* **Использование диска**: `df` (`df -i` — inodes), `du`, `iotop`, `iostat`
* **Системная нагрузка**: `uptime`, `w`, `top`, `htop`
* **Статистика I/O**: `iostat`, `iotop`
* **Сетевой трафик и статистика**: `netstat`, `ifconfig`, `ip`, `nload`, `iftop`, `ss`
* **Использование swap**: `swapon`, `swapoff`, `vmstat`, `free`
* **Сервисы**: `systemctl` (см. следующий раздел)
* **Логи**: `journalctl`

## Сервисы

[Наверх](#содержание)

Сервисы (демоны) — это приложения или программы, которые работают в фоновом режиме и выполняют системные функции либо предоставляют различные сервисы пользователям и другим программам.
В Ubuntu сервисами и инициализацией системы управляет systemd (`systemd`).
Сервисы описываются unit-файлами. Unit-файлы задают, как управлять сервисом (start, stop, ...).

Базовое управление сервисами:

* **Запустить**: `sudo systemctl start [service_name]`
* **Остановить**: `sudo systemctl stop [service_name]`
* **Перезапустить**: `sudo systemctl restart [service_name]`
* **Включить автозапуск**: `sudo systemctl enable [service_name]` (запуск при загрузке)
* **Отключить автозапуск**: `sudo systemctl disable [service_name]` (не запускать при загрузке)
* **Статус**: `sudo systemctl status [service_name]`
* **Перезагрузить конфигурацию systemd**: `sudo systemctl daemon-reload` (после изменений unit-файлов)
* **Список сервисов**: `systemctl list-units --type=service`
* **Логи (журнал)**: `journalctl`

## Соответствующие команды и примеры

[Наверх](#содержание)

* `watch`: периодически выполняет программу, показывая вывод на весь экран.

  ```bash
  $ # Повторять команду каждую секунду
  $ watch -n 1 ls -l
  ```

  ```bash
  $ # Подсвечивать различия при обновлении
  $ watch -n 1 -d ls -l
  ```

* `mount` (`umount`): монтирование/размонтирование файловых систем (в VM может потребоваться добавить USB в настройках).

  ```bash
  $ # Смонтировать (usb-устройство sda1)
  $ sudo mount /dev/sda1 /mnt
  $ cd /mnt
  $ ls
  ```

  ```bash
  $ # Размонтировать
  $ sudo umount /mnt
  ```

  ```bash
  $ # Смонтировать в конкретный каталог и размонтировать
  $ sudo mkdir /media/$USER/usb
  $ sudo mount /dev/sda1 /media/$USER/usb
  $ sudo umount /dev/sda1
  $ sudo rmdir /media/$USER/usb
  ```

* `udisksctl`: утилита командной строки для взаимодействия с демоном UDisks (в VM может потребоваться добавить USB в настройках).

  ```bash
  $ # Проверить статус
  $ udisksctl status
  ```

  ```bash
  $ # Смонтировать
  $ udisksctl mount -b /dev/sda1
  ```

  ```bash
  $ # Получить информацию
  $ udisksctl info -b /dev/sda1
  ```

  ```bash
  $ # Размонтировать
  $ udisksctl unmount -b /dev/sda1
  ```

* `uname`: показывает информацию о системе.

  ```bash
  $ # Показать всю информацию о системе
  $ uname -a
  Linux nstu 6.5.0-15-generic #15~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Fri Jan 12 18:54:30 UTC 2 x86_64 x86_64 x86_64 GNU/Linux
  ```

* `lsb_release`: показывает информацию о дистрибутиве.

  ```bash
  $ # Показать всю информацию о дистрибутиве
  $ lsb_release -a
  No LSB modules are available.
  Distributor ID: Ubuntu
  Description:    Ubuntu 22.04.3 LTS
  Release:        22.04
  Codename:       jammy
  ```

* `id` (`whoami`): показывает идентификаторы пользователя и групп.

  ```bash
  $ # Информация о текущем пользователе
  $ id
  uid=1000(nstu) gid=1000(nstu) groups=1000(nstu),27(sudo),999(vboxsf)
  ```

  ```bash
  $ # Информация о конкретном пользователе
  $ id student
  uid=1003(student) gid=1004(student) groups=1004(student),1002(course)
  ```

* `w`: показывает, кто вошёл в систему и чем занимается.

  ```bash
  $ # Показать, кто вошёл и чем занимается
  $ w
  $ w
  ...
  USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
  nstu     pts/0    10.0.2.2         11:51    0.00s  0.00s  0.00s w
  ```

  ```bash
  $ # Показать информацию о конкретном пользователе
  $ w student
  ...
  ```

* `uptime`: показывает, сколько система работает и среднюю нагрузку (также в верхней строке `w`).

  ```bash
  $ uptime
  ```

* `df`: показывает использование дискового пространства файловыми системами.

  ```bash
  $ # Показать использование дискового пространства
  $ df -h
  ```

* `du`: оценивает использование дискового пространства файлами/каталогами.

  ```bash
  $ # Показать использование диска (пример вывода)
  $ du -h
  Filesystem      Size  Used Avail Use% Mounted on
  tmpfs           391M  1,5M  390M   1% /run
  /dev/sda3        49G   27G   20G  57% /
  tmpfs           2,0G     0  2,0G   0% /dev/shm
  tmpfs           5,0M  4,0K  5,0M   1% /run/lock
  /dev/sda2       512M  6,1M  506M   2% /boot/efi
  nstu-share      468G  108G  361G  23% /home/nstu/nstu-share
  tmpfs           391M   76K  391M   1% /run/user/1000
  tmpfs           391M   84K  391M   1% /run/user/128
  ```

  ```bash
  $ # Показать общий размер каталога
  $ du -sh /usr/bin
  203M    /usr/bin 
  ```

  ```bash
  $ # Показать размеры всех файлов и каталогов
  $ du -ah /usr/bin
  ...
  32K     /usr/bin/usbhid-dump
  108K    /usr/bin/pdftohtml
  24K     /usr/bin/openvt
  40K     /usr/bin/id
  12K     /usr/bin/piconv
  203M    /usr/bin  
  ```

* `htop`: аналог `top` с расширенным интерактивным интерфейсом (`sudo apt install htop`).

  ```bash
  $ # Показать процессы конкретного пользователя
  $ htop -u nstu
  ```

  ```bash
  $ # Мониторить процессы по PID
  $ htop -p 1
  ```

* `vmstat`: показывает статистику виртуальной памяти.

  ```bash
  $ vmstat
  ```

* `free`: показывает объём свободной и занятой памяти.

  ```bash
  $ free -h
  ```

* `iostat`: показывает CPU-статистику и статистику ввода/вывода для устройств и разделов.

  ```bash
  $ # Показать CPU и I/O статистику
  $ iostat
  ```

  ```bash
  $ # Показать статистику CPU
  $ iostat -c
  ```

* `nethogs`: показывает использование сети по процессам (`sudo apt install nethogs`).

  ```bash
  $ # Показать использование сети
  $ sudo nethogs
  ```

<!-- РАЗДЕЛ  -->

# Сеть (Networking)

[Наверх](#содержание)

## Компоненты сети

[Наверх](#содержание)

* **Сетевое оборудование:**

  * Маршрутизаторы, коммутаторы, сетевые карты и другие устройства.

* **Сетевые модели:**

  * Модель OSI: Физический, Канальный, Сетевой, Транспортный, Сеансовый, Представления и Прикладной уровни.
  * Модель TCP/IP: Канальный (Link), Интернет (Internet), Транспортный (Transport) и Прикладной (Application) уровни.

* **IP-адресация:**

  * У каждого устройства в сети есть IP-адрес.
  * Существуют адреса IPv4 и IPv6; понимание подсетей (subnetting) важно для проектирования и диагностики сетей.

* **Сетевые протоколы:**

  * Протоколы TCP, UDP, ICMP и другие — это правила и стандарты, определяющие сетевое взаимодействие.

* **Сетевые службы:**

  * DNS (Domain Name System), DHCP (Dynamic Host Configuration Protocol) и другие службы необходимы для функционирования сети.

* **Конфигурация сети:**

  * CLI для NetworkManager: `nmcli`.
  * Статический IP или динамический — через DHCP-сервер.

* **Настройка фаервола:**

  * `iptables` — инструмент для задания правил, разрешающих или блокирующих трафик (или `nftables`).
  * `ufw` предоставляет интерфейсы для управления `iptables`.

* **Маршрутизация и коммутация:**

  * Понимание, как данные маршрутизируются по сети с помощью таблиц маршрутизации (команды `route` или `ip route`).
  * Linux можно настроить как маршрутизатор, пересылающий трафик между разными сетями.

* **Диагностика сети:**

  * Команды `ping`, `traceroute`, `netstat`, `ss`, `dig`, `nslookup`, `tcpdump`.

* **Безопасность сети:**

  * SSH для безопасного удалённого доступа.
  * Базовые знания о сетевом шифровании, например TLS/SSL.
  * Понимание механизмов аутентификации: ключи и сертификаты.

* **Сетевые файловые системы:**

  * NFS и Samba для обмена файлами по сети.

* **Мониторинг и управление сетью:**

  * Инструменты вроде Nagios, Zabbix или Prometheus для мониторинга.
  * SNMP (Simple Network Management Protocol) для управления сетью.

* **Виртуальные сети:**

  * Понимание виртуальных сетей, мостов и туннелей (например, VPN).
  * Инструменты вроде `virt-manager` для сетевых настроек виртуальных машин.

* **Сети контейнеров:**

  * С ростом контейнеризации (Docker, Kubernetes) важно понимать, как работает сеть внутри контейнеров и между ними.

## Задачи в сетевом администрировании

[Наверх](#содержание)

* **Проверка сетевой конфигурации:**

  * `ip addr`: показать текущую конфигурацию сети, включая IP-адреса, маски подсетей и сетевые интерфейсы.
  * `hostname`: посмотреть или установить имя хоста.

* **Управление сетевыми подключениями:**

  * `nmcli`: утилита командной строки для управления NetworkManager, полезна для настройки и управления соединениями.
  * `nmtui`: текстовый интерфейс (TUI) для NetworkManager, более «дружелюбный» способ менять сетевые настройки.

* **Диагностика сетевых проблем:**

  * `ping`: проверить доступность другого узла в сети.
  * `traceroute` или `tracepath`: проследить маршрут пакетов до узла, чтобы понять, где соединение замедляется или обрывается.
  * `ss`: показать сетевые соединения, таблицы маршрутизации, статистику интерфейсов, masquerade-соединения и multicast-memberships.

* **Анализ сетевого трафика:**

  * `tcpdump`: мощный анализатор пакетов в командной строке; полезен для отладки сети и мониторинга трафика.
  * `wireshark` (TShark в терминале): анализатор сетевых протоколов для глубокой инспекции сотен протоколов.

* **Настройка сетевых сервисов:**

  * `iptables` или `nftables`: инструменты командной строки для настройки и просмотра таблиц правил фильтрации IP-пакетов в ядре Linux.

* **Тестирование производительности сети:**

  * `speedtest-cli`: тестирование интернет-канала через speedtest.net из командной строки.
  * `iperf`: измерение максимально достижимой пропускной способности в IP-сетях.

* **Сканирование сети и портов:**

  * `nmap`: инструмент исследования сети и сканер портов/безопасности.

* **Управление DNS и доменной информацией:**

  * `dig`: запросы к DNS-серверам (адреса хостов, MX, NS и т.п.).
  * `nslookup`: запросы к DNS-серверам доменных имён.

* **Автоматизация сетевых задач:**

  * `ssh`: безопасное подключение к удалённым серверам для выполнения команд.
  * `scp` или `rsync`: безопасное копирование файлов между хостами.

* **Мониторинг сетевой нагрузки и трафика:**

  * `iftop` или `nload`: отображение использования полосы пропускания на интерфейсе.
  * `vnstat`: мониторинг сетевого трафика и пропускной способности в реальном времени.

## Соответствующие команды и примеры

[Наверх](#содержание)

* `ping`: проверяет сетевое соединение с сервером.

  ```bash
  $ # Проверить доступность hostname/ip/domain
  $ ping nstu  
  ```

  ```bash
  $ # Отправить 10 запросов с интервалом 1 секунда
  $ ping -c 10 -i 1 nstu  
  ```

* `host`: выполняет DNS-запросы, переводя доменные имена в IP-адреса и наоборот.

  ```bash
  $ host 8.8.8.8
  8.8.8.8.in-addr.arpa domain name pointer dns.google.
  ```

* `hostname`: посмотреть или установить hostname системы.

  ```bash
  $ # Показать текущий hostname системы
  $ hostname
  ```

  ```bash
  $ # Изменить hostname системы
  $ hostname <name>
  ```

* `ssh`: Secure Shell — протокол безопасного доступа к удалённым машинам.

  ```bash
  $ # Подключиться к <host> как <user>
  $ ssh <user>@<host>
  ```

  ```bash
  $ # Подключиться на конкретный порт
  $ ssh -p <port> <user>@<host>
  ```

  ```bash
  $ # Подключиться с использованием ключа
  $ ssh -i <path> <user>@<host>
  ```

  ```bash
  $ # Подключиться с X forwarding
  $ ssh -X <path> <user>@<host>
  ```

  ```bash
  $ # Подключиться с пробросом локального порта
  $ ssh -L <local_port>:<destination_address>:<destination_port> <user>@<host>
  ```

* `scp`: безопасное копирование файлов между хостами по сети.

  ```bash
  $ # Скопировать на удалённый хост
  $ scp <path>/<file> <user>@host:/<path>
  ```

  ```bash
  $ # Скопировать с удалённого хоста
  $ scp  <user>@host:/<path>/<file> <path>
  ```

  ```bash
  $ # Рекурсивно скопировать каталог на удалённый хост
  $ scp -r <directory> <user>@host:/<path>
  ```
