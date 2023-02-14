from config import *
from functions import *
import pynput
import api_key 


while True:

    combination = [pynput.keyboard.Key.ctrl, pynput.keyboard.KeyCode.from_char('0')]
    current = set()

    def main_function():
        current.clear()
        user_input = select_input()
        bot_response = send_to_bot(model, user_input, creativity, max_tokens)
        paste_response(bot_response)
        current.clear()

    def on_press(key):
        current.add(key)
        if all(k in current for k in combination):
            main_function()

    def on_release(key):
        if key in current:
            current.remove(key)

    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()



