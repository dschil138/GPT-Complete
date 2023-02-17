from config import *
from functions import *
import pynput
import api_key 

if (hotkey1 == 1):
    combination1 = [pynput.keyboard.Key.ctrl_r, pynput.keyboard.Key.alt_l]

elif(hotkey1 == 2):
    combination1 = [pynput.keyboard.Key.ctrl, pynput.keyboard.KeyCode.from_char('0')]

elif(hotkey1 == 3):
    combination1 = [pynput.keyboard.Key.cmd, pynput.keyboard.Key.enter]

elif(hotkey1 == 4):
    combination1 = [pynput.keyboard.Key.cmd, pynput.keyboard.Key.shift, pynput.keyboard.KeyCode.from_char('k')]

if (hotkey2 == 1):
    combination2 = [pynput.keyboard.Key.ctrl_r, pynput.keyboard.Key.alt_l]

elif(hotkey2 == 2):
    combination2 = [pynput.keyboard.Key.ctrl, pynput.keyboard.KeyCode.from_char('0')]

elif(hotkey2 == 3):
    combination2 = [pynput.keyboard.Key.cmd, pynput.keyboard.Key.enter]

elif(hotkey2 == 4):
    combination2 = [pynput.keyboard.Key.cmd, pynput.keyboard.Key.shift, pynput.keyboard.KeyCode.from_char('k')]



current = set()

def main_function(chosenModel):
    current.clear()
    user_input = select_input()
    print('sending to API')
    botResponse = send_to_bot(chosenModel, user_input)
    paste_response(botResponse)

def on_press(key):
    current.add(key)
    if all(k in current for k in combination1):
        pag.sleep(0.2)
        main_function(model1)
    if all(k in current for k in combination2):
        pag.sleep(0.2)
        main_function(model2)
def on_release(key):
    if key in current:
        current.remove(key)

while True:

    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()