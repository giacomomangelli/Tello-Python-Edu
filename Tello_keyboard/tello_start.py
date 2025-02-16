from pynput.keyboard import KeyCode

from tello_core import Tello
from datetime import datetime
import time
import tello_controls as Controls
from pynput import keyboard

start_time = str(datetime.now())

listener_running = True

tello = Tello('', 8889)
tello_controls = Controls.TelloControls(tello)


def on_press(key):
    try:
        tello_controls.on_press(key)
    except Exception as e:
        print(f"Error on press: {e}")


def on_release(key):
    try:
        tello_controls.on_release(key)
        if key == KeyCode.from_char('\x1a'):
            global listener_running
            listener_running = False
    except Exception as e:
        print(f"Error on release: {e}")


while True:
    try:
        # print('Waiting Input...')
        # Keyboard listener
        tello_controls.key_listner = keyboard.Listener(on_press=on_press, on_release=on_release)
        tello_controls.key_listner.start()

        while listener_running:
            time.sleep(0.1)

        tello_controls.key_listner.join()
        print('Listener stopped')
        break

    except Exception as e:
        print(e)
        print('Trying to reconnect...')
        time.sleep(3)
