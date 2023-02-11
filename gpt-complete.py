from config import *
from functions import *
import pynput
import api_key 


while True:

    combination = [pynput.keyboard.Key.cmd, pynput.keyboard.Key.enter]
    current = set()

    def do_the_thing():
        current.clear()
        userInput = select_input()
        print('doing the thing')
        botResponse = sendToBot(userInput, creativity, maxTokens)
        paste_response(botResponse)
        current.clear()

    def on_press(key):
        current.add(key)
        if all(k in current for k in combination):
            do_the_thing()

    def on_release(key):
        if key in current:
            current.remove(key)

    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()



