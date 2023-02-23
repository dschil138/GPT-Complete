import openai
import time
from config import *
import pyautogui as pag
import pyperclip
# from bs4 import BeautifulSoup
from AppKit import NSWorkspace
import re
import subprocess



def check_gmail():
    # Get the shared workspace

    workspace = NSWorkspace.sharedWorkspace()

    # Get the URL of the currently active webpage in Chrome
    chrome_bundle_identifier = "com.google.Chrome"
    chrome_app = workspace.frontmostApplication()
    if chrome_app.bundleIdentifier() == chrome_bundle_identifier:
        # Get the process ID of the Chrome process
        chrome_pid = chrome_app.processIdentifier()
        # Get the URL of the active tab in Chrome
        cmd = f"osascript -e 'tell application \"Google Chrome\" to get the URL of active tab of window 1'"
        output = subprocess.check_output(cmd, shell=True)
        current_url = output.decode("utf-8").strip()
        if "gmail" in current_url:
            print("in gmail")
            return True
        else:
            print("not in gmail")
            return False
    else:
            print("not in gmail")
            return False
        

def create_full_prepend(in_gmail):
    if in_gmail is True:
        print("gmail was true")
        full_prepend = (universal_prepend + "finish this email")
    else:
        print("gmail was false")
        full_prepend = universal_prepend
    print(full_prepend)
    return full_prepend




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

def send_to_bot(prepend, model_var, prompt_var):
    try:
        full_prompt = (f"{prepend}\n\n{prompt_var}")
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
