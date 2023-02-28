import openai
import time
from config import *
import pyautogui as pag
import pyperclip
from AppKit import NSWorkspace, NSAppleScript


# check open apps for Chrome
def check_apps_for_chrome():
    workspace = NSWorkspace.sharedWorkspace()
    running_apps = workspace.runningApplications()
    chrome_open = False
    chrome_active = False
    for app in running_apps:
        if app.bundleIdentifier() == "com.google.Chrome":
            print("Google Chrome is active.")
            return True


# check open tabs for gmail
def check_tabs_for_gmail(tab_wanted):
    script = NSAppleScript.alloc().initWithSource_("""
        tell application "Google Chrome"
            return URL of active tab of front window
        end tell
        """)
    result, error = script.executeAndReturnError_(None)
    if error:
        print(error)
    else:
        print(result.stringValue())
        tabs_string = result.stringValue()
        if tabs_string.find(tab_wanted) != -1:
            print("found gmail")
            return True
        else:
            return False



def check_system_for_gmail(website_wanted):
    if check_apps_for_chrome():
        if check_tabs_for_gmail(website_wanted):
            print("gmail is active")
            return True
    else:
        print("Google Chrome is not active.")

def create_full_prepend(website_wanted):
    if check_system_for_gmail(website_wanted):
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
