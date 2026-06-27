import os
import sys
from interface import ok, warning, warning_press, error
from filesystem import get_current_dir, normalize_path, path_exist, resolve_path, resolve_parent, current_path, disk

def help():
    print("-----")
    print("help - Show this help menu")
    print("ls - View the contents of the folder")
    print("cd <folder> - Navigating through folders")
    print("cat <file> - Read a file")
    print("notepad <file> - Open text editor")
    print("dir <name> - Сreate a folder")
    print("rm <name> - Delete the file")
    print("clear - Clear the terminal")
    print("exit - Exit the terminal")
    print("-----")

def ls(parts):
    if len(parts) != 1:
        error("Usage: ls")
        return
    
    current_dir = get_current_dir()

    if not current_dir:
        return

    for file in current_dir.keys():
        print(file)

def cd(parts):
    if len(parts) != 2:
        error("Usage: cd <path>")
        return

    path = parts[1]

    parts_path = path.split("/")

    if path.startswith("/"):
        new_path = ["/"] + [p for p in parts_path if p]
    else:
        new_path = current_path + parts_path

    new_path = normalize_path(new_path)

    if not path_exist(new_path):
        error("Folder not found")
        return

    current_path[:] = new_path

def cat(parts):
    if len(parts) != 2:
        error("Usage: cat <file>")
        return

    path = parts[1]
    target = resolve_path(path)

    if target is None:
        error("File not found")
        return

    if isinstance(target, dict):
        error("It's a directory")
        return

    print(target)

def notepad(parts):
    if len(parts) != 2:
        error("Usage: notepad <file>")
        return

    path = parts[1]

    print("=== NOTEPAD ===")
    print("Type your text. Use ':wq' to save and exit.")
    print("----------------------")

    lines = []

    while True:
        line = input()

        if line == ":wq":
            break

        lines.append(line)

    text = "\n".join(lines)

    parent, name = resolve_parent(path)

    if parent is None:
        error("Invalid path")
        return

    parent[name] = text

    ok("File saved")

def dir(parts):
    if len(parts) != 2:
        error("Usage: dir <folder>")
        return
    
    file = parts[1]
    current_dir = get_current_dir()

    if file in current_dir:
        error("Folder already exists")
        return

    if str(file).endswith(".txt"):
        error("Use note to create files")
        return
    
    if "/" in file:
        error("symbol '/' prohibited")
        return

    current_dir[file] = {}
    ok("Folder created")

def rm(parts):
    if len(parts) != 2:
        error("Usage: rm <file>")
        return

    path = parts[1]

    parent, name = resolve_parent(path)

    if parent is None or name is None:
        error("File not found")
        return

    if name not in parent:
        error("File not found")
        return

    if warning_press(f"Delete {path}? (yes/no): "):
        del parent[name]
        ok("File was successfully deleted")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def exit(parts):
    if len(parts) != 1:
        error("Usage: exit")
        return
    
    if warning_press("Do you want to leave? (yes/no) ") == True:
        print("Godbye!")
        sys.exit()
    else:
        return