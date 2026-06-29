# MinOS

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Status](https://img.shields.io/badge/Status-Alpha-orange)
![Platform](https://img.shields.io/badge/Platform-Terminal-lightgrey)

A simple terminal-based operating system simulator written in Python.

## About

MinOS is a lightweight educational project that simulates a basic operating system shell. It includes a virtual file system, command interpreter, text editor, directory navigation, and file management tools.

The project is designed for learning Python fundamentals, command-line interfaces, and filesystem concepts.

## Features

* Virtual file system stored in memory
* Directory navigation (`cd`)
* View directory contents (`ls`)
* Read files (`cat`)
* Create directories (`mkdir`)
* Delete files and folders (`rm`)
* Built-in text editor (`notepad`)
* Colored output messages using Colorama
* Terminal clear command (`clear`)
* Interactive shell prompt

## Available Commands

| Command          | Description                    |
| ---------------- | ------------------------------ |
| `help`           | Show help menu                 |
| `ls`             | List directory contents        |
| `cd <path>`      | Change directory               |
| `cat <file>`     | Read file contents             |
| `notepad <file>` | Open text editor and save text |
| `mkdir <folder>` | Create a folder                |
| `rm <file>`      | Delete a file or folder        |
| `clear`          | Clear terminal screen          |
| `exit`           | Exit MinOS                     |

## Installation

1. Clone the repository:

```bash
git clone https://github.com/vipol0/MinOS.git
cd MinOS
```

2. Install dependencies:

```bash
pip install colorama
```

3. Run MinOS:

```bash
python main.py
```

## Example

```text
=== MinOS ===

/> ls
home
system

/> cd home

/home> ls
notes.txt

/home> cat notes.txt
Hello word!

/home> mkdir projects
[OK] Folder created
```

## Technologies

* Python 3
* Colorama

## Future Plans

* File permissions
* Copy and move commands
* Save filesystem to disk
* Improving the notepad

## License

This project is open source and available under the MIT License.
