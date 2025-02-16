from pynput import keyboard
from pynput.keyboard import Key, KeyCode
import time


class TelloControls:

    def __init__(self, tello):
        self.tello = tello
        self.key_listner = None

        # Controls default vairables
        self.move_distance = 20
        self.rotate_angle = 30

    def on_press(self, key: Key | KeyCode | None) -> None:
        if key == KeyCode.from_char('\x1a'):
            print("Special key '\x1a' pressed")
            if self.key_listner:
                self.key_listner.stop()
            return None
        print("Clicked key: ", key)
        key_pressed = self.switch(key)
        return key_pressed

    def on_release(self, key: Key | KeyCode | None) -> None:
        return key

    def switch(self, key):
        try:
            match key:
                case Key.up:
                    self.tello.move_forward(self.move_distance)
                    return key
                case Key.down:
                    self.tello.move_down(self.move_distance)
                    return key
                case Key.left:
                    self.tello.move_left(self.move_distance)
                    return key
                case Key.right:
                    self.tello.move_right(self.move_distance)
                    return key
                case Key.space:
                    self.tello.takeoff()
                    return key
                case Key.enter:
                    self.tello.land()
                    return key
                case Key.shift:
                    self.tello.rotate_clockwise(self.rotate_angle)
                    return key
                case Key.ctrl:
                    self.tello.rotate_counter_clockwise(self.rotate_angle)
                    return key
                case Key.esc:
                    self.tello.quit()
                    return key
        except Exception as e:
            print(e)
