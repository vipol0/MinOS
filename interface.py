from colorama import init, Fore, Style

def init_colorama():
    init(autoreset=True)

def ok(msg: str):
    print(Fore.GREEN + "[OK] " + msg)

def warning(msg: str):
    print(Fore.YELLOW + "[WARNING] " + msg)

def warning_press(msg: str) -> bool:
    warning_ = input(Fore.YELLOW + "[WARNING] " + msg)

    if warning_ == "yes":
        return True
    else:
        return False

def error(msg: str):
    print(Fore.RED + "[ERROR] " + msg)