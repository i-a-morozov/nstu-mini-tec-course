<!-- SECTION  -->
# Contents
- [01-Linux file system description and navigation](#linux-file-system-description-and-navigation)
    - [Everything is a file](#everything-is-a-file)
    - [Filesystem Hierarchy Standard](#filesystem-hierarchy-standard)
    - [Path (absolute and relative)](#path-absolute-and-relative)
    - [Relevant commands and examples](#relevant-commands-and-examples)
- [02-File viewing and manipulation](#file-viewing-and-manipulation)
    - [File types](#file-types)
    - [Permissions](#permissions)
    - [Relevant commands and examples](#relevant-commands-and-examples-1)
- [03-Getting help](#getting-help)
    - [Is command build-in](#is-command-build-in)
    - [Relevant commands and examples](#relevant-commands-and-examples-2)
- [04-Package management](#package-management)
    - [Package](#package)
    - [Relevant commands and examples](#relevant-commands-and-examples-3)
- [05-User management](#user-management)
    - [Common tasks](#common-tasks)
    - [Resources control](#resources-control)
    - [Relevant commands and examples](#relevant-commands-and-examples-4)
- [06-Processes and jobs management](#processes-and-jobs-management)
    - [Processes](#processes)
    - [Jobs](#jobs)
    - [Relevant commands and examples](#relevant-commands-and-examples-5)
- [07-System monitoring](#system-monitoring)
    - [Resources](#resources)
    - [Services](#services)
    - [Relevant commands and examples](#relevant-commands-and-examples-6)
- [08-Networking](#networking)
    - [Networking components](#networking-components)
    - [Networking tasks](#networking-tasks)
    - [Relevant commands and examples](#relevant-commands-and-examples-7)

<!-- SECTION  -->
# Linux file system description and navigation
[Back to Top](#contents)

## Everything is a file
[Back to Top](#contents)

The concept "everything is a file" is a fundamental design concept in Linux (and Unix-like systems).
All the following are file under this concept:

- Files
- Directories
- Links
- Devices
- Processes
- Sockets
- ...

## Filesystem Hierarchy Standard
[Back to Top](#contents)

The Linux file system is structured as a hierarchical directory tree, with the root denoted by `/`. 
This file system hierarchy is defined by the Filesystem Hierarchy Standard (FHS), which sets the standard locations for files and directories. 
The following command can be used to see the contents of the `/` directory. 
Note, `->` means the directory (file) is in fact a link, you can check where the link points using `readlink` command.

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

You might need to install `tree` first:

```bash
$ sudo apt install tree
```

|Directory | Description |
|-----------|-------------|
| `/`       | The root directory: Everything is located under the root directory. |
| `/bin`    | User Binaries: Contains user command binaries. |
| `/boot`   | Boot Loader Files: Contains the boot loader files, such as kernels, initrd (initial ram disk), and sometimes configuration files for the boot loader. |
| `/dev`    | Device Files: Contains device files that represent hardware components as well as some software devices. |
| `/etc`    | Configuration Files: Contains configuration files required by all programs, startup and shutdown shell scripts used to start/stop individual programs. |
| `/home`   | Home Directories: Contains the personal directories of all users (each user has a directory within the `/home` directory). |
| `/lib`    | System Libraries: Holds the essential shared libraries needed to boot the system and run the commands in the root file system. |
| `/media`  | Removable Media: This directory contains subdirectories which are automatically created or removed when removable media devices are mounted or unmounted. |
| `/mnt`    | Mount Directory: Used for temporarily mounted file systems, such as network file systems or other temporary file systems. |
| `/opt`    | Optional add-on Applications: Contains add-on applications from individual vendors. |
| `/proc`   | Process Information: A virtual file system that provides process and kernel information as files. |
| `/root`   | Root Home Directory: The home directory for the root user. |
| `/run`    | Run-time Variable Data: Holds variable data that describes the running system since the last boot, such as the system's process ID. |
| `/sbin`   | System Binaries: Contains essential binaries that are generally intended to be run by the root user for system administration. |
| `/srv`    | Service Data: Contains data for services provided by the system. |
| `/sys`    | System Files: A virtual file system that contains information about the system and the devices connected to it (system's hardware organization structure). |
| `/tmp`    | Temporary Files: Intended for the storage of temporary files, which are cleared on system reboot. |
| `/usr`    | User Programs: Contains the majority of user utilities and applications, such as user binaries, libraries and documentation. |
| `/var`    | Variable Files: Contains files that are expected to grow in size, such as logs. |


## Path
[Back to Top](#contents)

Since file system is a tree, it possible to navigate to any of its nodes starting from the root or from the current working directry (or relative to the user).

- **Absolute Path**

    ```bash
    $ cd /home/nstu
    $ pwd
    /home/nstu
    ```

- **Relative Path**

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

- **What do you think will happen here?**

    ```bash
    $ cd
    $ cd ./Documents/../Downloads/
    $ pwd
    ```

## Relevant commands and examples
[Back to Top](#contents)

- `pwd`: Prints the current working directory.

- `ls`: Lists the contents of a directory.

    ```bash
    $ # List all files (including hidden ones) with detailed info
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
    $ # List files in a directory
    $ ls /home/nstu
    Desktop  Documents  Downloads  Music  Pictures  Public  snap  Templates  Videos
    ```

    ```bash
    $ # List files and select only hidden files
    $ cd
    $ ls -a | grep '^\.'
    .
    ..
    .bash_history
    .bash_logout
    .bashrc
    ...
    ```

- `tree`: Displays directory structure in a tree-like format.

    ```bash
    $ # List all files (tree-like) with level one along with user and size info
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

- `cd`: Changes the current directory.

    ```bash
    $ # Toggle between two previous directories
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

- `mkdir`: Creates a new directory.

    ```bash
    $ # Make nested directories
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
    $ # Set directory mode
    $ # Can look at the directory itself
    $ # Bun can't look inside the directory
    $ mkdir -m u-r test
    $ ls -ld test
    d-wxrwxr-x 2 nstu nstu 4096 Feb  1 11:02 test
    $ ls test
    ls: cannot open directory 'test': Permission denied
    ```

- `rmdir`: Removes an empty directory.

    ```bash
    $ # Remove empty directory
    $ rmdir test
    ```

- `rm`: Deletes files or directories.

    ```bash
    $ # Remove directories and their contents recursively
    $ rm -r backup
    ```

    ```bash
    $ # Ignore nonexistent files and arguments, never prompt
    $ rm test.txt
    rm: cannot remove 'test.txt': No such file or directory
    $ rm -f test.txt
    $ touch test.txt
    $ chmod u-w test.txt
    $ rm test.txt
    rm: remove write-protected regular empty file 'test.txt'? n
    $ ls text.txt
    test.txt
    $ rm -f test.txt
    ```

    ```bash
    $ # Remove files using wildcards (patterns like `?` and `*` to match characters in file names)
    $ touch file-{01..10}.txt
    $ ls file-*.txt
    file-01.txt  file-02.txt  file-03.txt  file-04.txt  file-05.txt  file-06.txt  file-07.txt  file-08.txt  file-09.txt  file-10.txt
    $ rm file-*.txt
    ```

- `cp`: Copies files or directories.

    ```bash
    $ # Recursive copy with verbose
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
    $ # Backup on copy
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

- `mv`: Moves or renames files or directories.

    ```bash
    $ # Move/rename
    $ touch text.txt
    $ mv text.txt data.txt
    $ ls *.txt
    data.txt
    $ rm data.txt 
    ```

    ```bash
    $ # Do not overwrite an existing file
    $ touch text.txt data.txt
    $ echo 'msg' > text.txt 
    $ cat text.txt 
    msg
    $ mv -n text.txt data.txt 
    $ cat data.txt 
    $ rm text.txt data.txt 
    ```

- `find`: Searches for files in a directory hierarchy.
 
    ```bash
    $ mkdir -p backup/version-{1..5}
    $ touch backup/version-{1..5}/readme.txt
    $ tree backup/
    backup/
    ├── version-1
    │   └── readme.txt
    ├── version-2
    │   └── readme.txt
    ├── version-3
    │   └── readme.txt
    ├── version-4
    │   └── readme.txt
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
    $ # Find all directories
    $ find backup -type d
    backup
    backup/version-4
    backup/version-1
    backup/version-5
    backup/version-2
    backup/version-3
    ```

    ```bash
    $ # Find and remove all *.txt files
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
    $ # Find files with specific size
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

<!-- SECTION  -->
# File viewing and manipulation
[Back to Top](#contents)

Relevant commands from previous section for file manipulation:

- `mkdir`: create directory
- `rmdir`: remove directory
- `cp`: copy file
- `mv`: move (or rename) file
- `rm`: remove file

## File types
[Back to Top](#contents)

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

Files are categorized not only by their content but also by their purpose and behavior. There are several different file types, which include:

- **Regular Files (-):** Common file type for text, data, program instructions, or other information and can be binary or human-readable.
- **Directory (d):** Directories are files that list other files and directories.
- **Link (l):** A link is a shortcut or a reference to another file or directory.
- **Character Device File (c):** This file type provides serial access to hardware devices.
- **Block Device File (b):** This file type represents a device file that provides buffered access to hardware devices.
- **FIFO (p):** Named pipe, it is used for inter-process communication.
- **Socket (s):** This file type is used for inter-process communication.

```bash
$ find /dev -type c
$ find /dev -type b
```

To determining file type you can use `ls -l`, `file` or `stat` command:

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

For links, you can also use `readlink` command to show the link target.

## Permissions
[Back to Top](#contents)

```bash
$ mkdir test
$ touch test.txt
$ touch test.sh && chmod u+x test.sh
$ ls -ldrh test*
-rw-rw-r-- 1 nstu nstu    0 Feb  1 11:30 test.txt
-rwxrw-r-- 1 nstu nstu    0 Feb  1 11:30 test.sh
drwxrwxr-x 2 nstu nstu 4,0K Feb  1 11:29 test
```

In Linux, each file and directory has an associated set of permissions that determine who can **read**, **write**, and **execute** them.

Permission types:

- **No permission (-):** No permission for the respective operation.
- **Read (r):** The read permission on a file allows you to view the contents of the file. On a directory, it allows you to list the contents of the directory.
- **Write (w):** The write permission on a file allows you to modify and delete the file. On a directory, it allows you to add, remove, and rename files stored in the directory.
- **Execute (x):** The execute permission on a file allows you to run the file as a program or script. On a directory, it allows you to access the directory's contents, i.e., go into the directory (change directory command).

Permission categories:

- **User (u):** The file's owner.
- **Group (g):** The set of users who belong to the file's group.
- **Others (o):** Everyone else not in the user or group category.

Note, you can use `groups` command to see the groups you are a member of.

Octal notation (represents owner, group and others by a single octal digit):

- 0 - no permissions
- 1 - execute only
- 2 - write only
- 3 - write and execute (1+2)
- 4 - read only
- 5 - read and execute (4+1)
- 6 - read and write (4+2)
- 7 - read, write, and execute (4+2+1)

`stat` can be used to check correspondence between alphanumeric and octal notations:

```bash
$ stat -c '%A %a %n' test*
drwxrwxr-x 775 test
-rwxrw-r-- 764 test.sh
-rw-rw-r-- 664 test.txt
```

Changing Permissions (`chmod` command):

- **Alphanumeric method (use this one, but be aware of octal notation):**
   - `u` for user, `g` for group, `o` for others, `a` for all.
   - `+` to add a permission, `-` to remove a permission, `=` to set a permission and remove others.
   - `r` for read, `w` for write, `x` for execute.

    ```bash
    $ ls -l test.sh
    -rwxrw-r-- 1 nstu nstu 0 Feb  1 11:30 test.sh
    $ chmod g+x test.sh
    $ ls -l test.sh
    -rwxrwxr-- 1 nstu nstu 0 Feb  1 11:30 test.sh
    ```

- **Octal method:**
   - 4 for read (r), 2 for write (w), 1 for execute (x).
   - These values can be added together to set multiple permissions.

Changing Ownership (`chown` command):

- **Change the user owner:**  `chown username filename`
- **Change the group owner:** `chown :groupname filename`
- **To change both user and group owner:** `chown username:groupname filename`

Changing Group Ownership (`chgrp`):

- **Change the file's group:** `chgrp groupname filename` (list groups `getent group | sort`)

## Relevant commands and examples
[Back to Top](#contents)

- `touch`: Creates an empty file or updates the timestamp of an existing file.

    ```bash
    $ # Create empty file
    $ touch test.txt
    $ file test.txt
    test.txt: empty
    ```

    ```bash
    $ # Set timestamp
    $ touch -t 197001010000 test.txt
    $ ls -l test.txt 
    -rw-rw-r-- 1 nstu nstu 0 Jan  1  1970 test.txt
    ```

    ```bash
    $ # Update access time
    $ touch -a test.txt && stat -c '%x' test.txt 
    2024-02-01 12:39:18.235509181 +0700
    $ touch -a test.txt && stat -c '%x' test.txt 
    2024-02-01 12:39:21.935509359 +0700
    ```

- `stat`: Displays detailed information about a particular file or file system.

    ```bash
    $ # Displays detailed file information
    $ stat test.txt 
    File: test.txt
    Size: 0               Blocks: 0          IO Block: 4096   regular empty file
    ...
    ```

    ```bash
    $ # Shows name ans size in bytes
    $ truncate -s 16M text.txt
    $ stat -c '%n %s' text.txt 
    text.txt 16777216
    ```

    ```bash
    $ # Displays the file permissions
    $ stat --format='%A' test.txt 
    -rw-rw-r--
    ```

    ```bash
    $ # Sort by size in descending order
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

- `ln`: Creates links (hard or symbolic) between files.

    ```bash
    $ # Create hard link (points to the same disk memory)
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
    $ # Create symbolic link
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
    $ # Change link target
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

- `more`: Views file contents.

    ```bash
    $ # Views file contents (page by page)
    $ touch test.txt
    $ for i in $(seq 10); do echo $i >> test.txt; done
    $ more test.txt
    $ rm test.txt
    ```

- `less`: Views file contents (press `h` for help, press `q` to exit).

    ```bash
    $ # Views file contents (page by page)
    $ touch test.txt
    $ for i in $(seq 10); do echo $i >> test.txt; done
    $ less test.txt
    $ rm test.txt
    ```

- `cat`: Concatenates and displays file contents (also see `tac` and `split`).

    ```bash
    $ # Displays file contents
    $ touch test.txt
    $ echo 'test' > test.txt
    $ cat test.txt
    test
    ```

    ```bash
    $ # ConCATenates files
    $ touch test.txt data.txt
    $ echo 'test' > test.txt
    $ echo 'data' > data.txt
    $ cat -n test.txt data.txt
        1  test
        2  data
    ```
- `head`: Displays the first part of files.

    ```bash
    $ # Displays the first 5 lines
    $ rm -f test.txt ; touch test.txt
    $ for i in $(seq 10); do echo $i >> test.txt; done
    $ head -n 5 test.txt
    1
    2
    3
    4
    5
    ```

- `tail`: Displays the last part of files.
    
    ```bash
    $ # Displays the last 5 lines
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
    $ # Monitor new entries in syslog (or sudo watch -n 1 tail -n 5 /var/log/syslog)
    $ # Press Ctrl+C to exit
    $ sudo tail -f /var/log/syslog
    ```

- `grep`: Searches for patterns in files.

    ```bash
    $ # Searches for pattern
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
    $ # Case-insensitive search for pattern
    $ echo 'pattern' > test.txt
    $ echo 'PATTERN' >> test.txt
    $ grep -i 'pattern' test.txt 
    pattern
    PATTERN
    ```

    ```bash
    $ # Search in several files
    $ echo 'pattern' > test.txt
    $ echo 'pattern' > data.txt
    $ grep 'pattern' test.txt data.txt
    test.txt:pattern
    data.txt:pattern
    ```

    ```bash
    $ # Recursive search
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

- `diff`: Compares files line by line.

    ```bash
    $ # Compares files (normal and unified)
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

    - Normal format

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

        - `1c1`: line 1 in the first file has been changed (`c`) with line 1 in the second file
        - `< year: 2023`: prefix `<` shows the content of line 1 in the first file
        - `---`: this is a separator line used by `diff` to distinguish between content of different files
        - `> year: 2024`: prefix `>` shows the content of line 1 in the second file
        -  The first change block reads "year: 2023" in `test.txt` has been changed to "year: 2024" in `data.txt`
        - `3c3,4`: starting at line 3 in `test.txt` (`3c`) and affecting lines 3 and 4 in `data.txt` (`3,4`)
        - `< file: test.txt`: shows the content of line 3 in `test.txt`
        - `> list: 1`: shows new content at line 3 in `data.txt`
        - `> file: data.txt`: shows new content at line 4 in `data.txt`
        - The second change block reads "file: test.txt" in `test.txt` (line 3) replaced by "list: 1" and "file: data.txt" in `data.txt` (lines 3 and 4)
    
    - Unified format

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

        - `--- test.txt ...`: indicates the first file (`test.txt`)
        - `+++ data.txt ...`: indicates the second file (`data.txt`)
        - `@@ -1,3 +1,4 @@`: (hunk header), shows where the changes are located in the files
        - `-1,3`: indicates that the changes start from line 1 and span 3 lines in `test.txt`
        - `+1,4`: indicates that the changes start from line 1 and span 4 lines in `data.txt`
        - Explicit changes are listed after the header
        - Lines starting with `-` are from `test.txt`
        - Lines starting with `+` are from `data.txt`
        - Lines without a `+` or `-` are unchanged and are shown as context
        - `-year: 2023`: line was in `test.txt` but has been removed or modified in `data.txt`
        - `+year: 2024`: line has been added or modified in `data.txt`
        - `data: 01`: line is unchanged in both files and is included for context
        - `-file: test.txt`: line was in `test.txt` but has been removed or replaced in `data.txt`
        - `+list: 1`: line has been added in `data.txt`
        - `+file: data.txt`: line has also been added in `data.txt`.

- `sort`: Sorts lines of text files.

    ```bash
    $ # Normal are reverse sort (alphanumeric)
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
    $ # Numeric sort
    $ sort -n test.txt
    1
    5
    10
    15
    20
    ```

    ```bash
    $ # Sort by the second field (numeric)
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

- `cut`: Removes sections from each line of files.

    ```bash
    $ # Cuts and displays the 1st field of each line (can select multiple fields)
    $ cut -d':' -f2 test.txt
    2023
    2020
    2021
    2007
    ```

    ```bash
    $ # Displays the 1st character
    $ cut -c1-1 test.txt 
    a
    b
    c
    d
    ```

- `uniq`: Reports or omits repeated lines.

    ```bash
    $ # Displays unique lines
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
    $ # Displays counts, duplicates and unique
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

- `wc`: Counts lines, words, and characters in files.

    ```bash
    $ # Count number of lines in a file
    $ wc -l test.txt 
    6 test.txt
    ```

    ```bash
    $ # Count number of words in a file (use -c for characters)
    $ wc -w test.txt 
    6 test.txt
    ```

    ```bash
    $ # Count number of directories
    $ find ~ -maxdepth 1 -name "*" ! -name ".*" -type d | wc -l
    10
    ```

- `tee`: Reads from standard input and writes to standard output and files.

    ```bash
    $ # Write (intermediate) result to a file
    $ echo $USER | tee user.log | wc -c
    4
    $ cat user.log
    nstu
    ```

    ```bash
    $ # Append
    $ echo 'line1' | tee file1.txt | tee -a file2.txt > /dev/null
    $ echo 'line2' | tee file1.txt | tee -a file2.txt > /dev/null
    $ cat file1.txt  file2.txt 
    line2
    line1
    line2
    ```

- `nl`: Adds line numbers to any text.

    ```bash
    $ # Add line numbers
    $ printf "a \nb \nc \nd" > test.txt
    $ nl test.txt
        1  a 
        2  b 
        3  c 
        4  d
    ```

- `ar`: Archive utility, used to create and modify archive files.

    ```bash
    $ # Create archive
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

- `tar`, `zip`, `unzip`: Archive files

    ```bash
    $ # Archive with tar
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
    $ # Archive with zip
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

- `sed`: Stream editor for filtering and transforming text.

    ```bash
    $ # Replace
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
    $ # Print specific line
    $ sed -n '5p' test.txt
    b
    ```

    ```bash
    $ # Delete by pattern
    $ sed '/[a,b]/d' test.txt
    c
    c
    ```

- `awk`: Programming language designed for text processing.

    ```bash
    $ # Print field
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
    $ # Pattern search
    $ awk '/C/{print $2}' test.txt 
    3
    ```

    ```bash
    $ # Some math functions
    $ awk '{sum+=$2} END {print sum}' test.txt
    15
    $ awk '{if ($2 == 5) print $1}' test.txt
    E
    ```

- `nano`, `vim`, `vi`, `neovim`: Terminal based text editors (checkout kickstart `neovim` on github)

    Some `vim` basics:

    - `vim [file]`

    - **Normal Mode**:
        - Default mode
        - Used for navigation, copy, cut, paste, and other editing commands
        - Enter Normal mode from other modes by pressing `Esc`

    - **Insert Mode**:
        - For inserting text
        - Enter from Normal mode by pressing `i`
        - Exit to Normal mode by pressing `Esc`

    - **Visual Mode**:
        - For selecting blocks of text
        - Enter from Normal mode by pressing `v` (character), `V` (line), or `Ctrl + v` (block)
        - Exit to Normal mode by pressing `Esc`

    - **Replace Mode**:
        - For replacing text
        - Enter from Normal mode by pressing `R`
        - Exit to Normal mode by pressing `Esc`

    - **Command-Line Mode**:
        - For entering editor commands (saving, quitting)
        - Enter from Normal mode by pressing `:` (commands), `/` (forward search), or `?` (backward search)
        - Execute a command with `Enter`, then return to Normal mode
        - `:q` - quit, `:!q` - quit without saving, `:wq` - write and quit

- `curl` or `wget`: Download files from the web (you might need to install them first `sudo apt install curl wget`)

    ```bash
    $ # Terminal browser
    $ curl "ipinfo.io"
    $ curl "wttr.in/Novosibirsk"
    ```

    ```bash
    $ # Download files
    $ curl -O https://raw.githubusercontent.com/i-a-morozov/nstu-mini-tec-course/main/README.MD
    $ wget https://raw.githubusercontent.com/i-a-morozov/nstu-mini-tec-course/main/LICENSE
    ```

<!-- SECTION  -->
# Getting help
[Back to Top](#contents)

In this section we will learn how to get help for commands.
Some of commands are build-in within the shell, like `cd`.
They in particular do not have `man` pages and you can't `sudo` them.

```bash
$ sudo cd /
sudo: cd: command not found
sudo: "cd" is a shell built-in command, it cannot be run directly.
sudo: the -s option may be used to run a privileged shell.
sudo: the -D option may be used to run a command in a specific directory.
```

Look at `man buildins` output for more information on build-ins.

## Is command build-in?
[Back to Top](#contents)

Shell, like `bash`, comes with a set of build-in commands (`man buildins`).

- `type`

    ```bash
    $ type cd
    cd is a shell builtin
    $ type ls
    ls is aliased to `ls --color=auto'
    ```

- `command` (without flags,test if command exists)

    ```bash
    $ command -V cd
    cd is a shell builtin
    $ command -V ls
    ls is aliased to `ls --color=auto'
    ```

- `help` (`bash` specific, works for builtins)

    ```bash
    $ help cd
    cd: cd [-L|[-P [-e]] [-@]] [dir]
    ...
    $ help ls
    -bash: help: no help topics match `ls'.  Try `help help' or `man -k ls' or `info ls'.
    ```

## Relevant commands and examples
[Back to Top](#contents)

- `man`: Manual pages.

    ```bash
    $ # Displays the manual page for the ls command
    $ man ls
    ```

    ```bash
    $ # C functions documentation
    $ man malloc
    ```

    - **Sections**: `man N ...`
        - (1) General commands
        - (2) System calls
        - (3) C library functions
        - (4) Special files and drivers (/dev)
        - ...

- `whatis`: Display one-line manual page description (`man -f`).

    ```bash
    $ # Note, section is also printed
    $ whatis grep
    grep (1)             - print lines that match patterns
    ```

- `apropos`: Search the manual page names and descriptions (`man -k`).

    ```bash
    $ # Note, section is also printed
    $ apropos udisks
    udisks (8)           - Disk Manager
    udisks2.conf (5)     - The udisks2 configuration file
    udisksctl (1)        - The udisks command line tool
    udisksd (8)          - The udisks system daemon
    umount.udisks2 (8)   - unmount file systems that have been mounted by UDisks2
    ```

- `whereis`: Locate the binary, source, and manual page files.

    ```bash
    $ whereis bash
    bash: /usr/bin/bash /usr/share/man/man1/bash.1.gz
    ```

- `info`: Read info documents.

    ```bash
    $ # Read info about tar
    $ info tar
    ```

- `tldr`: Simplified and community-driven man pages (examples).

    ```bash
    $ # Updates the local cache of tldr pages (do this first)
    $ tldr -u`: 
    ```

    ```bash
    $ # Show examples for grep
    $ tldr grep
    ```

- `command --help` or `command --help | less`

    ```bash
    $ man --help
    Usage: man [OPTION...] [SECTION] PAGE...
    ...
    ```

- Others
    - [Unix & Linux StackExchange](https://unix.stackexchange.com/)
    - [Ask Ubuntu](https://askubuntu.com/)
    - LLMs


<!-- SECTION  -->
# Package management
[Back to Top](#contents)

## Some definitions
[Back to Top](#contents)

In Linux, software distribution and management are primarily handled through the concept of packages and package managers.
This system simplifies the process of installing, updating, configuring, and removing software.

- **Packages**:
A package in Linux is a compressed file archive containing all of the files necessary to run a particular software program. 
These files usually include the executable program, documentation, configuration files, and additional dependencies required for the software to run properly. 
Common package formats include `.deb` (Debian, Ubuntu) and `.rpm` (Red Hat).

- **Package Management**: 
Package management is the process of handling software installation and maintenance in a systematic way. 
It helps in easy installation, upgrade, configuration, and removal of software. 
Software packages are stored in repositories, which are servers hosting a large number of packages. 
These repositories are accessed over the internet and can be official (provided by the distribution maintainers) or third-party.

- **Package Managers**: A package manager is a collection of tools that automate the process of installing, upgrading, configuring, and removing software packages from a Linux system.
   
## Relevant commands and examples
[Back to Top](#contents)

- `apt`: Advanced package tool (system level packages) (Debian, Ubuntu, ...).

    - `sudo apt update`: Updates the list of available packages and their versions.
    - `sudo apt upgrade`: Upgrades all installed packages to the latest versions.
    - `sudo apt install <package>`: Installs package.
    - `sudo apt remove <package>`: Removes package without removing its configuration files.
    - `sudo apt purge <package> `: Removes both package and its configuration files.
    - `apt list`: List installed packages (can save list of installed packages into a file `sudo apt list > packages.txt`, or pipe to `less`/`grep`/...)

- `snap`: Ubuntu (Canonical) package tool (system level packages).

    - `sudo snap refresh`: Updates all installed snaps to their latest versions.
    - `sudo snap install <package>`: Installs package.
    - `sudo snap remove <package>`: Removes package.
    - `snap find "text"`: Searches for snaps related to "text".
    - `sudo snap revert <package>`: Reverts the installed package to the previous version.

- `flatpak`: Distribution independent package tool: install, build, run applications (system level packages) (`sudo apt install flatpack`).

    - `flatpak update`: Updates all installed flatpak applications.
    - `flatpak list`: Lists all installed flatpak applications.
    - `flatpak install flathub <application>`: Installs application from `flathub` repository.
    - `flatpak uninstall <application>`: Uninstalls application.
    - `flatpak run <application>`: Runs application.

- `dpkg`: Debian low-level package manager (system level packages) (`.deb` packages can be installed with `apt` with automatic dependencies).
    
    - `sudo dpkg -i <package.deb>`: Installs package from file.
    - `sudo dpkg -r <package>`: Removes a package without removing its configuration files.
    - `dpkg -l`: Lists all installed Debian packages.

- `alien`:  Convertor between different Linux package formats (system level packages) (`sudo apt install alien`).

    - `sudo alien package.rpm`: Converts a `.rpm` package file to a Debian package file `.deb`.
    - `sudo alien -i <package.rpm>`: Converts a `.rpm` package to `.deb` and installs it.

- `aptitude`: `apt` with terminal based interface (system level packages) (`sudo apt install aptitude`).

    - `sudo aptitude`: Starts in interactive mode.
    - `sudo aptitude update`: Updates the list of available packages.
    - `sudo aptitude install <package>`: Installs package.
    - `sudo aptitude remove <package>`: Removes package without removing its configuration files.
    - `sudo aptitude purge <package>`: Removes package and its configuration files.
    - `sudo aptitude search "text"`: Searches for packages related to "text".

- `synaptic`: `apt` with GUI (system level packages) (`sudo apt install synaptic`).

- `conda`: Anaconda package manager (user level packages, not limitted to Python!).

    - `conda --help`: General help
    - `conda command --help`: Command help (`install`, `list`, ...)
    - `conda install <package>`: Installs package.
    - `conda update <package>`: Updates package (`conda update conda`).
    - `conda create -n <name> python=<version>`: Creates a new conda environment named "name" with Python "version".
    - `conda activate <name>`: Activates the conda environment "name".
    - `conda deactivate`: Deactivates current environment.
    - `conda list`: Lists all packages installed in the current conda environment.

- `pip`: Python package installer (user level packages).

    - `pip --help`: General help
    - `pip command --help`: Command help (`install`, `list`, ...)
    - `pip install <package>`: Installs package.
    - `pip install --upgrade <package>`: Installs package or upgrade installed.
    - `pip uninstall <package>`: Uninstalls package.
    - `pip list`: Lists all installed Python packages.
    - `pip freeze > requirements.txt`: Generates a requirements.txt file with all installed packages and their versions.
    - `pip install -e .`: Installs package (along with specified dependencies) from a current directory (`pyproject.toml`, `setup.py`, ..,) in edit mode
    - `pip install -r requirements`: Installs packages from a requirements file.

- Other: `sh`, `make` (follow installation instructions, if none, first try without `sudo`)

    - `chmod +x <application>.sh`, `./<application>.sh`
    - `make`, `make install`
    - `ninja`, `meson` and other build systems


<!-- SECTION  -->
# User management
[Back to Top](#contents)

## Common tasks
[Back to Top](#contents)

```bash
$ # Add user
$ sudo useradd student
```

```bash
$ # Set (change) user password
$ sudo passwd student
```

```bash
$ # Create group
$ sudo groupadd course
```

```bash
$ # Add to group
$ sudo usermod -aG course student
$ groups student 
student : student course
```

```bash
$ # Login/logout
$ sudo login
nstu login: student
Password: 
$ echo $USER
student
$ exit
```

```bash
$ # Remove user and corresponding home directory
$ sudo userdel -r student
```

```bash
$ # Create with options
$ sudo useradd -m -d /home/student -s /bin/bash -G course student
$ sudo passwd student
```

## Resources control
[Back to Top](#contents)

- `quota`: Set disk quotas for users (`sudo apt install quota`).

    - `sudo apt install quota`
    - `sudo nano /etc/fstab` (change `errors=remount-ro` to `errors=remount-ro,usrquota,grpquota`)
    - `sudo mount -o remount /`
    - `sudo quotacheck -cugm /` (initialize database)
    - `sudo edquota -u student` (set quota, e.g 1048576 in soft & hard for 1G)
    - `sudo quotaon /` (activate quotas)
    - `sudo quota -u student` (check quota)

    ```bash
    $ sudo login student
    $ dd if=/dev/zero of=tmp.log bs=1M count=1024
    dd: error writing 'tmp.log': Disk quota exceeded
    1024+0 records in
    1023+0 records out
    1073713152 bytes (1,1 GB, 1,0 GiB) copied, 0,459262 s, 2,3 GB/s
    ```

- `ulimit`: Resources available to the shell and to processes started by it (for current shell session). 

    - `ulimit -a`: View limits
    - `ulimit -u`: Set maximum number of processes
    - `ulimit -t`: Set CPU time limit in seconds 
    - `ulimit -f`: Set files size limit
    - `ulimit -s`: Set stack size limit (set `ulimit -s unlimited` for memory intense tasks)
    - `ulimit -m`: Set memory limit (`-v` for virtual memory)
    - `sudo nano /etc/security/limits.conf`: Set limits for a user (regular user can decrease limits, but not increase)

    ```bash
    $ # View current user limits
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

## Relevant commands and examples
[Back to Top](#contents)

- `sudo`: Executes a command as another user, typically as the superuser.

    ```bash
    $ # Run command as superuser
    $ sudo apt update
    $ sudo apt upgrade
    ```

    ```bash
    $ # Execute command as user
    $ sudo -u student touch /home/student/password
    $ ls /home/student/
    ls: cannot open directory '/home/student/': Permission denied
    $ sudo -u student ls /home/student/
    password
    ```

    ```bash
    $ # Starts a shell session as the superuser
    $ sudo -s
    # id
    uid=0(root) gid=0(root) groups=0(root)
    # exit
    exit
    ```

    ```bash
    $ # Re-executes the previous command as the superuser
    $ cat /etc/sudoers
    cat: /etc/sudoers: Permission denied
    $ sudo !!
    sudo cat /etc/sudoers
    #
    # This file MUST be edited with the 'visudo' command as root.
    #
    ...
    ```

- `su`: Changes the current user.

    ```bash
    $ # Change user
    $ su student
    Password: 
    $ id
    uid=1003(student) gid=1004(student) groups=1004(student),1002(course)
    $ exit
    exit
    ```

- `useradd`: Creates a new user or updates default new user information.

    ```bash
    $ # Add user
    $ sudo useradd <user>
    ```

    ```bash
    $ # Add user and create home directory
    $ sudo useradd -m <user>
    ```

    ```bash
    $ # Add user and add to group
    $ sudo useradd -G <group> <user>
    ```

    ```bash
    $ # Add user add set shell
    $ sudo useradd -s /bin/bash <user>
    ```

    ```bash
    $ # Add user add set account expiration date
    $ sudo useradd -e 2025-01-01 <user>
    ```

- `userdel`: Deletes a user account and related files.

    ```bash
    $ # Delete user
    $ sudo userdel <user>
    ```

    ```bash
    $ # Delete user with their home directory and mail spool
    $ sudo userdel -r <user>
    ```

    ```bash
    $ # Delete user with their home directory and mail spool, but backup files
    $ sudo userdel --backup -r <user>
    ```

- `usermod`: Modifies a user account.

    ```bash
    $ # Rename user
    $ usermod -l <user> <new-user>
    ```

    ```bash
    $ # Add to group
    $ usermod -aG <group> <user>
    ```

    ```bash
    $ # Lock account
    $ usermod -L <user>
    ```

- `passwd`: Changes user password.

    ```bash
    $ # Changes password for current user (Ctrl+D to cancel)
    $ sudo passwd
    ```

    ```bash
    $ # Changes password for user
    $ sudo passwd <user>
    ```

    ```bash
    $ # Forces to change password at next login
    $ sudo passwd -e <user>
    ```

- `login`: Begins a session on the system.

    ```bash
    $ # Login
    $ login
    ```

    ```bash
    $ # Login as user
    $ sudo login <user>
    ```

    ```bash
    $ # Logout
    $ logout
    ```

- `adduser`, `newusers`: Interfaces for adding users.

    ```bash
    $ # Add user
    $ sudo adduser <user>
    ```

    ```bash
    $ # Add user(s) from file (username:password:UID:GID:User Info:/home/username:/bin/bash)
    $ sudo newusers < <(echo '<user>:<password>::<GID>:,,,:/home/<user>:/bin/bash')
    ```

- `chown`: Changes file owner and group.

    ```bash
    $ # Changes owner
    $ touch data.log
    $ ls -l data.log 
    -rw-rw-r-- 1 nstu nstu ...
    $ sudo chown student data.log 
    $ ls -l data.log 
    -rw-rw-r-- 1 student nstu ...
    ```

    ```bash
    $ # Changes owner and group
    $ sudo chown student:course data.log 
    $ ls -l data.log 
    -rw-rw-r-- 1 student course ...
    ```

- `chmod`: Changes file access permissions.

    ```bash
    $ # Adds execute permission for the user
    $ touch data.sh
    $ ls -l data.sh 
    -rw-rw-r-- 1 nstu nstu 0 ...
    $ chmod u+x data.sh 
    $ ls -l data.sh 
    -rwxrw-r-- 1 nstu nstu 0 ...
    ```

    ```bash
    $ # Recursivly remove write permision 
    $ mkdir -p backup/version-{1..5}/src
    $ tree -p backup/
    [drwxrwxr-x]  backup/
    ├── [drwxrwxr-x]  version-1
    │   └── [drwxrwxr-x]  src
    ├── [drwxrwxr-x]  version-2
    │   └── [drwxrwxr-x]  src
    ├── [drwxrwxr-x]  version-3
    │   └── [drwxrwxr-x]  src
    ├── [drwxrwxr-x]  version-4
    │   └── [drwxrwxr-x]  src
    └── [drwxrwxr-x]  version-5
        └── [drwxrwxr-x]  src
    $ chmod -R u-w backup/version-*
    $ tree -p backup/
    [drwxrwxr-x]  backup/
    ├── [dr-xrwxr-x]  version-1
    │   └── [dr-xrwxr-x]  src
    ├── [dr-xrwxr-x]  version-2
    │   └── [dr-xrwxr-x]  src
    ├── [dr-xrwxr-x]  version-3
    │   └── [dr-xrwxr-x]  src
    ├── [dr-xrwxr-x]  version-4
    │   └── [dr-xrwxr-x]  src
    └── [dr-xrwxr-x]  version-5
        └── [dr-xrwxr-x]  src
    $ rm -r  backup/version-1/src/
    rm: remove write-protected directory 'backup/version-1/src/'? y
    rm: cannot remove 'backup/version-1/src/': Permission denied
    $ sudo rm -r backup/
    ```

- `groups`: Displays the groups the current user is part of.

    ```bash
    $ # Current user groups
    $ groups
    nstu sudo vboxsf
    ```

    ```bash
    $ # User groups
    $ groups student
    student : student course
    ```

- `chgrp`: Changes the group ownership of a file.

    ```bash
    $ # Changes the group ownership
    $ sudo chgrp nstu data.log
    $ ls -l data.log 
    -rw-rw-r-- 1 student nstu ...
    ```

<!-- SECTION  -->
# Processes and jobs management
[Back to Top](#contents)

## Processes
[Back to Top](#contents)

Process is a running instance of a program. 
Each process is identified by a unique process ID (PID). 
Each running process on the system is represented by a directory in `/proc` named after its process ID (PID). 
For example, `/proc/1` contains information about the process with PID 1.

```bash
$ cd /proc/1
$ sudo ls
arch_status  cgroup      coredump_filter     environ  gid_map            limits     mem         net        oom_score      personality  schedstat  smaps_rollup  status          timers
attr         clear_refs  cpu_resctrl_groups  exe      io                 loginuid   mountinfo   ns         oom_score_adj  projid_map   sessionid  stack         syscall         timerslack_ns
autogroup    cmdline     cpuset              fd       ksm_merging_pages  map_files  mounts      numa_maps  pagemap        root         setgroups  stat          task            uid_map
auxv         comm        cwd                 fdinfo   ksm_stat           maps       mountstats  oom_adj    patch_state    sched        smaps      statm         timens_offsets  wchan
```

- `/proc/[PID]/cmdline`: Contains the full command line of the process
- `/proc/[PID]/exe`: A symlink to the executable of the process
- `/proc/[PID]/comm`: The filename of the command executed by the process
- `/proc/[PID]/status`: Status (ID, parent ID, ...) and state (running, sleeping, ...), memory usage, ...
- `/proc/[PID]/maps`: Shows the memory map of the process, including addresses of mapped files and memory regions
- `/proc/[PID]/smaps`: An extended version of maps with more detailed memory usage statistics
- `/proc/[PID]/mem`: The actual contents of the process's memory, which can be read at certain offsets
- `/proc/[PID]/io`: Information about the I/O operations of the process
- `/proc/[PID]/limits`: Shows the limit on the resources (like file size, CPU time, memory usage, etc.) that the process can consume
- `/proc/[PID]/oom_score`: The score that the kernel uses to determine which process to kill in an out-of-memory (OOM) situation
- `/proc/[PID]/fd`: A directory containing symbolic links to all the open file descriptors of the process, including files, sockets, pipes, etc
- `/proc/[PID]/fdinfo`: Detailed information on the file descriptors
- `/proc/[PID]/environ`: The environment variables for the process
- `/proc/[PID]/sched`: Scheduler information for the process
- `/proc/[PID]/stat`: Process status in a form that's easy for other programs to parse. It includes the process's uptime, number of threads, and other statistics
- `/proc/[PID]/net`: Network statistics and configuration specific to the process, if it has created a network namespace
- ...

A process in Linux can be in one of the following states:

- **Running (R)**: The process is either executing on a CPU or waiting to be executed as soon as the CPU becomes available.
- **Interruptible Sleep (S)**: This state indicates a process that is waiting for an event to complete or for a system resource to become available.
- **Uninterruptible Sleep (D)**: The process is waiting for I/O (disk, network, etc.) to complete and cannot be interrupted.
- **Stopped (T)**: The execution of the process has been stopped. This can be caused by receiving a signal like `SIGSTOP`.
- **Zombie (Z)**: The process has completed execution, but still has an entry in the process table. This is to allow the parent process to read its child's exit status.
- ...

Kernel and process interaction:

- **Process Scheduler**: 
The scheduler is responsible for allocating CPU time to various processes. 
The Linux kernel uses a Completely Fair Scheduler (CFS) by default, which aims to provide a fair amount of CPU time to each process based on its priority and execution history.

- **Process Creation**: 
Processes are created using the `fork()` or `clone()` system calls, which create a new process by duplicating an existing one. 
The `exec()` system call can then be used to replace the forked process's image with a new program.

- **Process Termination**: 
A process terminates either voluntarily by calling `exit()` or by being killed by another process via a signal (e.g., `SIGKILL`).

- **Inter-Process Communication (IPC)**: 
Linux provides several mechanisms for IPC, including pipes, message queues, shared memory, and semaphores, allowing processes to communicate and synchronize with each other.

- **Process Hierarchies and Orphan Processes**: 
Each process, except the initial system process (init or systemd), is created by another process (its parent). 
If a parent process terminates before its children, the children become orphan processes and are adopted by the init/systemd process.

- **Signals**: 
Signals are a form of inter-process communication that are used to notify a process that a specific event has occurred. 
They can be used to instruct a process to stop, continue, terminate, etc.

- **Process Control Groups (cgroups)**: 
This is a kernel feature that allows the OS to organize processes into hierarchical groups to provide resource management and limiting.

- **Namespaces**: 
Namespaces are another feature that the kernel provides for isolating and virtualizing system resources among different processes. 
For example, PID namespaces isolate the process ID number space, meaning that processes in different PID namespaces can have the same PID.

## Jobs
[Back to Top](#contents)

One or multiple processes that are initiated from the same shell or terminal session and can be managed as a single unit.
`jobs` command lists all jobs current jobs.

- Jobs can be stopped, started, and managed directly from the shell using job control commands.
- Jobs are assigned job IDs within the shell, which are different from PIDs.
- Jobs can also be run in the foreground or background of the terminal.

## Relevant commands and examples
[Back to Top](#contents)

- `top` (`htop`): Displays Linux tasks and system status.

    ```bash
    $ # Show user processes
    $ top -u nstu
    ```

    ```bash
    $ # Monitor process by PID
    $ top -p 1
    ```

- `ps`: Displays information about active processes.

    ```bash
    $ # Show user processes
    $ ps -u nstu
    ```

    ```bash
    $ # Displays a process tree (terminal session)
    $ ps --forest
    ```

    ```bash
    $ #  Shows information about PID
    $ ps -p 1
    ```

    ```bash
    $ # Show all running with detailed info
    $ ps -aux
    ```

- `pidof`: Gets the ID of a process using its name (also see `pgrep`).

    ```bash
    $ pidof bash
    ```

- `pstree`: Displays a tree of processes.

    ```bash
    $ #  Shows tree for PID
    $ pstree 1
    ```

    ```bash
    $ # Current shell session tree (with PIDs, owner)
    $ pstree -pu $$
    ```

    ```bash
    $ # User tree
    $ pstree nstu
    ```

- `kill`: Sends a signal to a process, often used to end processes.

    ```bash
    $ # Kill process with pid (gently)
    $ kill -SIGTERM <PID>
    ```

    ```bash
    $ # Kill process with pid (forcefully)
    $ kill -SIGKILL <PID>
    ```

    ```bash
    $ # List signals
    $ kill -l
    ```

- `killall`: Kills processes by name.

    ```bash
    $ # Kill by name
    $ killall <name>
    ```

    ```bash
    $ # Kill by user (forcefully)
    $ killall -u <user> -SIGKILL
    ```

- `time`: Run programs and summarize system resource usage.

    ```bash
    $ # Measures execution time
    $ time sleep 1

    real    0m1.005s
    user    0m0.001s
    sys     0m0.004s
    ```

- `nice` (`renice`): Changes process priority.

    - Priority range -20 to 19 (highest to lowest), default priority of user processes is 0
    - Kernel's scheduler decides which process to run next based on these priority values
    - The `nice` command in Linux is used to start a process with a modified scheduling priority
    - When you run a command with `nice`, you can specify the 'niceness' level (value added to the priority of the process)
    - The `renice` command is used to change the priority of an already running process

    ```bash
    $ # Run with (lower) priority
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

- `fg`: Brings a job to the foreground (use `Ctrl+Z` to stop).

    ```bash
    $ # Bring the most recent background job to the foreground
    $ # Press Crtl+C to cancel sleep
    $ sleep 100 &
    $ fg
    sleep 100
    ^C
    ```

    ```bash
    $ # By ID (can do several)
    $ # Press Crtl+C to cancel sleep
    $ sleep 100 &
    $ fg 1
    sleep 100
    ^C
    ```

    ```bash
    $ # By name (can do several)
    $ # Press Crtl+C to cancel sleep
    $ fg "%sleep" 
    sleep 100
    ^C
    ```

- `bg`: Resumes a job in the background.

    ```bash
    $ # Resumes the most recent job in the background
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
    $ # By ID (can do several)
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
    $ # By name (can do several)
    $ sleep 100
    ^Z
    [1]+  Stopped                 sleep 100
    $ bg "%sleep"
    [1]+ sleep 100 &
    $ fg
    sleep 100
    ^C
    ```

- `jobs`: Lists the jobs currently running or stopped.

    ```bash
    $ #  Lists all current jobs with PIDs
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

- `at`: Executes commands at a specified time.

     ```bash
     $ # Executes at selected time, e.g. HH:MM [AM/PM] MM DD
     $ # Enter commnd(s) and press `Ctrl + D`
     $ at now + 1 hour
     ```

     ```bash
     $ # Display  the queue of scheduled jobs
     $ atq
     ```

     ```bash
     $ # Remove a job from queue
     $ atrm 1
     ```

     ```bash
     $ # Executes when he system load levels drop to a certain level
     $ # Enter commnd(s) and press `Ctrl + D`
     $ batch
     ```

- `crontab`: Schedules periodic background jobs (use [crontab guru](https://crontab.guru/)).

    ```bash
    $ # Edits the current user's crontab
    $ crontab -e
    ```

    ```bash
    $ # Lists the current user's crontab
    $ crontab -l
    ```

    ```bash
    $ # Removes the current user's crontab
    $ crontab -r
    ```

<!-- SECTION  -->
# System monitoring
[Back to Top](#contents)

## Resources
[Back to Top](#contents)

- **Process Management**: `ps`, `top`, `htop`, `pstree`
- **CPU Usage**: `top`, `htop`
- **Memory Usage**: `free`, `vmstat`, `top`, `htop`
- **Disk Usage**: `df` (`df -i` inodes), `du`, `iotop`, `iostat`
- **System Load**: `uptime`, `w`, `top`, `htop`
- **I/O Statistics**: `iostat`, `iotop`
- **Network Traffic and Statistics**: `netstat`, `ifconfig`, `ip`, `nload`, `iftop`, `ss`
- **Swap Usage**: `swapon`, `swapoff`, `vmstat`, `free`
- **Services**: `systemctl` (see the next section)
- **Logs**: `journalctl`


## Services
[Back to Top](#contents)

Services (daemons) are applications or programs that run in the background and perform system functions or provide various services to users and other programs. 
In Ubunty servises and system init are managed `systemd`. 
Services are defined by unit files. Unit files describe how to manage a service (start, stop, ...).

Basic service management:

- **Start**: `sudo systemctl start [service_name]`
- **Stop**: `sudo systemctl stop [service_name]`
- **Restart**: `sudo systemctl restart [service_name]`
- **Enable**: `sudo systemctl enable [service_name]` (start on boot)
- **Disable**: `sudo systemctl disable [service_name]` (do not start on boot)
- **Status**: `sudo systemctl status [service_name]`
- **Reload Systemd**: `sudo systemctl daemon-reload` (on modifications of service files)
- **Listing**: `systemctl list-units --type=service`
- **Journaling**: `journalctl`

## Relevant commands and examples
[Back to Top](#contents)

- `watch`: Executes a program periodically, showing output fullscreen.

    ```bash
    $ # Rerun command every second
    $ watch -n 1 ls -l
    ```

    ```bash
    $ # Highlight differences as they appear
    $ watch -n 1 -d ls -l
    ```

- `mount` (`umount`): Mount unmount file systems (you might need to add USB in VM settings).

    ```bash
    $ # Mount (usb device sda1)
    $ sudo mount /dev/sda1 /mnt
    $ cd /mnt
    $ ls
    ```

    ```bash
    $ # Unmout
    $ sudo umount /mnt`
    ```

    ```bash
    $ # Mount to specific directory and unmount 
    $ sudo mkdir /media/$USER/usb
    $ sudo mount /dev/sda1 /media/$USER/usb
    $ sudo umount /dev/sda1
    $ sudo rmdir /media/$USER/usb
    ```

- `udisksctl`: Command-line utility used for interacting with the UDisks daemon (you might need to add USB in VM settings).

    ```bash
    $ # Check status
    $ udisksctl status
    ```

    ```bash
    $ # Mount
    $ udisksctl mount -b /dev/sda1
    ```

    ```bash
    $ # Get info
    $ udisksctl info -b /dev/sda1
    ```

    ```bash
    $ # Unmount
    $ udisksctl unmount -b /dev/sda1
    ```

- `uname`: Shows system information.

    ```bash
    $ # Displays all system information
    $ uname -a
    Linux nstu 6.5.0-15-generic #15~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Fri Jan 12 18:54:30 UTC 2 x86_64 x86_64 x86_64 GNU/Linux
    ```

- `lsb_release`: Show distribution information.

    ```bash
    $ # Show all distribution information
    $ lsb_release -a
    No LSB modules are available.
    Distributor ID: Ubuntu
    Description:    Ubuntu 22.04.3 LTS
    Release:        22.04
    Codename:       jammy
    ```

- `id` (`whoami`): Displays user and group IDs.

    ```bash
    $ # Current user information
    $ id
    uid=1000(nstu) gid=1000(nstu) groups=1000(nstu),27(sudo),999(vboxsf)
    ```

    ```bash
    $ # Specific user information
    $ id student
    uid=1003(student) gid=1004(student) groups=1004(student),1002(course)
    ```

- `w`: Shows who is logged on and what they are doing.

    ```bash
    $ # Displays who is logged on and what they are doing
    $ w
    $ w
    ...
    USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
    nstu     pts/0    10.0.2.2         11:51    0.00s  0.00s  0.00s w
    ```

    ```bash
    $ # Shows information about specific user
    $ w student
    ...
    ```

- `uptime`: Displays how long the system has been running and load averages (also top line of `w`).

    ```bash
    $ uptime
    ```

- `df`: Reports file system disk space usage.

    ```bash
    $ # Shows disk space usage
    $ df -h
    ```

- `du`: Estimates file space usage.

    ```bash
    $ # Shows directory space usage
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
    $ # Displays the total size of a directory
    $ du -sh /usr/bin
    203M    /usr/bin 
    ```

    ```bash
    $ #  Lists sizes for all files and directories
    $ du -ah /usr/bin
    ...
    32K     /usr/bin/usbhid-dump
    108K    /usr/bin/pdftohtml
    24K     /usr/bin/openvt
    40K     /usr/bin/id
    12K     /usr/bin/piconv
    203M    /usr/bin  
    ```

- `htop`: Similar to `top`, but with an enhanced, interactive interface (`sudo apt install htop`).

    ```bash
    $ # Shows processes for a specific user
    $ htop -u nstu
    ```

    ```bash
    $ # Monitors specific processes by their process ID
    $ htop -p 1
    ```

- `vmstat`: Reports virtual memory statistics.

    ```bash
    $ vmstat
    ```

- `free`: Displays amount of free and used memory in the system.

    ```bash
    $ free -h
    ```

- `iostat`: Reports CPU statistics and input/output statistics for devices and partitions.

    ```bash
    $ #  Shows CPU and I/O statistics 
    $ iostat
    ```

    ```bash
    $ #  Shows CPU
    $ iostat -c
    ```

- `nethogs`: Display network usage per process (`sudo apt install nethogs`).

    ```bash
    $ # Display network usage
    $ sudo nethogs
    ```

<!-- SECTION  -->
# Networking
[Back to Top](#contents)


## Networking components
[Back to Top](#contents)

 - **Networking Hardware:**
   - Routers, switches, network interface cards, and other devices.

- **Networking Models:**
   - The OSI Model: Physical, Data Link, Network, Transport, Session, Presentation, and Application.
   - The TCP/IP Model: Link, Internet, Transport, and Application.

- **IP Addressing:**
   - Every device on a network has an IP address.
   - There are IPv4 and IPv6 addresses, and understanding subnetting is crucial for designing and troubleshooting networks.

- **Network Protocols:**
   - Protocols such as TCP, UDP, ICMP, and others are the rules and standards that dictate network communication.

- **Network Services:**
   - Services like DNS (Domain Name System), DHCP (Dynamic Host Configuration Protocol), and others are essential for network functionality.

- **Network Configuration:**
   - Network manager CLI `nmcli`.
   - Static IP or dynamic a DHCP server.

- **Firewall Configuration:**
   - `iptables` is a tool for setting up rules to allow or block traffic (or `nftables`).
   - `ufw` firewall provides interfaces for managing `iptables`.

- **Routing and Switching:**
   - Understanding how data is routed through a network using routing tables (`route` or `ip route` commands).
   - Linux can be configured to act as a router, passing traffic between different networks.

- **Network Troubleshooting:**
   - Commands like `ping`, `traceroute`, `netstat`, `ss`, `dig`, `nslookup`, and `tcpdump`.

- **Network Security:**
    - SSH for secure remote access.
    - Understanding the basics of network encryption, like TLS/SSL.
    - Knowledge of authentication mechanisms like keys and certificates.

- **Network File Systems:**
    - NFS and Samba for sharing files over a network.

- **Network Monitoring and Management:**
    - Tools like Nagios, Zabbix, or Prometheus for network monitoring.
    - SNMP (Simple Network Management Protocol) for network management.

- **Virtual Networking:**
    - Understanding virtual networks, bridges, and tunnels (like VPNs).
    - Tools like `virt-manager` for virtual machine networking.

- **Container Networking:**
    - With the rise of containerization with tools like Docker and Kubernetes, understanding how networking works within and between containers is also vital.

## Networking tasks
[Back to Top](#contents)

- **Checking Network Configuration:**
   - `ip addr`: Display the current network configuration, including IP addresses, subnet masks, and network interfaces.
   - `hostname`: View or set the host name.

- **Managing Network Connections:**
   - `nmcli`: A command-line tool for controlling NetworkManager, useful for setting up and managing network connections.
   - `nmtui`: A text-user interface (TUI) for NetworkManager, providing a more user-friendly way to manage network settings.

- **Diagnosing Network Issues:**
   - `ping`: Check the connectivity to another network host.
   - `traceroute` or `tracepath`: Trace the route packets take to a network host, helping to diagnose where a connection gets slow or breaks.
   - ``ss``: Display network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.

- **Analyzing Network Traffic:**
   - `tcpdump`: A powerful command-line packet analyzer; useful for network debugging and traffic monitoring.
   - `wireshark` (TShark for terminal): Network protocol analyzer that can be used for deep inspection of hundreds of protocols.

- **Configuring Network Services:**
   - `iptables` or `nftables`: Command-line tools for setting up, maintaining, and inspecting the tables of IP packet filter rules in the Linux kernel.

- **Testing Network Performance:**
   - `speedtest-cli`: A command-line interface for testing internet bandwidth using speedtest.net.
   - `iperf`: Tool to measure the maximum achievable bandwidth on IP networks.

- **Scanning Networks and Ports:**
   - `nmap`: Network exploration tool and security / port scanner.

- **Managing DNS and Domain Information:**
   - `dig`: Query DNS name servers for information about host addresses, mail exchanges, name servers, and related information.
   - `nslookup`: Query Internet domain name servers.

- **Automating Network Tasks:**
   - `ssh`: Securely connect to remote servers for command execution.
   - `scp` or `rsync`: Securely copy files between hosts on a network.

- **Monitoring Network Usage and Bandwidth:**
    - `iftop` or `nload`: Display bandwidth usage on an interface.
    - `vnstat`: Monitor network traffic and bandwidth usage in real time.

## Relevant commands and examples
[Back to Top](#contents)

- `ping`: Checks the network connection to a server.

    ```bash
    $ # Check connectivity to hostname/ip/domain
    $ ping nstu  
    ```

    ```bash
    $ # Sends 10 requests with 1 second interval
    $ ping -c 10 -i 1 nstu  
    ```

- `host`: Performs DNS lookups, translating domain names to IP addresses and vice versa.

    ```bash
    $ host 8.8.8.8
    8.8.8.8.in-addr.arpa domain name pointer dns.google.
    ```

- `hostname`: View or set the system's hostname.

    ```bash
    $ # Display the current system hostname
    $ hostname
    ```

    ```bash
    $ # Change the system hostname
    $ hostname <name>
    ```

- `ssh`: Secure Shell, a protocol to securely access remote machines.

    ```bash
    $ # Connects to <host> as <user>
    $ ssh <user>@<host>
    ```

    ```bash
    $ # Connects on specific port
    $ ssh -p <port> <user>@<host>
    ```

    ```bash
    $ # Connects using a key
    $ ssh -i <path> <user>@<host>
    ```

    ```bash
    $ # Connects with X forwarding
    $ ssh -X <path> <user>@<host>
    ```

    ```bash
    $ # Connects with local port forwarding
    $ ssh -L <local_port>:<destination_address>:<destination_port> <user>@<host>
    ```

- `scp`: Securely copy files between hosts on a network.

    ```bash
    $ # Copies to the remote host
    $ scp <path>/<file> <user>@host:/<path>
    ```

    ```bash
    $ # Copies from the remote host
    $ scp  <user>@host:/<path>/<file> <path>
    ```

    ```bash
    $ # Recursively copies a directory to the remote host
    $ scp -r <directory> <user>@host:/<path>
    ```