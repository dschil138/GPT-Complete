import openai
import time
from config import *
import pyautogui as pag
import pyperclip


def select_input():
    pag.sleep(0.1)
    pyperclip.copy('')
    pag.sleep(0.1)
    pag.hotkey("command", "c")
    pag.sleep(0.1)
    current_selection=pyperclip.paste()
    pag.sleep(0.1)



    if current_selection.length() < 2:
        pag.sleep(0.1)
        pag.keyDown("shift")
        pag.sleep(0.1)
        pag.hotkey("command", "left")
        pag.sleep(0.1)
        pag.hotkey("up")
        pag.hotkey("up")
        pag.hotkey("up")
        pag.hotkey("up")
        pag.hotkey("command", "left")
        pag.keyUp("shift")
        pag.sleep(0.1)
        pag.hotkey("command", "c")

    pag.sleep(0.2)
    pag.hotkey("right")
    pag.sleep(0.1)
    return pyperclip.paste()

def sendToBot(myPrompt, creativityV, maxTokens):

    print(myPrompt)
    response = openai.Completion.create(
        model="text-curie-001",
        prompt=myPrompt,
        temperature=creativityV,
        max_tokens=80,
        top_p=1,
        frequency_penalty=1.2,
        presence_penalty=1.2,
        stop=["?"]   
    )
    fullResponse = response.choices[0].text
    print(fullResponse)
    strippedResponse = response.choices[0].text.strip()
    print(strippedResponse)
    pag.sleep(0.3)
    return strippedResponse

def write_response(response):
    print(response)
    pag.typewrite(response)

def paste_response(response):
    # pag.hotkey("space")
    pyperclip.copy(response)
    pag.sleep(0.2)
    pag.hotkey("command", "v")
