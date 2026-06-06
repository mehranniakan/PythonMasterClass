from pynput import keyboard

def shortcut1_onclick():
    print('shortcut1 onclick')

def shortcut2_onclick():
    print('shortcut2 onclick')

def shortcut3_onclick():
    print('shortcut1 onclick')


with keyboard.GlobalHotKeys({
    '<ctrl>+<alt>+d': shortcut1_onclick,
    '<ctrl>+<alt>+s': shortcut2_onclick,
    '<ctrl>+<alt>+a': shortcut3_onclick,
}) as listener:
    listener.join()