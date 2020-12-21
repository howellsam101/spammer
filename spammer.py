#spammer for all laptops/PCs running python.
#requires the pynput python extension to be installed.


import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from pynput.keyboard import Key, Controller

print("the program is live!")
print("to start/stop press 2") #make sure any of these values are not going to be pressed
print("to exit press 1")

keyboard = Controller()
delay = 0.8
button = Button.left
start_stop = KeyCode(char='2')
exit = KeyCode(char='1')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
        
    def start_clicking(self):
        self.running = True
    def stop_clicking(self):
        self.running = False
    def exit(self):
        self.stop_clicking()
        self.program_running = False
    def run(self):
        while self.program_running:
            while self.running:
                keyboard.type("type message here")
                #keyboard.press('h') #alternative to keyboard.type is to press each key
                #keyboard.press('e')
                #keyboard.press('l')
                #keyboard.press('l')
                #keyboard.press('0')
                keyboard.press(Key.space)
                keyboard.release(Key.space)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(self.delay)
                
mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    if key == start_stop:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()

    

