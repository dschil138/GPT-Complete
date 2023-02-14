import openai
import time
from config import *
import pyautogui as pag
import pyperclip

pag.PAUSE = 0.15

def select_input():
    pyperclip.copy('')
    pag.sleep(0.1)
    pag.hotkey("command", "c", interval=0.1)
    current_selection=pyperclip.paste()
    pag.sleep(0.1)
    if current_selection.length() < 2:
        pag.keyDown("shift")
        pag.hotkey("command", "left")
        pag.keyUp("shift")
        pag.keyDown("shift")
        for i in range(lines_to_send - 2):
            pag.hotkey("left")
            pag.hotkey("up")
        pag.hotkey("command", "left")
        pag.keyUp("shift")
        pag.sleep(0.1)
        pag.hotkey("command", "c", interval=0.1)
    pag.sleep(0.1)
    pag.hotkey("right")
    pag.hotkey("space")
    return pyperclip.paste()

def send_to_bot(model_var, prompt_var, creativity_var, max_tokens_var):
    print(prompt_var)
    full_prompt = (f"Continue or finish the following text:\n{prompt_var}")
    response = openai.Completion.create(
        model=model_var,
        prompt=full_prompt,
        temperature=creativity_var,
        max_tokens=max_tokens_var,
        top_p=1,
        frequency_penalty=1.2,
        presence_penalty=1.2
    )
    stripped_response = response.choices[0].text.strip()
    print(stripped_response)
    pag.sleep(0.1)
    return stripped_response

def write_response(response):
    print(response)
    pag.typewrite(response)

def paste_response(response):
    pyperclip.copy(response)
    pag.sleep(0.1)
    pag.hotkey("command", "v")
