disk = {
    "/": {
        "home": {
            "notes.txt": "Hello word!"
        },
        "system": { }
    }
}

current_path = ["/"]

def get_current_dir():
    current = disk

    for folder in current_path:
        current = current[folder]

    return current

def get_promt():
    if current_path == ["/"]:
        return "/"

    return "/" + "/".join(current_path[1:])

def path_exist(path_parts):
    current = disk

    for part in path_parts:
        if part not in current:
            return False
        
        current = current[part]

        if not isinstance(current, dict):
            return False
        
    return True

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
            return None
        if part not in current:
            return None
        current = current[part]

    return current

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

def resolve_parent(path: str):
    if path.startswith("/"):
        parts = path.strip("/").split("/")
        current = disk["/"]
    else:
        parts = (current_path + path.split("/"))
        parts = normalize_path(parts)
        current = get_current_dir()
        parts = parts[len(current_path):]

    if not parts:
        return None, None

    filename = parts[-1]
    dirs = parts[:-1]

    for d in dirs:
        if d not in current:
            return None, None
        current = current[d]

    return current, filename