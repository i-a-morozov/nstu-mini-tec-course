<!-- Every shell includes hell  -->


<!-- SECTION -->
# Contents
- [Introduction](#introduction)
- [BASH and command line basics](#bash-and-command-line-basics)
  - [Command structure](#command-structure)
  - [BASH features](#bash-features)
  - [Command line navigation](#command-line-navigation)
  - [Command continuation](#command-continuation)
- [Compound commands](#compound-commands)
  - [Separation of commands](#separation-of-commands)
  - [Pipes](#pipes)
  - [Background](#background)
  - [Grouping of commands](#grouping-of-commands)
- [Redirections](#redirections)
  - [Standard redirections](#standard-redirections)
  - [Process substitution](#process-substitution)
  - [Here documents and here strings](#here-documents-and-here-strings)
  - [Advanced redirections](#advanced-redirections)
- [Script files](#script-files)
   - [Layout](#layout)
   - [Execution](#execution)
   - [Best practices](#best-practices)
- [Pathname expansion](#pathname-expansion)
   - [Brace expansion](#brace-expansion)
   - [Wildcards](#wildcards)
   - [Globbing](#globbing)
- [Variables](#variables)
   - [Customization](#customization)
   - [Parameter substitution](#parameter-substitution)
   - [Environment variables](#environment-variables)
   - [Special characters and variables](#special-characters-and-variables)
   - [Arrays](#arrays)
- [Math operations](#math-operations)
   - [Operations](#operations)
   - [Functions (bc)](#functions-bc)
   - [Examples](#examples)
   - [Exit status of math operations](#exit-status-of-math-operations)
- [Flow control](#flow-control)
   - [Test](#test)
   - [Exit codes](#exit-codes)
   - [Conditional execution](#conditional-execution)
   - [Ternary operator (math)](#ternary-operator-math)
   - [Logical operator (math)](#logical-operator-math)
   - [If](#if)
   - [Case](#case)
   - [Trap](#trap)
- [Loops](#loops)
   - [While](#while)
   - [Until](#until)
   - [For](#for)
- [Functions](#functions)
- [Input and parsing](#input-and-parsing)
   - [Input](#input)
   - [Parsing arguments and options](#parsing-arguments-and-options)
- [Managing scripts, aliases, and other](#managing-scripts-aliases-and-other)
   - [A good place to put your scripts](#a-good-place-to-put-your-scripts)
   - [Aliases vs functions vs scripts](#aliases-vs-functions-vs-scripts)
   - [.bashrc](#bashrc)

<!-- SECTION -->
# Introduction
[Back to Top](#contents)

Mastering command line is an important skill to have in research environment.
Often, interaction with computing resources is only avalible via command line.
Proficient command line usage can save you a lot of time and effort (apart from impressing your colleagues and being a bullet point in you CV).

This course teaches you to harness `bash` scripting to streamline tasks, from simple command-line operations to writing robust automation scripts. By the end, you’ll be able to:
- Navigate and manipulate files using advanced globbing and expansion techniques
- Combine commands with pipes, redirections, and process substitution
- Write reusable scripts with variables, loops, conditionals, and error handling
- Parse inputs and design interactive tools using read, dialog, or whiptail
- Optimize your workflow with aliases, functions, and environment customization

<!-- SECTION -->
# BASH and command line basics
[Back to Top](#contents)

`bash` (Bourne-Again SHell) is a command language interpreter, or shell, for Unix-like operating systems and is the default shell in many popular Linux distributions. A shell interprets user commands and acts as a middleman between the user and the system's kernel, along with other operating system services. It provides a command-line interface (CLI) that allows users to interact with the system. The shell takes commands typed by the user and translates them into a format that the operating system can understand and act on. It can execute commands directly or launch other programs. In addition, shells offer programming constructs that enable users to write scripts: small programs that can automate tasks, manipulate files, and perform many other routine tasks.

The following command displays the path to the default user shell binary in the terminal (emulator), which is also referred to as the **standard output**:

```bash
$ echo "${SHELL}"
/bin/bash
```

In the above example, the `$` symbol represents a non-privileged user's prompt, while the `#` symbol would usually indicate a privileged root user's prompt. After the prompt (i.e. after `$` or `#` symbols), the command `echo "${SHELL}"` is entered (you need to press `Enter` key to execute it), which displays the value of the `SHELL` variable. Note, `SHELL` is a variable name, while `"${SHELL}"` is how its value is referenced. The prompt then becomes ready to accept a new command. A common workflow with terminal commands is to enter one command at a time and adjust the next command according to the current command output:

```bash
$ echo "${USER}"
nstu
$ echo "${GROUPS}"
1000
```

Here the values of two different environment variables are displayed using `echo` command.

<!-- SUBSECTION -->
## Command structure
[Back to Top](#contents)

In the terminal user can enter different commands to interact with the system. In general different options and arguments can be passed to a command:

```bash
$ command [options] [arguments]
```

- `command` is the name of the program, e.g. `echo`, `ls` or `cd`

- `options` (also known as flags or switches) are commonly schematically shown inside `[]` to indicate their optional usage, `options` modify the behavior of the command and are typically preceded by a single dash or double dash
  - `-option` (short option, Unix style) is the traditional Unix/Linux style, where options are prefixed by a single dash and usually consist of a single letter, such options can often be combined without spaces in between, e.g. `ls -altrh`
  - `--option` (long option, GNU style) is a more modern, GNU-style approach for specifying options with full words, which makes it clear what the option does, for some long options their short form is also available (usually the first letter is used in this case if available)

- `arguments` are the targets or values upon which the command acts, `arguments` can also be optional

Several short options that don't require additional values (act like on/off flags) can be combined, e.g in `ls -a -l` can be written as `ls -al`. Long options cannot be combined in the same way. Some long options might require an equals sign when assigning a value, like `--option=value`.

Additionally `--` can be used by itself to signify the end of the command options. After `--`, all following inputs are treated as arguments, not as options. This is particularly useful when `-` present in commands.

Equally important concept is the command **exit code**. Executing a command returns a value that indicates its execution status. The **exit code** of the most recent command can be checked with `echo $?` command:

```bash
$ echo "${USER}"
nstu
$ echo "${?}"
0
```

Zero value indicates successful execution, while values other than zero correspond to some kind of an error.

To illustrate the above concepts `ls` command can be used. It is used to list files and directories. First, create several nested directories:

```bash
$ mkdir -p versions/v-{0.1.0,0.2.0,0.2.1,1.0.0,1.0.1}
$ tree versions
versions
├── v-0.1.0
├── v-0.2.0
├── v-0.2.1
├── v-1.0.0
└── v-1.0.1
5 directories, 0 files
```

Now `ls` can be used to list files (directories in our case). List everything in `versions` directory:

```bash
$ ls versions
v0.1.0  v0.2.0  v0.2.1  v1.0.0  v1.0.1
$ ls -- versions
v0.1.0  v0.2.0  v0.2.1  v1.0.0  v1.0.1
```

Use `--classify` (long) option to classify listed items (here `/` is appended to all listed names since all items are in fact directories):

```bash
$ ls --classify versions
v-0.1.0/  v-0.2.0/  v-0.2.1/  v-1.0.0/  v-1.0.1/
```

Similarly a short form `-F` of the same option can be used:

```bash
$ ls -F versions
v-0.1.0/  v-0.2.0/  v-0.2.1/  v-1.0.0/  v-1.0.1/
```

One or several short flag-like options can be combined:

```bash
$ ls -mF versions
v-0.1.0/, v-0.2.0/, v-0.2.1/, v-1.0.0/, v-1.0.1/
```

Use command arguments to exclude listing of patch versions in reversed order (note, `--` is not necessary here and is used to visually separate arguments from options):

```bash
$ ls -r -- versions/v-*[0]
versions/v-1.0.0:
versions/v-0.2.0:
versions/v-0.1.0:
```

In the above example a pattern `v-*[0]` was used to show only directories that end with zero. Similar effect can be achieved using `hide` long option:

```bash
$ ls -r --hide='v-*[^0]' -- versions
v-1.0.0  v-0.2.0  v-0.1.0
$ rm -r versions
```

Again, a pattern `'v-*[^0]'` was used that now hides directories that do not end with a zero. Note, this will work as intended only if patch numbers are in `{0..9}` range. The last command `rm -r versions` removes versions` directory and all its subdirectories.

The above examples illustrate the usage of `ls` command with different options and arguments. Use `man command` to see all available option(s) and the form argument(s) for different commands, e.g. look at `pwd`, `ls`, `cd`, `cp`, `mv` and `rm`.

A long command can be split across several lines with `\` (write `\` and press `Enter` to start a new line):

```bash
$ mkdir -p versions/v-{0.1.0,0.2.0,0.2.1,1.0.0,1.0.1}
$ ls \
> -r --hide='v-*[^0]' \
> -- \
> versions
v-1.0.0  v-0.2.0  v-0.1.0
$ rm -r versions
```

<!-- SUBSECTION -->
## BASH features
[Back to Top](#contents)

`bash` is a domain specific language, it provides a robust environment for scripting and task automation. Its main purpose is user interaction with the system and automation of repeated routine tasks via scripts. `bash` has several features that make it powerful and flexible:

- **Command Processor**: Processes user commands, entered by the user at the command prompt.
- **Scripting Language**: Scripting language allowing users to write complex programs that perform batch processing and automate tasks.
- **Environment Control**: Provides the ability to control the operating environment of the system, including managing files and directories, starting and stopping services.
- **User Interface**: Powerful and efficient CLI.
- **Piping and Redirection**: Allows for the output of one command to be used as the input to another (piping), and it can also redirect input and output from and to files or programs.
- **Job Control**: Supports job control, which allows users to stop, start, and manage background and foreground processes.
- **Expansion**: Features different types of expansion (brace expansion, tilde expansion, variable expansion, command substitution, etc.) for generation of complex command lines.
- **History**: Keeps a history of commands that have been entered, allowing users to easily recall, edit, and rerun past commands.
- **Customization**: Users can customize their shell environment using a file called `.bashrc` (aliases, functions, variables, and more).
- **Compatibility**: Aims to be portable across different Unix-like systems.

<!-- SUBSECTION -->
## Command line navigation
[Back to Top](#contents)

Command line navigation can greatly enhance productivity and reduce the amount of typing. Here are some key techniques and shortcuts:

- **Tab Completion**:
   - **Basic Completion**: Press the `Tab` key while typing a command or file name. `bash` will auto-complete the name if it is uniquely identified. If there are multiple matches, pressing `Tab` twice will display all possible completions.
   - **Command Completion**: When typing a command, `Tab` completion also works for command names.
   - **File and Directory Completion**: Works for file and directory names. If you type a few characters of a file/directory name and press `Tab`, `bash` will auto-complete it.

- **Searching Command History (`Ctrl`+`R`)**:
   - To search through your command history, press `Ctrl`+`R`. Start typing a part of the command you're looking for. Bash will dynamically search your command history and present the matches.
   - Press `Ctrl`+`R` again to cycle through other matches.
   - Once you find the desired command, press `Enter` to execute it, or `Right Arrow` or `End` to edit it.

- **Navigating within the Command Line**:
   - `Ctrl`+`A`: Move to the beginning of the line.
   - `Ctrl`+`E`: Move to the end of the line.
   - `Ctrl`+`Left Arrow`/`Ctrl`+`Right Arrow`: Move the cursor between words/arguments.

- **Manipulating Command History**:
   - **Using the `history` Command**: Type `history` to display recent commands. Use `history N` to display the last N commands.
   - **Re-executing Commands**: Use `!N` to re-execute the Nth command in the history list. For example, `!100` will execute the 100th command in your history.
   - **Re-executing the Last Command**: Use `!!` to quickly re-execute the last command.

- **Other Useful Shortcuts**:
   - `Ctrl`+`U`: Cut everything before the cursor to the clipboard.
   - `Ctrl`+`K`: Cut everything after the cursor to the clipboard.
   - `Ctrl`+`Y`: Paste the last thing you cut.
   - `Ctrl`+`L`: Clear the screen.
   - `Ctrl`+`X` `Ctrl`+`E`: Edit command with $EDITOR
   - `Ctrl`+`N`: Next command in history
   - `Ctrl`+`P`: Previous command in history

   ## Command continuation
   [Back to Top](#contents)

   Use `\` to continue a command over multiple lines:

   ```bash
   $ echo "Hi!"
   ```

   ```bash
   $ echo \
   "Hi!"
   ```

<!-- SECTION -->
# Compound commands
[Back to Top](#contents)

So far we have seen how to enter and execute commands one at a time, but `bash` allows more advanced combination of commands. Commands combination is a powerful feature that allows to express complex behaviors. There are several options when it comes to commands combination: 
- execution of several commands in a sequence
- conditional execution
- passing the result of one command to the other.

<!-- SUBSECTION -->
## Separation of commands
[Back to Top](#contents)

It is possible to enter several commands by separating them with semicolons:

```bash
$ mkdir versions ; cd versions; mkdir v-{1..5}.0.0 ; ls ; cd ..
v-1.0.0  v-2.0.0  v-3.0.0  v-4.0.0  v-5.0.0
```

In this example `mkdir versions` command creates `versions` directory, `cd versions` changes the working directory to `versions`, `mkdir v-{1..5}.0.0` creates several directories inside the current working directory, `ls` lists files (directories in this case) and `cd ..` changes the working directory back to the starting one (goes up one level). With the `;` separator, commands are executed sequentially, regardless of whether the previous command succeeded or failed. For example, if the same command is executed again:

```bash
$ mkdir versions ; cd versions; mkdir v-{1..5}.0.0 ; ls ; cd ..
mkdir: cannot create directory ‘versions’: File exists
mkdir: cannot create directory ‘v-1.0.0’: File exists
mkdir: cannot create directory ‘v-2.0.0’: File exists
mkdir: cannot create directory ‘v-3.0.0’: File exists
mkdir: cannot create directory ‘v-4.0.0’: File exists
mkdir: cannot create directory ‘v-5.0.0’: File exists
v-1.0.0  v-2.0.0  v-3.0.0  v-4.0.0  v-5.0.0
```

all `mkdir` commands fail to create corresponding directories since they already exist. 

The above command **exit code** (here it is the **exit code** of the last command `cd ..`) :

```bash
$ echo $?
0
```

The value of `?` special variable is the execution status of `cd ..` command, i.e. the very last command in the chain, which was executed successfully (zero **exit code** indicates success, non-zero **exit code** indicate an error). For the above the **exit code** is zero, which might not be the intended behavior.

It is important to note that if one of the commands fails (i.e. `mkdir` fails), the rest of the commands are still executed. This behavior can be changed with `set` command, for example, if `set -e` is executed at the beginning of a shell session (or a script), the shell will stop on the first failed command (see `help set` for details). 

More advanced (conditional) behavior can be achieved using `&&` or `||` separators. In the case of `&&` (AND) commands after the first failed command will not be executed, for `||` (OR) the execution is stopped once the current command finishes successfully (returns zero **exit code**). `&&` and `||` separators have equal precedence, while the precedence of `;` is smaller.

For example, in the following the first command fails, which stops the execution:

```bash
$ mkdir versions && cd versions && mkdir v-{1..5}.0.0 && ls && cd ..
mkdir: cannot create directory ‘versions’: File exists
$ echo $?
1
```

Lets now break down the following command:

```bash
$ mkdir versions || cd versions && mkdir v-{1..5}.0.0 || ls ; cd ..
mkdir: cannot create directory ‘versions’: File exists
mkdir: cannot create directory ‘v-1.0.0’: File exists
mkdir: cannot create directory ‘v-2.0.0’: File exists
mkdir: cannot create directory ‘v-3.0.0’: File exists
mkdir: cannot create directory ‘v-4.0.0’: File exists
mkdir: cannot create directory ‘v-5.0.0’: File exists
v-1.0.0  v-2.0.0  v-3.0.0  v-4.0.0  v-5.0.0
```

First `mkdir versions` is executed and fails, but the separator is `||`, so the execution is continued. Next `cd versions` is executed. To this point the executed command is `mkdir versions || cd versions` which is successful, hence condition for `&&` separator is fulfilled and `mkdir v-{1..5}.0.0` is executed and fails. The full command is now `mkdir versions || cd versions && mkdir mkdir v-{1..5}.0.0` and the separator is `||`, hence `ls` is executed. Next separator is `;` and `cd ..` is executed whether the previous command `mkdir versions || cd versions && mkdir mkdir v-{1..5}.0.0 || ls` failed or not.

To sum it up, use `;` to run commands in sequence, `&&` to run the next command only if the previous succeeds, and `||` for the next command to run only if the previous fails. Note, the overall **exit code** of the compound command will be different for different separators, which can be used to control the program flow. As it can be seen, nesting of several separators can become progressively cumbersome to interpret and it is hence better to avoid complicated nestings.

A useful application of `&&` or `||` separators is to replace `if` statement where appropriate. For example, execute a command only if a file or a directory exists:

```bash
$ [ -e versions/v-1.0.0 ] && cd versions/v-1.0.0
$ echo $?
0
$ cd ../..
$ [ -e versions/v-9.0.0 ] && cd versions/v-9.0.0
$ echo $?
1
```

<!-- SUBSECTION -->
## Pipes
[Back to Top](#contents)

Execution of commands prints some output to the terminal. This output is called the **standard output** and it is in fact a file (if the command fails errors are also printed, but to the **standard error**, also a file). Some commands expect input from a file, such input can be also performed using the **standard input**. To redirect the **standard output** of one command to the **standard input** of the next command pipe `|` can be used (use `|&` to pipe both **standard output** and **standard error**). Consider the following example:

```bash
$ rm -rf versions
$ mkdir -p versions/v-{0.1.0,0.2.0,0.2.1,1.0.0,1.0.1}
$ ls versions | grep '^v.*0$' | wc -l
3
```

First remove `versions` directory if any, create several nested directories with `mkdir -p versions/v-{0.1.0,0.2.0,0.2.1,1.0.0,1.0.1}`. `ls versions` command returns a list of files that are piped to `grep` command, which uses `'^v.*0$'` pattern to filter out minor versions. The output of `grep` command is piped again into `wc -l` command, which justs counts the number of such files.

In case you need to redirect only **stderr**, you will need to use redirections (see [Redirections](#redirections) section). In the following example, **stderr** is first redirected to **stdout** which itself is redirected to **/dev/null**:

```bash
$ ls file 2>&1>/dev/null | grep file
ls: cannot access 'file': No such file or directory
```

Note, occurancies of **file** will be highlighted in the above command when executed in `bash`.

<!-- SUBSECTION -->
## Background
[Back to Top](#contents)

The `&` symbol at the end of a command in `bash` causes the command to run in the background. This will in general spawn a subshell (a child shell process of the current shell) for the background command to run in. While the prompt is immediately ready for the next command. This allows you to continue working in the shell without waiting for the command to complete. It is possible to use `&` as a separator:

```bash
$ sleep 5 & pstree $$
bash─┬─pstree
     └─sleep
```

In the above example `sleep 5` command runs in the background and the output of `pstree $$` is returned immediately. Several commands can be placed into background:

```bash
$ sleep 5 & sleep 5 & pstree $$
bash─┬─pstree
     └─2*[sleep]
```

Each command runs in its own subshell (in general), and the shell does not wait for either to complete before continuing. For the above examples, only one shell process `bash` is present in the above examples, this is due to optimization of simple commands.

Here are several practical aspects of running commands in the background:

- **Concurrency**: Start multiple tasks simultaneously. This is useful for tasks that are independent and can run concurrently without affecting each other.

- **Non-blocking Execution**: When you have a command that takes a long time to complete, and you don’t need the results immediately, you can run it in the background and continue using your terminal for other tasks.

- **Scripting**: In scripts, you might want to start a process that runs in the background and doesn’t block the execution of subsequent commands.

When running commands in the background, their **standard input** is usually closed immediately. If they try to read from **standard input**, they will receive an end-of-file. Also, output is not available unless redirected to a file. Command **exit code** is also not immediately accessible, the immediately returned **exit code** is a command submission status.

<!-- SUBSECTION -->
## Grouping of commands
[Back to Top](#contents)

Several commands can be grouped with `{}`. The commands within `{}` must be separated by semicolons or newlines, and there should be a space after the opening brace `{` and before the closing brace `}`. The closing brace must be followed by a semicolon or a newline. Grouped commands are executed in the current shell context, not a subshell (child shell of the current shell). This grouping can be used to redirect the **standard output** from all commands inside `{}`, modify and create variables, group `&&` and `||` separators.

In the example below `{}` grouping is used to first create a directory if it doesn't exist and create a file inside it:

```bash
$ rm -rf versions
$ { [ -d versions ] && touch versions/README.MD ; } || { mkdir versions ; touch versions/README.MD ; }
$ ls versions/
README.MD
$ rm versions/README.MD
$ { [ -d versions ] && touch versions/README.MD ; } || { mkdir versions ; touch versions/README.MD ; }
$ ls versions/
README.MD
```

Grouping with `{}` can be used to group commands within given shell, no subshells are created. In contrast, using `()` for grouping will in general (except simple commands that can be optimized out) with execute commands inside `()` in subshell:

Example of `()` grouping with simple command (no subshell process):

```bash
$ ( sleep 5 ) & pstree $$
bash─┬─pstree
     └─sleep
```

For a command that can't be directly optimized, subshell will be used:

```bash
$ ( sleep 5 ; sleep 5 ) & pstree $$
bash─┬─bash───sleep
     └─pstree
```

Subshell grouping can be also nested:

```bash
$ ( (sleep 5; sleep 5) & sleep 5 ; sleep 5 ) & pstree $$
bash─┬─bash─┬─bash───sleep
     │      └─sleep
     └─pstree
```

Note, in the above examples `&` was used to place commands into background.

Subshells in `bash` create a separate child process for the shell environment. When you use a subshell (by enclosing commands within parentheses `( )`), you essentially create a new instance of the current shell that is a child of the parent shell. The subshell is a duplicate of the parent shell at the time it is created, including environment variables and the current working directory. Any changes made inside the subshell do not affect the parent shell. The return status of the last command executed in the subshell is returned as the exit status of the subshell. Subshells are used in several common scenarios:

- **Temporary Environment Changes**: For example, temporarily change the current working directory temporarily without affecting the parent shell's working directory.

   ```bash
   $ echo $SHELL
   /bin/bash
   $ (SHELL=zsh; echo $SHELL)
   zsh
   $ echo $SHELL
   /bin/bash
   ```

- **Parallel Execution**: Execute commands in parallel without waiting for them to finish in the current shell. In this case subshell syntax is not required, but it makes command more explicit.

- **Complex Command Evaluation**: When a command substitution needs several commands to be executed, a subshell groups them together.

- **Pipeline Execution**: Each command in a pipeline runs in a subshell. This is the default behavior in `bash`, which is why variables set in a pipeline do not persist after the pipeline completes.

Using subshell `()` grouping can be more resource-intensive than using built-in `{}` grouping because creating a new process is more expensive than just grouping commands.


<!-- SECTION -->
# Redirections
[Back to Top](#contents)

In `bash`, file descriptors are used to control input and output from a shell script. By default, every process has at least three file descriptors open (file descriptors are in `/dev/fd` directory):

- `0` - **standard input** (stdin)
- `1` - **standard output** (stdout)
- `2` - **standard error** (stderr)

Here is an example command that uses these file descriptors to show a dialog box and return the entered name:

```bash
$ name=$(whiptail --inputbox "Enter name" 8 32 --title "Name query" 3>&1 1>&2 2>&3)
```

Notation `>&` is used to redirect one file descriptor to another. `3>&1 1>&2 2>&3` manipulates (swaps **standard output** and **standard error**) file descriptors.

- `3>&1`: Creates a new (temporary) file descriptor, `3`, and makes it a duplicate of the **standard output** (`1`).
- `1>&2`: Redirects the **standard output** (`1`) to the **standard error** (`2`). After this redirection, anything that would normally go to stdout now goes to stderr.
- `2>&3`: Redirects the **standard error** (`2`) to file descriptor `3`. `3` was pointed to `1` in the first step, so now, `1` and `2` are swapped.

This swapping is performed since `whiptail` outputs the entered input to the **standard error** (`2`), not **standard output** (`1`).
Without the redirections, `name` would be empty, because all the actual output would go to stderr and would not be captured by `$()`. 

## Standard redirections
[Back to Top](#contents)

- **Standard Output Redirection (`>` and `>>`)**:
   Redirects the output of a command to a file. Using `>` will overwrite the file if it exists, while `>>` will append to it.
   ```bash
   $ echo "Section 1" > text.txt
   $ echo "Section 2" >> text.txt
   $ echo "Section 3" >> text.txt
   ```

- **Standard Input Redirection (`<`)**:
   Takes the content of a file and uses it as the input to a command.
   ```bash
   $ grep "Section" < text.txt
   ```

- **Standard Error Redirection (`2>` and `2>>`)**:
   Redirects the error messages output by a command to a file.
   ```bash
   $ ls file01.txt 2> error.txt 
   $ ls file02.txt 2>> error.txt 
   ```

- **Combining Output and Error Redirection (`&>`, `&>>`)**:
   Redirects both standard output and standard error to the same file.
   ```bash
   $ ls text.txt file01.txt file02.txt &> error.txt
   ```

## Process substitution
[Back to Top](#contents)

Process substitution enables the output of a process (or processes) to appear as a temporary file at a unique filename (often in `/dev/fd` on modern systems). This allows tools that can only read from files or write to files to interact with the output or input of another process.

**Input Process Substitution (`<()`)** 

This form is used when you want the output of a command to be read like a file by another command.
When you use `<()`, the shell replaces that expression with the path to a file that provides the output of the command inside the `()` as if it were a file.
For example, compare the contents of two directories using `diff`:

```bash
$ mkdir -p dir1/file{1..4}
$ mkdir -p dir2/file{3..6}
$ diff dir1 dir2
Only in dir1: file1
Only in dir1: file2
Common subdirectories: dir1/file3 and dir2/file3
Common subdirectories: dir1/file4 and dir2/file4
Only in dir2: file5
Only in dir2: file6
$ diff --side-by-side <(ls dir1) <(ls dir2)
file1							      <
file2							      <
file3								file3
file4								file4
							      >	file5
							      >	file6
```

Here, `ls dir1` and `ls dir2` commands are each run in their own subshell, with their outputs sent to named pipes. These pipes are passed to `diff`, so it can compare the directory listings as if they were files.

**Output Process Substitution (`>()`)** 

Treat the output of a command as if it were a file.

```bash
$ echo "Hello, ${USER}!" > >(grep "Hello")
Hello, nstu!
```
Here the output of `echo "Hello, ${USER}!"` is redirected not to the standard output but into the input of another command specified within `>(...)`. The above is equivalent to:

```bash
$ echo "Hello, ${USER}!" | grep "Hello"
Hello, nstu!
```

Here is another example of output process substitution:

```bash
$ seq 1 10 | tee >(grep -E "^[0-9]*[02468]$" > even.txt) >(grep -E "^[0-9]*[13579]$" > odd.txt) > /dev/null
$ cat {even,odd}.txt
2
4
6
8
10
1
3
5
7
9
```

**When to Use Process Substitution**

Use process substitution when you need to:

- Use multiple commands' outputs as files for comparison, merging, or other file-based operations without creating temporary files.
- Feed the output of a sequence of piped commands into the input of another command that expects a file.
- Work with commands that do not accept standard input/output redirections.

It is most useful when working with commands that expect file names as arguments and you want to use the output of another command instead.

**Limitations**

- Not all shells support process substitution (e.g., `dash` and some instances of `sh` do not).
- Process substitution may not work as expected when used in environments where `/dev/fd` is not properly implemented, like in some older Unix systems or restricted environments.
- Since process substitution creates a subshell, any changes to variables within that subshell will not be reflected in the parent shell.

Process substitution is one of those advanced features in `bash` that can significantly streamline complex shell scripting tasks and is a testament to the flexibility of the shell environment.

Process substitution is often categorized with redirection because it involves directing the input or output of a command to or from a process rather than a file. However, it's a distinct feature that uses named pipes or temporary files in the background to allow processes to communicate.

Process substitution is like a more advanced form of redirection, integrating the concept of inter-process communication. While standard redirection deals primarily with static files, process substitution is dynamic, allowing for real-time data exchange between processes as if they were files. This can be particularly powerful in shell scripting for creating efficient data processing workflows that would otherwise require more complex and potentially less efficient methods.

## Here documents and here strings
[Back to Top](#contents)

**Here Document (`<<`)**:
   Allows the creation of a multiline string from the command line and redirects it as an input (file) to a command.

   ```bash
   $ cat <<EOF
   > The quick brown fox
   > jumps over the lazy dog
   > EOF
   The quick brown fox
   jumps over the lazy dog
   ```

Other string can be used:

   ```bash
   $ cat <<STRING
   > The quick brown fox
   > jumps over the lazy dog
   > STRING
   The quick brown fox
   jumps over the lazy dog
   ```

Quotations can be used not to allow variable substitution:

   ```bash
   $ animal=fox
   $ cat <<'EOF'
   > The quick brown ${animal}
   > jumps over the lazy dog
   > EOF
   The quick brown ${animal}
   jumps over the lazy dog
   ```

Can also use to output to a file:

   ```bash
   $ animal=fox
   $ cat <<'EOF'>>file.txt
   > The quick brown ${animal}
   > jumps over the lazy dog
   > EOF
   The quick brown ${animal}
   jumps over the lazy dog
   $ cat file.txt 
   The quick brown ${animal}
   jumps over the lazy dog
   ```

**Here String (`<<<`)**:
   A variant of here documents, which allows a single line of input to be redirected to a command.
   ```bash
   $ grep "fox" <<< "The quick brown fox jumps over the lazy dog"
   ```
   Here, `grep` expects a file name and without `<<<` we would have an error:
   ```bash
   $ grep "fox" "The quick brown fox jumps over the lazy dog"
   grep: The quick brown fox jumps over the lazy dog: No such file or directory
   ```
   Alternative option would be to `echo` into `grep`:
   ```bash
   $ echo "The quick brown fox jumps over the lazy dog" | grep 'fox'
   The quick brown fox jumps over the lazy dog
   ```

## Advanced redirections
[Back to Top](#contents)

**Copying File Descriptors (`>&`, `<&`)**:
   
   Duplicates one file descriptor, making it copy the output or input of another.

   ```bash
   $ exec 3>&1   # Duplicates stdout to fd 3
   $ command >&3 # Redirects output of command to fd 3 (stdout)
   ```

**Moving File Descriptors (`>&-`, `<&-`)**:

   Closes the specified file descriptor.

   ```bash
   $ exec 3>&1 # Duplicates stdout to fd 3
   $ exec 3>&- # Closes fd 3
   ```

**Redirection with exec**:

   Redirects input or output globally for the shell or script. This affects all subsequent commands.

   ```bash
   $ exec > outputfile # All subsequent commands' stdout will go to outputfile
   $ exec 2> errorfile # All subsequent commands' stderr will goto errorfile
   ```

<!-- SECTION -->
# Script files
[Back to Top](#contents)

## Layout
[Back to Top](#contents)

Scripts are files that contain a combination of one or several commands. A powerful feature of `bash` is the ability to use system commands directly, without the need for a wrapper, as is required in other languages like `Python`. The first line in a script is used to indicate the interpreter for the script, such as `bash`. The special symbol `#!`, known as **shebang**, precedes the full path to the interpreter, for example, `#!/bin/bash` (usage of the full path is not required, but it is a good practice or use `#!/usr/bin/env bash`). The hash symbol `#` on subsequent lines denotes a comment. It is common practice to define variables and functions before the main body of the script. While not required, using the `.sh` file extension is considered good practice, as it indicates that the file is a script. The typical script file layout is shown below:

```bash
#!/bin/bash

# usage information
# ./script -opt_1 -opt_2 ... arg_1 arg_2 ...
# opt_i - ...
# arg_i - ...

# customize shell
set -e

# define variables and process input arguments

name="$1"

if [ -z "$name" ]; then
   name="${USER}@${HOSTNAME}"
fi

# define functions

function hello() {
   echo
   echo "hello from ${SHELL}, ${1}!"
   return 0
}

function goodbye() {
   echo
   echo "goodbye!"
   return 0
}

# execute script (body)

hello "${name}"

# clean up (unset variables)
unset name

# optional 'exception handling'
trap goodbye EXIT

# exit (can also exit with different codes)
exit 0
```

Note, the `trap` command in `bash` is used to catch signals and other system events and then execute a command or a list of commands when one of these events occurs. 

## Execution
[Back to Top](#contents)

The above script can be executed (here commands are processed sequentially) even without creating a file which might be useful in some situations:

```bash
$ bash << 'EOF'
#!/bin/bash

# customize shell
set -e

# define variables and process input arguments
name="$1"
if [ -z "$name" ]; then
   name="${USER}@${HOSTNAME}"
fi

# define functions
function hello() {
   echo
   echo "hello from ${SHELL}, ${1}!"
   return 0
}
function goodbye() {
   echo
   echo "goodbye!"
   return 0
}

# execute script
hello "${name}"

# optional exception handling
trap goodbye EXIT

# exit (can also exit with different codes)
exit 0
EOF

hello from /bin/bash, nstu@nstu-course!

goodbye!

```

Note, here a special form of input stream (here-document) is used to is passed into `bash` command. All text between `<<'EOF' ... EOF` is considered as a file content. The first `EOF` is in single quotes to avoid substitutions (compare the result of with and without quotes). Different streams and redirections are explored in more details in [Redirections](#redirections) section.

Normally scripts are used for automation and are not intended to be used only one time as above. In this case the script is more convenient to store in a file with conventional `.sh` extension. Create a `script.sh` file.

```bash
$ cat > script.sh << 'EOF'
#!/bin/bash

# customize shell
set -e

# define variables and process input arguments
name="$1"
if [ -z "$name" ]; then
   name="${USER}@${HOSTNAME}"
fi

# define functions
function hello() {
   echo
   echo "hello from ${SHELL}, ${1}!"
   return 0
}
function goodbye() {
   echo
   echo "goodbye!"
   return 0
}

# execute script
hello "${name}"

# optional exception handling
trap goodbye EXIT

# exit (can also exit with different codes)
exit 0
EOF
```

Now `bash` command can be used to execute the script file:

```bash
$ bash script.sh
hello from /bin/bash, nstu@nstu-course!

goodbye!

```
A more convenient and preferred method is to grant execute permissions to the script file and then run it directly from the command line:

```bash
$ chmod u+x script.sh
$ ./script.sh
hello from /bin/bash, nstu@nstu-course!


goodbye!
```

For debugging it might be useful to use `set` command with `-x` flag (see `man set` for details). `shellcheck` command can be used to (statically) check script files **before execution**. Already mentioned `trap` command can be used to catch different signals (see `trap -l` for details).

```bash
$ shellcheck script.sh
```

In the above scriprs were **executed**, variables and functions defined in them do not persist after the execution in complete. What if we actually want to make them persistent? In this case we **source** such scripts instead!

- **Execute** (`./script.sh` or `bash script.sh`)
   - Runs the script in a new subshell (child process).
   - Any variables and functions defined in the script do not persist after execution.

- **Source** (`source script.sh` or `. script.sh`):
   - Runs the script in the current shell (no new process).
   - Variables and functions defined in the script remain available after execution.

## Best practices
[Back to Top](#contents)

Large and complex scripts in `bash` might be hard to follow. Below are some things to consider when writing scripts:

- **Complexity**: If the script is becoming complex, especially with many loops, conditionals, and function calls, more advanced scripting language syntax and language features may make the script easier to write and maintain.

- **Portability**: `bash` scripts are great for Unix-like environments, but they can be less portable to systems like Windows without additional software. Consider using cross-platform scripting tools that can be run unchanged across different operating systems.

- **Functionality**: `bash` has a limited range of built-in functions, and while you can call external programs and utilities, doing so can be less efficient and more complex than using a language with a rich standard library.

- **Error Handling**: Error handling is not particularly robust. Consider using a different scripting tool if advanced error handling is desired.

- **Performance**: While `bash` can be suitable for simple tasks, other tools may perform better with CPU-intensive tasks due to its ability to use pre-compiled code and optimized libraries.

- **Readability and Maintenance**: Some scripting tools are often easier to read and maintain, especially for those who are not familiar with advanced `bash` syntax.

- **Community and Libraries**: A scripting tool can have a large community and a wealth of libraries for nearly every task imaginable, from web development to data analysis. If your `bash` script is starting to require more external tools or complex data processing it might be a signal to use a different tool.

- **User Interaction**: If your script requires complex user interaction (advanced CLIs or GUIs) it might be a signal to use a different tool.

- **String Manipulation and Data Processing**: While `bash` can handle simple string manipulation and data processing, other tools might have more powerful string methods and data structures.

In general, if your script is moving beyond file manipulation, simple task automation, and environment setup, and it starts to involve more complex data types, structures, and logic flows, you should consider another higher-level scripting language.

For smaller scripts or when working within a system that is highly dependent on shell environments or for simple file and system operations, `bash` may still be the preferable choice. In practice, it's also common to see hybrid solutions where `bash` scripts call other programs for more complex tasks. For instance, you can leverage `Python` for complex math operations within a `bash` script:

```bash
$ function calculator () {
>    python -c "from math import *; print($1)"
> }
$ calculator "sqrt(4.0)"
2.0
$ echo $((2.0 + $(calculator "sqrt(4.0)")))
4.0
```

Make sure to add comments where it makes sense (describe what your script is for, comment complex sections). This will improve script readability and maintenance. You also should test scripts in different environments with different input to ensure they work as expected.

`bash` scripts also allow different configuration and customization options:

- **Shell Options**: Use the `set` command to change shell attributes and options.

- **Environment Variables**: Use environment variables to modify the behavior of your script without changing the code, e.g. set an environmental variable (see [Variables](#variables) section) to a different value prio to script execution.

- **Configuration Files**: Source external configuration files that define variables and functions.

- **Command Line Arguments**: Passing different command line arguments to your script can change its behavior. You can parse options and arguments using `getopts` or manually iterating over `$@`.

- **Aliases and Functions**: Define aliases and functions to simplify complex commands or to add shortcuts for common operations.

- **Interactive Prompts**: Use `read` or tools like `dialog` or `whiptail` to create interactive scripts that ask for user input.

<!-- SECTION -->
# Pathname expansion

<!-- SUBSECTION -->
## Brace expansion
[Back to Top](#contents)

Modern shells support the mechanism of brace expansion. Several types of brace expansion are available. `bash` brace expansions are automatically expanded before any other kind of expression. Brace expansions allows to generate different file names or sequences of strings. One or several expressions can be used together and even nested.

Brace expansion expression with numbers has the following form:

```bash
$ {START..END..[INCREMENT]}
```

with `START` beginning the start number of the sequence, `END` being the end number of the sequence and an optional `INCREMENT` with default value of `1` if omitted. For numbers, brace expansion allows you to create a range of values that can be used for iteration or to generate file names. One or more such expressions can be used.

Generate sequence of numbers from 0 to 100 with a step of 5:

```bash
$ echo {0..100..5}
0 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100
```

When generating a reverse sequence by setting a `START` value greater than `END`, the sequence descends. If `INCREMENT` is omitted, it defaults to `-1`, creating a decrementing sequence:

You can also generate a sequence in reverse order by making the `START` larger than the `END` (`INCREMENT` should be positive):

```bash
$ echo {100..0..5}
100 95 90 85 80 75 70 65 60 55 50 45 40 35 30 25 20 15 10 5 0
```

Generate a sequence with numbers padded with zeroes to ensure a fixed string length (why this might be useful?):

```bash
$ echo {000..100..5}
000 005 010 015 020 025 030 035 040 045 050 055 060 065 070 075 080 085 090 095 100
```

Generate file names using brace expansion with numbers:

```bash
$ touch file_{1..5}
$ ls file_*
file_1  file_2  file_3  file_4  file_5
$ rm file_{1..5}
```

Sequences of alphabetic characters can be generated in the following way:

```bash
$ echo {a..z}
a b c d e f g h i j k l m n o p q r s t u v w x y z
```

Similarly, for uppercase letters:

```bash
$ echo {A..Z}
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
```

And for reverse order:

```bash
$ echo {z..a}
z y x w v u t s r q p o n m l k j i h g f e d c b a
```

Unlike expansion with numbers, `INCREMENT` is not available for letters.

Several comma separated items inside braces are also expanded:

```bash
$ echo {a,b,c,d,e}
a b c d e
```

All these kinds of expansions can be combined. Note, no spaces should be used in brace expansion. For example, one can generate different file names:

```bash
$ touch {vector,matrix}_{a..b}_{1..2}
$ ls vector_?_?
vector_a_1  vector_a_2  vector_b_1  vector_b_2
$ ls matrix_?_?
matrix_a_1  matrix_a_2  matrix_b_1  matrix_b_2
$ rm {vector,matrix}_{a..b}_{1..2}
```

The following nesting also works:

```bash
$ echo {{a..z},{0..9}}
a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9
```

Create nested directories:

```bash
$ mkdir -p project/{src,bin,doc} && cd project && tree
.
├── bin
├── doc
└── src
$ cd .. && rm -r project
```

Create a backup file:

```bash
$ touch file
$ cp file{,_backup}
$ ls file{,_backup}
file  file_backup
$ rm file{,_backup}
```

Copy or move several files to a directory:
```bash
$ mkdir test
$ touch file_{1..5}
$ mv file_{1..5} test
$ ls test
file_1  file_2  file_3  file_4  file_5
$ rm -r test
```

Rename a file:

```bash
$ touch file
$ mv {,old_}file
$ ls old_file
$ rm old_file
```

Brace expansion can significantly reduce the time and effort required to generate multiple items or iterate over sequences.

<!-- SUBSECTION -->
## Wildcards
[Back to Top](#contents)

Another powerful feature of shell scripting is pattern matching with wildcards, which are symbols that represent one or more characters in file names or text. The shell interprets these wildcards to expand file names or filter text. The most commonly used wildcards are `*`, `?`, and `[]`.

The `*` wildcard represents zero or more characters, allowing it to match any string of characters:

```bash
$ touch file_{a..b}_{1..2}.txt
$ ls file*.txt
file_a_1.txt  file_a_2.txt  file_b_1.txt  file_b_2.txt
$ rm file_{a..b}_{1..2}.txt
```

The `?` wildcard is used to represent a single character, meaning it matches any filename with any character in that specific position:

```bash
$ touch file_{a..b}_{1..2}.txt
$ ls file_?_?.txt
file_a_1.txt  file_a_2.txt  file_b_1.txt  file_b_2.txt
$ rm file_{a..b}_{1..2}.txt
```

The `[]` wildcard matches one of any characters enclosed within the brackets. A range of characters can be specified using the `-` symbol:

```bash
$ touch file_{a..b}_{1..2}.txt
$ ls file_[ab]_[12].txt
file_a_1.txt  file_a_2.txt  file_b_1.txt  file_b_2.txt
$ ls file_[a-b]_[1-2].txt
file_a_1.txt  file_a_2.txt  file_b_1.txt  file_b_2.txt
$ rm file_{a..b}_{1..2}.txt
```

To create a pattern that excludes specific characters, place a `!` or `^` symbol at the beginning of the character list inside the brackets:

```bash
$ touch file_{a..b}_{1..2}.txt
$ ls file_[^a]_[^1].txt
file_b_2.txt
$ rm file_{a..b}_{1..2}.txt
```

<!-- SUBSECTION -->
## Globbing
[Back to Top](#contents)

Globbing is a way to specify patterns matching to groups of filenames. Brace expansion and wildcards can be used for globbing. The matching process has the following steps:

- **Wildcard Expansion**: In `bash`, wildcard patterns are expanded to match filenames, and brace expansions occur before command execution. This process ensures that commands receive actual filenames, not the original patterns or braces.

- **No Matches**: When a glob pattern finds no matching filenames in `bash`, it remains as is. However, enabling the `nullglob` option (see `shopt`) removes unmatched patterns, resulting in a null string. Conversely, with `failglob` enabled, unmatched patterns cause the command to fail.

```bash
$ # set option
$ shopt -s nullglob
$ # unset option
$ shopt -u nullglob
```

- **Dot Files**: Dot files (those beginning with `.`) are not matched by the `*` or `?` wildcards unless the pattern explicitly includes the dot.

- **Non-Recursive**: Glob patterns, by default, do not extend their search to subdirectories.

```bash
$ shopt -s failglob
$ mkdir test
$ touch test/file_{01..10}.txt
$ ls *txt
-bash: no match: *txt
$ ls */*txt
test/file_01.txt  test/file_03.txt  test/file_05.txt  test/file_07.txt  test/file_09.txt
test/file_02.txt  test/file_04.txt  test/file_06.txt  test/file_08.txt  test/file_10.txt
$ shopt -u failglob
```

- **Case Sensitivity**: Matching patterns are case-sensitive by default. This behavior can be changed by setting the `nocaseglob` shell option.

- **Extended Globbing**: `bash` supports extended globbing, which allows more complex patterns with operators like `?(pattern)`, `*(pattern)`, `+(pattern)`, `@(pattern)`, and `!(pattern)` if the `extglob` shell option is enabled (`shopt -s extglob`).


<!-- SECTION -->
# Variables
[Back to Top](#contents)

Variables can be set within the command line or inside the script file using the following syntax:

```bash
$ # No spaces around equal sign
$ name=value
```

Here the variable `name` is set to `value`. There should be no spaces around the `=` sign. If the `value` contains spaces, single or double quotes should be used depending on the context.

The value of a variable can be referenced with `$` sign:

```bash
$ echo $name
value
```

The value of a variable is substituted inside expressions surrounded by `"` quotes:

```bash
$ echo "$name"
value
```

Or using the full form of parameter expansion:

```bash
$ echo "${name}"
value
```

In math expressions `$` can be ommitted, since the meaning is clear from the context.

```bash
$ x=1
$ y=1
$ echo $(( x + y ))
2
```

All these methods are valid for basic tasks, but full parameter expansion syntax if often prefered since it is the savest one and allows additional proccesing (see bellow). Note, referencing an undefined variable returns an empty string.

The term **variable** is used here to refer to a `name` in the expresson of the form `name=value` instead of calling is a **parameter** which is a more general term that also includes special characters (like `?` for the **exit code**) and positional parameters of functions and scripts.

Variable values are not substituted into expressions surrounded by single quotes, such expressions are literal.

```bash
$ name="value"
$ echo "${name}"
value
$ echo '${name}'
${name}
```

There are important differences between using double quotes (`"`) and single quotes (`'`):

- **Double Quotes (`"`)**: using `"` allows for parameter substitution (also for brace expansion, command substitution and arithmetic expansion) to take place. If `name="value"`, then `echo "name is $name"` will result in `name is value`. Double quotes prevent word splitting and pathname expansion, so they are safer to use when your variable might contain spaces or special characters. For example, a variable `name=*` when used without quotes will be expanded, which might not be desired. 

- **Single Quotes (`'`)**: Enclosing a variable in single quotes will treat everything inside as a literal string, so no variable expansion or command substitution will occur. If `name="value"`, then `echo 'name is $name'` will result in `name is $name`.

When referencing a variable, consider the following:

- **Use quotes**: To avoid issues with word splitting and globbing, it's recommended to quote variables. `"${name}"` is a safe way to ensure that the value of `name` is treated as a single word, even if it contains spaces or special characters.

- **Use braces**: For concatenating variables with strings or using variable names next to characters that could be part of the name, use braces to clearly delimit the variable name, like `"${name}_suffix"` or `"prefix_${name}"`.

Referencing variables without quotes can lead to unexpected behaviors and issues:

- **Splitting**: If a variable containing spaces used in a context where word splitting occurs, such as in a loop or when passed as an argument to a command, each part would be treated as a separate word if it is referenced without quotes.

- **Globbing**: Unquoted variables undergo globbing, where patterns like `*`, `?`, and `[]` are expanded to matching filenames.

- **Unintended Execution**: If a variable contains characters that are interpreted by the shell, like `;`, `&`, `|`, `$(...)`, `>` etc., it could lead to execution of unexpected commands or overwriting files.

- **Argument Count**: When passing arguments to functions or scripts, unquoted variables can change the count of arguments due to word splitting.

- **Unpredictable Loop Iterations**: When looping over a variable's contents, unquoted references can split items incorrectly, creating more loop iterations than intended.

```bash
$ animals="cat dog"
$ for animal in "${animals}"; do echo $animal; done
cat dog
$ for animal in $animals; do echo $animal; done
cat
dog
```

- **Conditional Expression Errors**: In conditional expressions, unquoted variables can lead to syntax errors or unintended results if they contain spaces or are empty.

<!-- SUBSECTION -->
## Customization
[Back to Top](#contents)

Customization of variables behaviour is possible with `local` keyword, that is used only inside **functions** to limit the scope of a variable to that function. This means the variable will not be accessible or interfere with variables outside the function or in the global scope:

```bash
$ function foo() {
>  local local_var="local"
>  global_var="global"
> }
$ foo
$ echo $local_var

$ echo $global_var
"global"
```

If `global_var` was defined before the function call, it's value will be overwritten.

`declare` built-in command (not limited to functions) can be used to declare variables and give them attributes or to modify the properties of variables that have already been defined (see `help declare`):

- **Declaring an Integer Variable**:

   ```bash
   $ declare -i n
   $ n="2 + 2"
   $ echo $n
   4
   $ unset n
   $ n="2 + 2"
   $ echo $n
   "2 + 2"
   ```

- **Creating an Array**: Explicitly declare variable to be an array (not required)

   ```bash
   $ unset x
   $ declare -a x
   $ x=(1 2 3 4 5)
   $ echo "${x}"
   1
   $ echo "${x[@]}"
   1 2 3 4 5
   $ echo "${#x[@]}"
   5
   $ echo "${x[1]}"
   2
   ```

- **Creating an Associative Array (similar to dictionary in Python)**:

   ```bash
   $ unset x
   $ declare -A x
   $ x['A']=0
   $ x['B']=1
   $ echo "${x}"

   $ echo "${x[@]}"
   1 0
   $ echo "${x['A']}"
   0
   $ echo "${x['B']}"
   1
   ```

- **Setting Variables to Read-only**:

   ```bash
   $ unset x
   $ declare -r x=1
   $ x=0
   bash: x: readonly variable
   $ echo $x
   1
   ```

- **Listing All Declared Variables**:

   ```bash
   $ declare -p
   ```

The `declare` command is particularly useful in scripts that require strict typing of variables or to ensure certain attributes are applied to your variables to prevent errors in script's logic.

There are several other commands that can be used to modify variables and their attributes:

- **`set`**: It's a built-in shell command used to set and unset shell options and positional parameters. It can also display the names and values of shell variables when used without options.

- **`export`**: This command is used to make a shell variable available to child processes of the current shell session. Variables that are exported can be accessed by subsequent programs that the shell executes.

   ```bash
   $ export name="value"
   ```
   ```bash
   $ x=1
   $ bash << 'EOF'
   echo $x
   EOF

   $ export x=1
   $ bash << 'EOF'
   echo $x
   EOF
   1
   ```

- **`readonly`**: This command is used to make variables or functions read-only. Once a variable is set as readonly, its value cannot be changed.

   ```bash
   $ readonly name="value"
   ```

<!-- SUBSECTION -->
## Parameter substitution
[Back to Top](#contents)

As already mentioned variable value can be referenced with `$`, more generic parameter substitution can be used to provide a range of functionalities (string manipulation, default value assignment). Here's a list of some of these forms:

- **Substring Expansion**: `${parameter:offset:length}`
   
   Extracts a substring from `$parameter` starting at `offset` and up to `length` characters.
   
   ```bash
   $ unset name
   $ name="John Doe"
   $ echo "${name:0:4}"
   John
   $ echo "${name:5:3}"
   Doe
   ```

- **Default Value**: `${parameter:-default}`
   
   If `parameter` is unset or null, the expansion of `default` is substituted. Otherwise, the value of `parameter` is used.

   ```bash
   $ unset name
   $ echo "${name:-John Doe}"
   John Doe
   $ echo "${name}"

   ```

- **Assign Default Value**: `${parameter:=default}`
   
   If `parameter` is unset or null, `default` is assigned to `parameter`.

   ```bash
   $ unset name
   $ echo "${name:=John Doe}"
   John Doe
   $ echo "${name}"
   John Doe
   ```

- **Error if Null or Unset**: `${parameter:?error_message}`
   
   If `parameter` is null or unset, `error_message` is displayed as an error message, and the script can be terminated.
 
   ```bash
   $ unset name
   $ echo "${name:?'name is not set'}"
   bash: name: name is not set
   ```

- **Use Alternative Value**: `${parameter:+alternative_value}`

   If `parameter` is set and not null, `alternative_value` is substituted; otherwise, nothing is substituted.

   ```bash
   $ name="John"
   $ echo "${name:+John Doe}"
   John Doe
   ```

- **Remove Smallest Prefix Pattern**: `${parameter#pattern}`

   Removes the shortest match of `pattern` from the beginning of `$parameter`.

   ```bash
   $ file="/usr/local/bin/script.sh"
   $ echo "${file#*/}"
   usr/local/bin/script.sh
   ```

- **Remove Largest Prefix Pattern**: `${parameter##pattern}`

   Removes the longest match of `pattern` from the beginning of `$parameter`.

   ```bash
   $ file="/usr/local/bin/script.sh"
   $ echo "${filepath##*/}"
   script.sh
   ```

- **Remove Smallest Suffix Pattern**: `${parameter%pattern}`

   Removes the shortest match of `pattern` from the end of `$parameter`.

   ```bash
   $ file="report.pdf"
   $ echo "${file%.pdf}"
   report
   ```

- **Remove Largest Suffix Pattern**: `${parameter%%pattern}`
   
   Removes the longest match of `pattern` from the end of `$parameter`.

   ```bash
   $ file="backup.tar.gz"
   $ echo "${file%%.*}"
   backup
   ```

- **Case Modification (Uppercase)**: `${parameter^^}`

   Converts all letters in `parameter` to uppercase.

   ```bash
   $ name="John Doe"
   $ echo "${name^^}"
   JOHN DOE
   ```

- **Case Modification (Lowercase)**: `${parameter,,}`
    
   Converts all letters in `parameter` to lowercase.

   ```bash
   $ name="John Doe"
   $ echo "${name,,}"
   john doe
   ```

<!-- SUBSECTION -->
## Environment variables
[Back to Top](#contents)

Environment variables in `bash` are a way to store values that can affect the way running processes will behave on a computer (processes might look for specific environment variables). They are used to communicate configuration information to applications and scripts — such as the location of libraries, system preferences, session information, and so on.

For instance, the `PATH` environment variable stores a list of directory paths. When you type a command into the shell, it looks through the directories listed in your `PATH` environment variable to find the executable.

In `bash`, you can set an environment variable for the current session using the export command:
```bash
$ export NAME="VALUE"
```
This will make `NAME` (common paractice is to use uppercase names) available to all child processes initiated from that session (including subshells).

You can view a list of all environment variables by running the `env` command, or you can echo a specific variable using `echo`:
```bash
$ echo $NAME
VALUE
$ env | grep NAME
NAME=VALUE
```
- Do not to store sensitive data likepasswords or API keys in your environment variables if your scripts or processes are shared or stored in insecure places
- Use expressive names for your environment variables (prefix with application name `APP_NAME`)
- Consider using local variables instead of global ones
- Do not overwrite system variables (`PATH`, `HOME`, `SHELL`)
- Set commonly used environment variables in `.bashrc` file (executed at session startup)
- Unset variables if not needed

<!-- SUBSECTION -->
## Special characters and variables
[Back to Top](#contents)

The following table contains `bash` special characters:

| Special Character | Description                                    |
|:------------------|:---------------------------------------------- |
| `$`               | Variable substitution                          |
| `#`               | Comment                                        |
| `&`               | Background job                                 |
| `*`               | Matches any string in filename expansion       |
| `?`               | Matches any single character in filename expansion |
| `;`               | Command separator                              |
| `\|`               | Pipe, command chaining                         |
| `>`               | Redirect output                                |
| `<`               | Redirect input                                 |
| `()`              | Command grouping(subshell)                   |
| `{}`              | Command grouping                                   |
| `[]`              | Character classes in filename expansion        |
| `` ` ` ``           | Command substitution (deprecated, use `$()` instead) |
| `"`               | Partial quote (allows variable expansion)                                  |
| `'`               | Full quote (literal string)                                     |
| `~`               | Home directory                                 |
| `!`               | History substitution                           |
| `\`               | Escape character                               |

The following table contains `bash` special variables:

| Special Variable | Description                                        |
|:-----------------|:---------------------------------------------------|
| `$#`             | Number of command-line arguments                   |
| `$-`             | Shell session options currently in effect                        |
| `$?`             | Exit value of last executed command                |
| `$$`             | Process number of current process                  |
| `$!`             | Process number of last background command          |
| `$0`             | Script command name                        |
| `$n`             | Positional arguments (`n` represents the argument number) |
| `$*` or `$@`     | All arguments on command line (`$1 $2 ...`)       |
| `"$*"`           | All positional parameters as a single word (`"$1 $2 ..."`)|  
| `"$@"`           | All positional parameters as separate words (`"$1" "$2" ...`) |
| `$_`             | Last argument of the previous command              |

<!-- SUBSECTION -->
## Arrays
[Back to Top](#contents)

Note, arrays are indexed starting from 0 in `bash` (from 1 in `zsh`).

- **Declare Arrays Explicitly**: Use `declare -a` to explicitly declare an array (or use `declare -A` to declare an associative array). Also, use descriptive names for arrays.

   ```bash
   $ declare -a array
   ```

- **Access Elements with Braces**: Always access elements with braces to avoid issues with spaces and to clearly delimit the array index.

   ```bash
   $ declare -a array
   $ array=("element 1" "element 2" "element 3")
   $ echo "${array[0]}"
   element 1
   ```

- **Quote Array Expansions**: When expanding an array to pass as arguments to a command, quote it to avoid issues with elements that contain spaces.

   ```bash
   $ for element in ${array[@]}; do   echo $element; done
   element
   1
   element
   2
   element
   3
   $ for element in "${array[@]}"; do   echo $element; done
   element 1
   element 2
   element 3
   $ for element in "${array[*]}"; do   echo $element; done
   element 1 element 2 element 3
   ```

- **Append Elements with `+=`**: When adding elements, use `+=` to append to the array without overwriting existing elements.

   ```bash
   $ array+=("element 4")
   $ echo "${array[@]}"
   element 1 element 2 element 3 element 4
   ```

- **Check Array Length with `${#array[@]}`**: To get the length of an array, use the syntax `${#array[@]}`.

- **Sparse Arrays Carefully**: `bash` arrays are sparse, indices can be undefined.

   ```bash
   $ array[100]=100
   $ echo "${array[@]}"
   element 1 element 2 element 3 element 4 100
   $ echo "${#array[@]}"
   5
   $ array+=(1)
   $ echo "${array[101]}"
   1
   $ unset array[101]
   $ echo "${array[101]}"

   ```

- **Local Arrays in Functions**: If you use arrays within functions and you want to avoid global side effects, declare them as local (use `local` with `declare` flags).

   ```bash
   $ function fn() {
   local -ir factor="${1}"
   local -ia array=(1 2 3 4)
   for i in "${array[@]}"; do
      echo $((factor * i))
   done
   return 0
   }
   $ fn 5
   5
   10
   15
   20
   ```

- **Passing Arrays to Functions**: Pass expanded array using `"${array[@]}"`.

   ```bash
   declare -a array
   array=(A B C)
   function fn() {
      local -a array=("$@")
      for i in "${array[@]}";
         do
            echo "$i"
         done
   }
   fn "${array[@]}"
   A
   B
   C
   ```

- **Array Slicing**: Use `"${array[@]:i:j}"` to slice an array.

   ```bash
   $ array=(1 2 3 4 5 6 7 8 9 10)
   $ slice=("${array[@]:0:5}")
   $ echo "${slice[@]}"
   1 2 3 4 5
   ```

   This will create a new array called `sliced_array` containing a slice of `my_array` from index 1 to 2.

- **Copy an Array**: Expand into a new array using `@` inside parentheses.

   ```bash
   $ array=(1 2 3 4 5 6 7 8 9 10)
   $ local=("${array[@]}")
   $ unset array
   $ echo "${local[@]}"
   ```

- **Concatenate Arrays**: 

   ```bash
   $ x=(0 1 2 3 4)
   $ y=(5 6 7 8 9)
   $ z=("${x[@]}" "${y[@]}")
   $ echo "${z[@]}"
   0 1 2 3 4 5 6 7 8 9
   ```

<!-- SECTION -->
# Math operations
[Back to Top](#contents)

In `bash`, `(( ))` is used to perform arithmetic operations. Within `(( ))`, variables can be referenced without the `$` prefix and perform arithmetic operations just like in other programming languages (variables used within `(( ))` are expected to numbers in this case).

Note, you do not need to put spaces after `((` or before `))` in math ops.

```bash
$ # Perform math and set the result to
$ ((result = 1 + 2))
$ echo "1 + 2 = ${result}"
1 + 2 = 3

$ # Reference variables in math
$ a=2
$ b=3
$ ((result = a * b))
$ echo "${a} * ${b} = ${result}"
2 * 3 = 6

$ # Increment
$ a=0
$ (( a++ ))
$ echo "$a"
1

$ # Condition
$ a=1
$ b=0
$ if (( a > b )) ; then
>   echo "${a} > ${b}"
> fi
1 > 0
```

Exit code of math comparison:

```bash
# FALSE corresponds to 1 exit code
$ ((0 > 1))
$ echo $?
1
```

```bash
# TRUE corresponds to 0 exit code
$ ((0 < 1))
$ echo $?
0
```

Other common math operations: subtraction (`-`), division (`/`), modulus (`%`), exponentiation (`**`), and other. It's important to note that `bash` only supports integer arithmetic in `(( ))`, so if you perform division, it will only return the integer part of the result. Use `bc` or `python` for floating point arithmetic.

```bash
$ echo "sqrt(4.0)" | bc -l
2.00000000000000000000
```

Note, `(expr ...)` is a deprecated form (also need to escape special characters) of `(())`:

```bash
$ a=2
$ b=5
$ echo $((a*b))
10
$ # Since * is a special bash character (wildcard)
$ # It should be escaped with \
$ echo $(expr $a \* $b)
10
```

Undefined variables are evaluated to zero:

```bash
$ unset x
$ echo $(( x ))
0
```

<!-- SUBSECTION -->
## Operations
[Back to Top](#contents)

| Operators      | Description                                    |
|----------------|------------------------------------------------|
| ++x, x++       | Pre and post-increment                         |
| --x, x--       | Pre and post-decrement                         |
| +, -, *, /     | Addition, subtraction, multiplication, division|
| %, **          | Modulo (remainder) and exponentiation          |
| &&, \|\|, !      | Logical AND, OR, and negation                  |
| &, \|, ^, ~     | Bitwise AND, OR, XOR, and negation             |
| <=, <, >, =>   | Less than or equal to, less than, greater than, and greater than or equal to comparison operators|
| ==, !=         | Equality and inequality comparison operators   |
| =              | Assignment operator                            |

<!-- SUBSECTION -->
## Functions (bc)
[Back to Top](#contents)

| Function  | Description                                        |
|-----------|----------------------------------------------------|
| s(x)      | The sine of x, x is in radians                    |
| c(x)      | The cosine of x, x is in radians                  |
| a(x)      | The arctangent of x, arctangent returns radians   |
| l(x)      | The natural logarithm of x                         |
| e(x)      | The exponential function of raising e to the value x|
| j(n,x)    | The bessel function of integer order n of x        |
| sqrt(x)   | Square root of the number x. If the expression is negative, a run time error is generated|


<!-- SUBSECTION -->
## Examples
[Back to Top](#contents)

- **C-style for loop syntax**

   ```bash
   $ for ((i = 0; i < 10; i++)); do
   > echo $i
   > done
   0
   1
   2
   3
   4
   5
   6
   7
   8
   9
   ```

- **Nested logic and comparisons**
   ```bash
   $ a=5
   $ b=3
   $ c=4
   $ if (( (a > b) && (a == c) )); then
   >    echo 1
   > else
   >    echo 0
   > fi
   0
   ```

- **Bitwise operations**
 
   ```bash
   $ echo $(( (1 << 4) ))
   16
   echo $(( (16 >> 4) )
   1
   ```

- **Comma separation**
   ```bash
   $ (( a = 0, b = 1 ))
   $ echo $a
   0
   $ echo $b
   1
   ```

- **Ternary operator**
   
   ```bash
   $ (( a = 0, b = (a==0)?1:0 ))
   $ echo $a
   0
   $ echo $b
   1
   ```

- **Arithmetic expansion and assignment:**
   ```bash
   a=10
   (( a+=5, b=a*2 ))
   echo "a is $a, b is $b"
   ```

- **FizzBuzz**

   ```bash
   $ for ((i = 1; i <= 15; i++)); do
   >   x=""
   >   (( (i % 3) == 0 ))  && x+="FIZZ"
   >   (( (i % 5) == 0 ))  && x+="BUZZ"
   >   if [ -n "$x" ]; then
   >      echo $i $x
   >   fi
   > done
   3 FIZZ
   5 BUZZ
   6 FIZZ
   9 FIZZ
   10 BUZZ
   12 FIZZ
   15 FIZZBUZZ
   ```

<!-- SUBSECTION -->
## Exit status of math operations
[Back to Top](#contents)

Within `(( ))`, exit status rules are reversed for commands in that context compared to the normal shell context: an expression that evaluates to `0` (false in most programming languages) returns an exit status of `1` (failure in shell scripting), and a non-zero expression (true in most programming languages) returns an exit status of `0` (success in shell scripting). This can be particularly useful in conditional expressions.

```bash
$ ((0 == 1))
$ echo $?
1
$ ((0 == 0))
$ echo $?
0
```

<!-- SECTION -->
# Flow control
[Back to Top](#contents)

- In flow control (conditional execution), exit status is used to branch on the execution path
- Commands return an exit status of `0` (success) or other (failure)
- The exit code of a chain of commands is the exit code of the last command in the chain
- If a command is sent to the background, the exit code is its submission status
- In math expressions the exit code of true is `0` and the exit code of false is `1`.

<!-- SUBSECTION -->
## Test
[Back to Top](#contents)

| Syntax          | Description                                                                           |
|-----------------|---------------------------------------------------------------------------------------|
| \[ condition \] | Traditional test command (implicitly uses the `test` command)        |
| \[\[ condition \]\] | Updated test command (implicitly uses the `test` command)           |
| \(\(condition\)\) | Evaluate mathematical expression                                                     |
| \(command\)     | Run in subshell and use exit code. Subshell can be used to capture result, e.g., `echo $(cmd)` will echo the result of `cmd`. |
| command         | Execute command and use exit code                                                     |


- **Traditional test command (`[ condition ]`)**:
   
   ```bash
   $ function file_status() {
   >   local -r filename="${1}"
   >   if [ -f "${filename}" ]; then
   >      return 0
   >   else
   >      return 1
   >   fi
   > }
   $ rm -f test.txt
   $ file_status test.txt
   $ echo $?
   1
   $ touch test.txt
   $ file_status test.txt
   $ echo $?
   0
   ```

- **Updated test command (`[[ condition ]]`)**:

   ```bash
   $ function file_status() {
   >   local -r filename="${1}"
   >   if [[ -f "${filename}" ]]; then
   >      return 0
   >   else
   >      return 1
   >   fi
   > }
   $ rm -f test.txt
   $ file_status test.txt
   $ echo $?
   1
   $ touch test.txt
   $ file_status test.txt
   $ echo $?
   0

- **Mathematical expression evaluation (`((condition))`)**:

   ```bash
   $ ((1==1))
   $ echo $?
   0
   $ ((1==0))
   $ echo $?
   1
   ```

- **Run in subshell and use exit code (`(command)`)**:

   ```bash
   $ (sleep 1; echo "DONE")
   DONE
   $ echo $?
   0
   $ (sleep ; echo "DONE")
   sleep: missing operand
   Try 'sleep --help' for more information.
   DONE
   $ echo $?
   0
   $ (sleep && echo "DONE") 
   sleep: missing operand
   Try 'sleep --help' for more information.
   $ echo $?
   1
   $ (sleep 1; echo "DONE") &
   $ echo $?
   0
   DONE
   ```

- **Execute command and use exit code (`command`)**:

   ```bash
   $ ls > /dev/null
   $ echo $?
   0
   ```

- **String comparison**:

| Operator | Description                                      |
|----------|--------------------------------------------------|
| =        | Equals to (but for strings)                      |
| !=       | Not equal to (for strings)                       |
| <        | Less than (in ASCII alphabetical order)          |
| >        | Greater than (in ASCII alphabetical order)       |
| ==       | Double equals to (used to compare two strings)   |
| -z       | The String is null                               |
| -n       | The String is not null                           |


- **Test flags**:

| Operator | Description                                                                                |
|----------|--------------------------------------------------------------------------------------------|
| -e       | Check whether the file exists at a given path                                               |
| -f       | Check whether the given file path points to a regular file or not                           |
| -d       | Check whether the given path refers to an existing directory or not                         |
| -h       | Finds whether the given path is a symbolic link                                              |
| -L       | It checks for the symbolic link as the `-h` does, but it will also check whether it resolves to an actual file or directory|
| -b       | Checks for the block device                                                                 |
| -c       | Checks for the character special file                                                        |
| -p       | Checks for a named pipe (FIFO)                                                               |
| -s       | Used to find whether the file size is greater than zero or not                               |
| -t       | Check whether the file descriptor is associated with the terminal or not                     |
| -r       | Used to find whether the file is readable or not                                             |
| -w       | Checks for whether the file has write permissions or not                                     |
| -x       | It checks for the executable permissions for a specified file                                |
| -g       | Checks for "set-group-ID" (SGID) permission set on a specific file                           |
| -u       | Checks for "set-user-ID" (SUID) permission set on a specific file                            |
| -k       | Look for the "sticky" bit is set or not on a specified directory                             |
| -O       | Check whether the file exists and is owned by the current user                               |
| -G       | Check whether the file exists and is owned by the same group as the user running the script  |
| -N       | Helps you check if the file has been modified since it was last read                         |
| -nt      | Compares modification time of two files and determines which one is newer                    |
| -ot      | Compares modification time of two files and determines which one is older                    |
| -ef      | Check whether two file paths refer to the same inode on the system                           |
| !        | Reverses the result of a condition or command                                                |


<!-- SUBSECTION -->
## Exit codes
[back to top](#contents)

| Exit Code | Description                            |
|-----------|----------------------------------------|
| 0         | Success                                |
| 1         | Operation not permitted                |
| 2         | No such file or directory              |
| 3         | No such process                        |
| 4         | Interrupted system call                |
| 5         | Input/output error                     |
| 6         | No such device or address              |
| 7         | Argument list too long                 |
| 8         | Exec format error                      |
| 9         | Bad file descriptor                    |
| 10        | No child processes                     |
| 11        | Resource temporarily unavailable       |
| 12        | Cannot allocate memory                 |
| 13        | Permission denied                      |
| 14        | Bad address                            |
| 15        | Block device required                  |
| 16        | Device or resource busy                |
| 17        | File exists                            |
| 18        | Invalid cross-device link              |
| 19        | No such device                         |
| 20        | Not a directory                        |
| 21        | Is a directory                         |
| 22        | Invalid argument                       |
| 23        | Too many open files in system          |
| 24        | Too many open files                    |
| 25        | Inappropriate ioctl for device         |
| 26        | Text file busy                         |
| 27        | File too large                         |
| 28        | No space left on device                |
| 29        | Illegal seek                           |
| 30        | Read-only file system                  |
| 31        | Too many links                         |
| 32        | Broken pipe                            |
| 33        | Numerical argument out of domain       |
| 34        | Numerical result out of range          |
| 35        | Resource deadlock avoided              |
| 36        | File name too long                     |
| 37        | No locks available                    |
| 38        | Function not implemented              |
| 39        | Directory not empty                   |
| 40        | Too many levels of symbolic links      |
| 42        | No message of desired type             |
| 43        | Identifier removed                     |
| 44        | Channel number out of range            |
| 45        | Level 2 not synchronized               |
| 46        | Level 3 halted                         |
| 47        | Level 3 reset                          |
| 48        | Link number out of range               |
| 49        | Protocol driver not attached           |
| 50        | No CSI structure available             |
| 51        | Level 2 halted                           |
| 52        | Invalid exchange                         |
| 53        | Invalid request descriptor               |
| 54        | Exchange full                            |
| 55        | No anode                                 |
| 56        | Invalid request code                     |
| 57        | Invalid slot                             |
| 59        | Bad font file format                     |
| 60        | Device not a stream                      |
| 61        | No data available                        |
| 62        | Timer expired                            |
| 63        | Out of streams resources                 |
| 64        | Machine is not on the network            |
| 65        | Package not installed                    |
| 66        | Object is remote                         |
| 67        | Link has been severed                    |
| 68        | Advertise error                          |
| 69        | Srmount error                            |
| 70        | Communication error on send              |
| 71        | Protocol error                           |
| 72        | Multihop attempted                       |
| 73        | RFS specific error                       |
| 74        | Bad message                              |
| 75        | Value too large for defined data type    |
| 76        | Name not unique on network                         |
| 77        | File descriptor in bad state                       |
| 78        | Remote address changed                             |
| 79        | Can not access a needed shared library             |
| 80        | Accessing a corrupted shared library               |
| 81        | .lib section in a.out corrupted                    |
| 82        | Attempting to link in too many shared libraries    |
| 83        | Cannot exec a shared library directly              |
| 84        | Invalid or incomplete multibyte or wide character  |
| 85        | Interrupted system call should be restarted        |
| 86        | Streams pipe error                                 |
| 87        | Too many users                                     |
| 88        | Socket operation on non-socket                     |
| 89        | Destination address required                       |
| 90        | Message too long                                   |
| 91        | Protocol wrong type for socket                     |
| 92        | Protocol not available                             |
| 93        | Protocol not supported                             |
| 94        | Socket type not supported                          |
| 95        | Operation not supported                            |
| 96        | Protocol family not supported                      |
| 97        | Address family not supported by protocol           |
| 98        | Address already in use                             |
| 99        | Cannot assign requested address                    |
| 100       | Network is down                                    |
| 101       | Network is unreachable                           |
| 102       | Network dropped connection on reset              |
| 103       | Software caused connection abort                 |
| 104       | Connection reset by peer                         |
| 105       | No buffer space available                        |
| 106       | Transport endpoint is already connected          |
| 107       | Transport endpoint is not connected              |
| 108       | Cannot send after transport endpoint shutdown    |
| 109       | Too many references                              |
| 110       | Connection timed out                             |
| 111       | Connection refused                               |
| 112       | Host is down                                     |
| 113       | No route to host                                 |
| 114       | Operation already in progress                    |
| 115       | Operation now in progress                        |
| 116       | Stale file handle                                |
| 117       | Structure needs cleaning                         |
| 118       | Not a XENIX named type file                      |
| 119       | No XENIX semaphores available                    |
| 120       | Is a named type file                             |
| 121       | Remote I/O error                                 |
| 122       | Disk quota exceeded                              |
| 123       | No medium found                                  |
| 125       | Operation canceled                               |
| 126       | Required key not available                       |
| 127       | Key has expired                                  |
| 128       | Key has been revoked                             |
| 129       | Key was rejected by service                      |
| 130       | Owner died                                       |
| 131       | State not recoverable                            |
| 132       | Operation not possible due to RF-kill            |
| 133       | Memory page has hardware error                   |

<!-- SUBSECTION -->
## Conditional execution
[Back to Top](#contents)

Conditional execution with `&&` and `||` in `bash` can be used for flow control to execute commands conditionally based on the success or failure of previous commands:

- **`&&` (AND Operator)**:

    ```bash
    $ rm -f test.txt
    $ [ -f test.txt ] && cat test.txt
    $ echo $?
    1
    $ touch test.txt
    $ [ -f test.txt ] && cat test.txt
    $ echo $?
    0
    ```

- **`||` (OR Operator)**:
   
   ```bash
   $ rm text.txt 
   $ rm -f test.txt
   $ touch test.txt
   $ rm -f test.txt || touch test.txt
   $ echo $?
   0
   $ rm -f test.txt || touch test.txt
   $ echo $?
   0
   $ ls test.txt 
   test.txt
   ```

<!-- SUBSECTION -->
## Ternary operator (math)
[Back to Top](#contents)

```bash
$ condition=1
$ result=$((condition ? 10 : 20))
$ echo $result 
10
$ condition=0
$ result=$((condition ? 10 : 20))
$ echo $result 
20
```

<!-- SUBSECTION -->
## Logical operator (math)
[Back to Top](#contents)

```bash
$ a=1; b=0; ((c=(a>b)*5 + (a<=b)*10))
$ echo "${c}"
5
$ a=0; b=1; ((c=(a>b)*5 + (a<=b)*10))
$ echo "${c}"
10
```

<!-- SUBSECTION -->
## If
[Back to Top](#contents)

```bash
$ if <condition>; then
> <command>
> fi
```

```bash
$ if <condition>; then
> <command>
> else
> <command>
> fi
```

```bash
$ if <condition>; then
> <command>
> elif <test>; then
> <command>
> else
> <command>
> fi
```

<!-- SUBSECTION -->
## Case
[Back to Top](#contents)

```bash
$ function check_day() {
>    local -r day="${1}"
>    case "${day}" in
>        "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday")
>            echo "Weekday"
>            ;;
>        "Saturday" | "Sunday")
>            echo "Weekend"
>            ;;
>        *)
>            echo "Invalid"
>            ;;
>    esac
>}
$ check_day Monday
Weekday
$ check_day Sunday
Weekend
$ check_day May
Invalid
```

<!-- SUBSECTION -->
## Trap
[Back to Top](#contents)

`trap` in `bash` is primarily used to catch signals and handle them gracefully within scripts.

```bash
$ trap -l
 1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL       5) SIGTRAP
 6) SIGABRT      7) SIGBUS       8) SIGFPE       9) SIGKILL     10) SIGUSR1
11) SIGSEGV     12) SIGUSR2     13) SIGPIPE     14) SIGALRM     15) SIGTERM
16) SIGSTKFLT   17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU     25) SIGXFSZ
26) SIGVTALRM   27) SIGPROF     28) SIGWINCH    29) SIGIO       30) SIGPWR
31) SIGSYS      34) SIGRTMIN    35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3
38) SIGRTMIN+4  39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12 47) SIGRTMIN+13
48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14 51) SIGRTMAX-13 52) SIGRTMAX-12
53) SIGRTMAX-11 54) SIGRTMAX-10 55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7
58) SIGRTMAX-6  59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
63) SIGRTMAX-1  64) SIGRTMAX
```

```bash
#!/usr/bin/env bash

handle_sigint() {
    echo "SIGINT"
    exit 0
}

trap 'handle_sigint' SIGINT

echo "Running. Press CTRL+C to exit."

while true; do
    sleep 1
done
```

<!-- SECTION -->
# Loops
[Back to Top](#contents)

Note, `continue` and `break` can used with flow control statements.

<!-- SUBSECTION -->
## While
[Back to Top](#contents)

In a while loop, the loop continues executing as long as the condition is true.

   ```bash
   $ while <condition>
   > do 
   >   <command>
   > done
   ```

   ```bash
   $ i=1
   $ while ((i <= 5))
   > do
   >    echo $i
   >    ((i++))
   > done
   1
   2
   3
   4
   5
   ```

<!-- SUBSECTION -->
## Until
[Back to Top](#contents)

In an until loop, the loop continues executing until the condition becomes true.

   ```bash
   $ until <condition>
   > do 
   >   <command>
   > done
   ```

   ```bash
   $ i=1
   $ until ((i > 5))
   > do
   >    echo $i
   >    ((i++))
   > done
   1
   2
   3
   4
   5
   ```

<!-- SUBSECTION -->
## For
[Back to Top](#contents)

   ```bash
   for i in <set>
   do
      <command>
   done
   ```

- **Iterate over a list of space separated values**:

   ```bash
   $ for i in 1 2 3 4 5
   > do 
   > echo $i
   > done
   1
   2
   3
   4
   5
   ```

   ```bash
   $ ((a=1, b=2, c=3, d=4, e=5))
   $ for i in $a $b $c $d $e
   > do 
   > echo $i
   > done
   1
   2
   3
   4
   5
   ```

- **Iterate over a set defined by brace expancion**:

   ```bash
   $ for i in {1..5}; do echo $i; done
   1
   2
   3
   4
   5
   ```

- **Can also use `seq` command, but it is external command, but can be used with variables**:

   ```bash
   $ ((a=1, b=5))
   $ for i in $(seq $a $b); do echo $i; done
   1
   2
   3
   4
   5
   ```

- **C-style for loop**:

   ```bash
   $ ((a=1, b=5))
   $ for ((i=a; i<=b; i++)); do echo $i; done
   1
   2
   3
   4
   5
   ```

- **Infinite C-style loop**:

   ```bash
   $ for (( ; ; ))
   > do
   >   <command>
   > done
   ```

- **Command sustitution**:

   ```bash
   $ touch {1..5}.txt
   $ for file in $(ls *.txt); do
   >   echo "${file}"
   >   rm "${file}"
   > done
   1.txt
   2.txt
   3.txt
   4.txt
   5.txt
   ```

   ```bash
   $ printf "1\n2\n3\n4\n5" > test.txt
   $ for line in $(cat test.txt); do echo "${line}"; done
   1
   2
   3
   4
   5
   ```

   ```bash
   $ printf "1\nA\n2\nB\n3\nC\n4\nD\n5" > test.txt
   $ for line in $(grep "[0-9]" test.txt); do echo "${line}"; done
   1
   2
   3
   4
   5
   ```

- **Iterate over arrays**:

   ```bash
   $ declare -a array=(1 2 3 4 5)
   $ for line in "${array[@]}"; do echo "${line}"; done
   1
   2
   3
   4
   5
   ```

   ```bash
   $ declare -a array=(1 2 3 4 5)
   $ array[8]=0
   $ for i in "${!array[@]}"; do echo "$i ${array[$i]}"; done
   0 1
   1 2
   2 3
   3 4
   4 5
   8 0
   ```

   ```bash
   $ unset array 
   $ declare -A array='([red]=128 [blue]=128 [green]=128)'
   $ for value in "${array[@]}"; do echo "${value}"; done
   128
   128
   128

   ```

   ```bash
   $ unset array 
   $ declare -A array='([red]=128 [blue]=128 [green]=128)'
   for key in "${!array[@]}"; do echo "${key} ${array[${key}]}"; done
   blue 128
   red 128
   green 128
   ```

<!-- SECTION -->
# Functions
[Back to Top](#contents)

```bash
$ [function] <name> () {
>   <command>
>   [return]
> }
```

`function` is an optional keyword. Variables are not named, but can be referenced inside the body `{ ... }` using `$1`, `$2`, etc (same as in scripts). `return` is optional (should return ints), if not specified it will return the exit status of the last command executed in the function.

- **Naming**: 

   Use `function` keyword and descriptive name. 

- **Scope**: 

   Use local variables to prevent side effects, do not rely on global variables (better pass as arguments), rename arguments.

   ```bash
   $ VALUE=0
   $ function fn() {
   >   local value="${1}"
   >   echo "${value}"
   >   return 0
   > }
   $ fn $VALUE
   0
   ```

- **Return Values**: 

Use `return` to exit a function with a status code. To return data, use `echo` or `printf`.

   ```bash
   $ VALUE=0
   $ function fn() {
   >   local value="${1}"
   >   echo "${value}"
   > }
   $ fn $VALUE
   $ result=$(fn "${VALUE}")
   $ echo "${result}"
   0
   ```

- **Error Handling**: Check for errors and return a non-zero status when encountering an error. This allows the calling code to handle the error appropriately.

    ```bash
    do_something() {
      if ! do_something_else; then
        echo "Error occurred" >&2
        return 1
      fi
    }
    ```

<!-- SECTION -->
# Input and parsing
[Back to Top](#contents)

<!-- SUBSECTION -->
# Input
[Back to Top](#contents)

- **`read`:

   `read` is a built-in `bash` command that reads a line from the standard input (or from a file) and assigns it to a variable.

   ```bash
   $ read -p "Enter a number: " number
   Enter a number: 1
   $ echo "${number}"
   1
   ```

   ```bash
   $ read -p "Enter password: " -s password
   Enter password:
   $ if (( "${#password}" < 10 )); then echo "Password must be at least 10 characters long" ; fi
   Password must be at least 10 characters long
   ```

- **`dialog`**:

   `dialog` is a utility for creating interactive dialogs in a text window.

   ```bash
   $ if dialog --title "Question" --yesno "Continue?" 6 25; then
   >  echo "All files deleted!"
   > else
   >  echo "Some files deleted!"
   > fi
   ``

- **`whiptail`**:

   `whiptail` is similar to `dialog` and can be used to produce dialog boxes from shell scripts.

   ```bash
   $ echo "Deleting $(whiptail --inputbox "Enter name?" 8 39 --title "Name query" 3>&1 1>&2 2>&3)'s home directory!"
   ```

   ```bash
   $ options=(1 "A" 2 "B" 3 "C")
   $ choice=$(whiptail --title "Menu Example" --menu "Select one:" 15 50 5 "${options[@]}" 3>&1 1>&2 2>&3)
   ```

   ```bash
   $ whiptail --title "Message" --msgbox "Hi!" 10 50
   ```

   ```bash
   $ (
   >   echo "10"
   >   sleep 1
   >   echo "XXX"
   >   echo "20"
   >   sleep 1
   >   echo "XXX"
   >   echo "40"
   >   sleep 1
   >   echo "XXX"
   >   echo "60"
   >   sleep 1
   >   echo "XXX"
   >   echo "80"
   >   sleep 1
   >   echo "XXX"
   >   echo "100"
   >   sleep 1
   > ) | whiptail --gauge "Progress" 10 50 0
   ```

<!-- SUBSECTION -->
# Parsing arguments and options
[Back to Top](#contents)


- **`getopt`**:
   Ensure `getopt` is installed on your system. It's usually pre-installed on most Unix-like systems.

2. **Script Implementation**:

    ```bash
    #!/bin/bash
    
    # Parse options
    OPTS=`getopt -o ab:c:: --long option-a,option-b:,option-c:: -- "$@"`
    
    if [ $? != 0 ] ; then echo "Failed parsing options." >&2 ; exit 1 ; fi
    
    eval set -- "$OPTS"
    
    # Defaults
    opt_a=false
    opt_b=
    opt_c=
    
    while true; do
      case "$1" in
        -a | --option-a ) opt_a=true; shift ;;
        -b | --option-b ) opt_b="$2"; shift 2 ;;
        -c | --option-c ) opt_c="$2"; shift 2 ;;
        -- ) shift; break ;;
        * ) break ;;
      esac
    done
    
    # Rest of the script goes here
    ```

    - Customize the options `-a`, `-b`, `-c` according to your script requirements.
    - The `--long` options provide a long form of options, e.g., `--option-a`.
    - The `:` and `::` in the option string signify whether an option requires an argument.
    - Use `shift` to discard the processed options and their arguments.

- **`getopts`**:

1. **Script Implementation**:

    ```bash
    #!/bin/bash
    
    # Defaults
    opt_a=false
    opt_b=
    opt_c=
    
    while getopts ":ab:c:" opt; do
      case ${opt} in
        a )
          opt_a=true
          ;;
        b )
          opt_b=${OPTARG}
          ;;
        c )
          opt_c=${OPTARG}
          ;;
        \? )
          echo "Invalid option: $OPTARG" 1>&2
          exit 1
          ;;
        : )
          echo "Invalid option: $OPTARG requires an argument" 1>&2
          exit 1
          ;;
      esac
    done
    shift $((OPTIND -1))
    
    # Rest of the script goes here
    ```

    - Customize the options `-a`, `-b`, `-c` according to your script requirements.
    - The colon `:` after the options in the `getopts` string signifies whether an option requires an argument.
    - Use `${OPTARG}` to access the argument passed to an option.

### Usage:

You can run these scripts like any other Bash script, passing options and arguments as needed:

```bash
./script.sh -a -b value -c
```

These scripts provide a basic framework for parsing arguments and options. You can extend them further based on your specific needs.

<!-- SECTION -->
# Managing scripts, aliases, and other
[Back to Top](#contents)

<!-- SUBSECTION -->
## A good place to put your scripts
[Back to Top](#contents)

- Execute (or source) scripts from the command line

   ```bash
   $ ./<script.sh> # execute or bash <path>/<script.sh`>
   $ . <script.sh> # source <script.sh> (more explicit)
   ```

- Add script directories `$PATH` (export in command line or in `.bashrc`)

   ```bash
   $ export PATH=<path>:$PATH
   $ <script.sh>
   ```

- Keep scripts localy and create links (possibly under different names)

- Place scripts in `/usr/local/bin`

<!-- SUBSECTION -->
## Aliases vs functions vs scripts
[Back to Top](#contents)

In `bash`, aliases, functions, and scripts serve similar purposes in that they allow you to bundle commands into reusable units, but they have different scopes and are used in different scenarios.

- **Alias**:
   - `alias` is a shortcut for a single command or a series of commands

      ```bash
      $ alias la
      alias la='ls -A'
      ```

   - Typically defined in a user’s shell profile file, e.g in `.bashrc`

   - Aliases are text substitutions, they are not sutable to handle arguments

   - Aliases are can be affected by the current shell environment

   - Use for simple command substitutions or for a quick shorthand for a long command

- **Function**:

   - Functions can accept arguments and contain complex logic

   - Typically defined in a user’s shell profile file, e.g in `.bashrc`, or in other files that are sourced to make functions avaliable

   - Functions are executed in the current shell without spawning a new process

   - They are suitable for sequences of commands that need to act like a single command and are too complex for an alias

      ```bash
      function python () {
         cat ${1} | ssh -Y <user>@<host> python
      }
      ```

- **Script**:

   - A script is a separate file which can be executed (program), can be as simple as a single command or as complex as a full-fledged application

   - Scripts can accept arguments, use complex logic

   - They run in a new shell process, meaning they don’t affect the current shell environment

   - Scripts are useful for complex tasks and are easy to share and run on different systems

   - They are the best option for automated tasks that need to be executed regularly or on multiple systems

**When to Use Each**:

- **Use an alias** when you want a shorthand for a command or a series of commands you frequently use. For example, `alias ll='ls -la'`.
  
- **Use a function** when you need something more complex than an alias but you don't want to leave the current shell context. Functions are powerful when you need to process arguments or when you need to include some logic before executing commands.

- **Use a script** for standalone tasks that might be run independently of a shell session, potentially by different users or systems. If the task is complex and involves a lot of logic or if you want to distribute the command as a tool, a script is the way to go.

Start with an alias for simplicity, move to a function if you need more complexity or parameters, and create a script when the task becomes sufficiently complex or when it needs to be portable.

<!-- SUBSECTION -->
## .bashrc
[Back to Top](#contents)

The `.bashrc` (`rc` = run commands) file is a script that is executed (sourced) whenever a new terminal session is started in interactive mode. It's a place where you can define and customize your shell environment.

### What to place in `.bashrc`:

- **Alias Definitions**: Shortcuts for long commands that you use frequently

- **Function Definitions**: Custom functions for sequences of commands that you need to use regularly

- **Environment Variables**: Such as `PATH` or custom variables that you want to be available in every session

- **Prompt Customization**: Settings that change the appearance of your shell prompt (e.g., `PS1`)

- **Command History Configuration**: Settings that affect the behavior of your command history (e.g., `HISTSIZE`, `HISTFILESIZE`, etc.)

- **Shell Options**: Options that affect the behavior of the shell itself (e.g., `shopt` options in bash)

### What not to place in `.bashrc`:

- **Sensitive Information**: Passwords or any other sensitive data should not be stored in plain text

- **Heavy Computation or Slow Commands**: Anything that can slow down the startup of your shell, such as heavy computations or commands that take a long time to execute

- **Interactive Commands**: Commands that require user interaction should not be placed in `.bashrc` since it can prevent the shell from starting properly

- **Session-Specific Commands**: Commands that are meant to run only once when a login shell starts should go into `.bash_profile` or `.profile`, not `.bashrc`

- **Large Blocks of Application-Specific Configuration**: If you have a complex setup for a particular application, it's often better to source a separate script file

### General Tips:

- **Backup your .bashrc**: Before making changes, it's always a good idea to create a backup of your current `.bashrc`

- **Comments**: Always comment your changes, so you or others can understand why a particular configuration was made

- **Keep it Organized**: Group related settings and keep separate concerns well organized within the file

- **Modular Approach**: Consider sourcing other scripts from your `.bashrc` for complex configurations (e.g., `source ~/my_bash_aliases.sh`)

Changes to `.bashrc` won't take effect in current sessions until you source the file with `source ~/.bashrc` or open a new terminal.
