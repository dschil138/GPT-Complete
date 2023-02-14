from config import *
from functions import *
import pynput
import api_key 

if (hotkey == 1):
    combination = [pynput.keyboard.Key.ctrl_r, pynput.keyboard.Key.alt_l]

elif(hotkey == 2):
    combination = [pynput.keyboard.Key.ctrl, pynput.keyboard.KeyCode.from_char('0')]

elif(hotkey == 3):
    combination = [pynput.keyboard.Key.cmd, pynput.keyboard.Key.enter]

current = set()

def main_function():
    current.clear()
    user_input = select_input()
    print('sending to API')
    botResponse = send_to_bot(model, user_input, creativity, max_tokens)
    paste_response(botResponse)

def on_press(key):
    current.add(key)
    if all(k in current for k in combination):
        pag.sleep(0.2)
        main_function()

def on_release(key):
    if key in current:
        current.remove(key)

while True:

    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()



