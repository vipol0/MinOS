from interface import ok, warning, error, init_colorama
import filesystem
import commands

def main():
    init_colorama()
    commands.clear()
    print("=== MinOS ===")
    
    while True:
        command = input(filesystem.get_promt() + "> ")
        parts = command.split()

        match parts[0]:
            case "help":
                commands.help()
            case "ls":
                commands.ls(parts)
            case "cd":
                commands.cd(parts)
            case "cat":
                commands.cat(parts)
            case "notepad":
                commands.notepad(parts)
            case "dir":
                commands.dir(parts)
            case "rm":
                commands.rm(parts)
            case "clear":
                commands.clear()
            case "exit":
                commands.exit(parts)
            case _:
                error(f"Unknown command: {command}. Type 'help' for a list of commands.")
                continue

        

if __name__ == "__main__":
    main()