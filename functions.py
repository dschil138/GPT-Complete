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

def send_to_bot(model_var, prompt_var):
    try:
        full_prompt = (f"{prepend}\n{prompt_var}")
    except:
        full_prompt = prompt_var
    print(full_prompt)
    response = openai.Completion.create(
        model=model_var,
        prompt=full_prompt,
        temperature=creativity,
        max_tokens=max_tokens,
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
