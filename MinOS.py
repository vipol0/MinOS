import os
from colorama import init, Fore, Style

disk = {
    "/": {
        "home": {
            "notes.txt": ""
        },
        "system": { }
    }
}

current_path = ["/"]

def ok(msg: str) -> None:
    print(Fore.GREEN + "[OK] " + msg)

def warning(msg: str) -> None:
    print(Fore.YELLOW + "[WARNING]" + msg)

def erorr(msg: str) -> None:
    print(Fore.RED + "[ERORR]" + msg)

def get_current_dir():
    current = disk

    for folder in current_path:
        current = current[folder]

    return current

def resolve_path(path: str):
    if path.startswith("/"):
        current = disk["/"]
        parts = path.split("/")[1:]
    else:
        current = get_current_dir()
        parts = path.split("/")

    for part in parts:
        if part == "" or part == ".":
            continue
        if part == "..":
            return None  # позже можно улучшить
        if part not in current:
            return None
        current = current[part]

    return current

def get_prompt():
    if current_path == ["/"]:
        return "/"

    return "/" + "/".join(current_path[1:])

def normalize_path(parts):
    stack = []

    for part in parts:
        if part == "" or part == ".":
            continue

        if part == "..":
            if len(stack) > 1:
                stack.pop()
        else:
            stack.append(part)

    if not stack:
        return ["/"]

    return stack

def cd(parts):
    if len(parts) != 2:
        erorr("Usage: cd <path>")
        return

    path = parts[1]

    parts_path = path.split("/")

    if path.startswith("/"):
        new_path = ["/"] + [p for p in parts_path if p]
    else:
        new_path = current_path + parts_path

    current_path[:] = normalize_path(new_path)

def ls(parts) -> None:
    if len(parts) > 1:
        erorr("Usage: ls")
        return
    
    current_dir = get_current_dir()
    for file in current_dir.keys():
        print(file)

def pwd() -> None:
    print(get_prompt())

def cat(parts) -> None:
    if len(parts) != 2:
        erorr("Usage: cat <file>")
        return
    
    path = parts[1]
    target = resolve_path(path)

    if target is None:
        erorr("File not found")
        return

    if isinstance(target, dict):
        erorr("It's a directory")
        return

    print(target)

def help_menu(parts) -> None:
    if len(parts) > 1:
        erorr("Usage: help")
        return

    print("Available commands:")
    print("help - Show this help menu.")
    print("ls - List files in the current directory.")
    print("pwd - Show current path.")
    print("cd - Move through directories.")
    print("cat <filename> - Display the contents of a file.")
    print("cr <name> -  create a new file/folder.")
    print("wr <filename> <notes> - Write to a file.")
    print("rm <name> - Delete the file/folder.")
    print("clear - clear console.")
    print("exit - Exit the MinOS.")

def create_file(parts) -> None:
    if len(parts) != 2:
        erorr("Usage: cr <file>")
        return

    file = parts[1]
    current_dir = get_current_dir()

    if file in current_dir:
        erorr("Already exists")
        return

    if "." not in file:
        current_dir[file] = {}
        ok("Folder created.")
        return
    
    current_dir[file] = ""
    ok("File created.")

def write_file(parts) -> None:
    if len(parts) < 3:
        erorr("Usage: wr <file> <text>")
        return
    
    file = parts[1]
    notes = " ".join(parts[2:])
    current_dir = get_current_dir()

    if file not in current_dir:
        erorr("File not found")
        return
    
    if isinstance(current_dir[file], dict):
        erorr("It's a directory")
        return
    
    current_dir[file] = notes
    ok("File was successfully write.")

def remove_file(parts) -> None:
    if len(parts) != 2:
        erorr("Usage: rm <file>")
        return
    
    current_dir = get_current_dir()
    file = parts[1]

    if file not in current_dir:
        erorr(f"File not found: {parts[1]}")

    warning_ = input(Fore.YELLOW + f"[WARNING] Are you sure you want to delete {file}? (yes/no): ")

    if warning_ == "yes":
        current_dir.pop(file, None)
        ok("File was successfully deleted.") 
    else:
        return

def clear(parts):
    if len(parts) > 1:
        erorr("Usage: clear")
        return

    os.system("cls" if os.name == "nt" else "clear")

def exit_os() -> bool:
    warning_ = input(Fore.YELLOW + "[WARNING] Are you sure you want to log out? (yes/no): ")

    if warning_ == "yes":
        print("Goodbye!")
        return True
    else:
        return False

def main() -> None:
    init(autoreset=True)
    print("MinOS")

    while True:
        cmd = input(get_prompt() + "> ")
        parts = cmd.split()

        if not parts:
            continue

        match parts[0]:
            case "help":
                help_menu(parts)
            case "ls":
                ls(parts)
            case "pwd":
                pwd()
            case "cat":
                cat(parts)
            case "cr":
                create_file(parts)
            case "wr":
                write_file(parts)
            case "rm":
                remove_file(parts)
            case "cd":
                cd(parts)
            case "clear":
                clear(parts)
            case "exit":
                if exit_os() == True:
                    break
            case _:
                erorr(f"Unknown command: {cmd}. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()