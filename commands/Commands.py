def Open():
    return 'command open invoked'


def New():
    return 'command new invoked'


def Save():
    return 'command save invoked'


def execute(command: str):
    if command == 'open':
        return Open()
    elif command == 'new':
        return New()
    elif command == 'save':
        return Save()

