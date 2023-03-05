import openai
import time
from config import *
import pyautogui as pag
import pyperclip
import re

pag.PAUSE = 0.15

def extract_number(input_text):
    '''Extracts the number from between the colons at the end of the input text.'''
    sub_text = input_text[-5:]
    match = re.search(r':(\d+):', sub_text)
    if match:
        return match.group(1)
    return None


def check_for_highlighted_text():
    print("check_for_highlighted_text")
    pyperclip.copy('')
    pag.sleep(0.1)
    pag.hotkey("command", "c", interval=0.1)
    current_selection=pyperclip.paste()
    pag.sleep(0.1)
    if current_selection.length() < 2:
        print("no text selected")
        return False
    else:
        print("selected text found")
        return pyperclip.paste()
    

def check_for_typed_number():
    print("check_for_typed_number")
    pag.sleep(0.1)
    pag.keyDown("shift")
    pag.hotkey("command", "left")
    pag.keyUp("shift")
    pag.keyDown("shift")
    pag.hotkey("left")
    pag.hotkey("up")
    pag.keyUp("shift")
    pag.sleep(0.1)
    pag.hotkey("command", "c", interval=0.1)
    pag.sleep(0.1)
    pag.hotkey("right")
    text_to_check_for_typed_num = pyperclip.paste()
    extracted_number = extract_number(text_to_check_for_typed_num)
    if extracted_number:
        print(f"{extracted_number} found")
        return extracted_number
    else:
        print("no number found")
        return False


def select_input(typed_number_var):
    print("select_input")
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
        for i in range(int(typed_number_var) - 2):
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


def remove_numbers_and_colons_from_end(text):
    sub_text = text[-7:]
    match = re.search(r':(\d+):', sub_text)
    if match:
        return text[:-len(match.group())]
    else:
        return text


def check_and_select_input():
    print("check_and_select_input")
    highlighted_text = check_for_highlighted_text()
    if highlighted_text:
        return highlighted_text
    else:
        typed_number = check_for_typed_number()
        if typed_number:
            return select_input(typed_number)
        else:
            return select_input(lines_to_send)


def send_to_bot(prepend_var, model_var, prompt_var):
    cut_prompt = remove_numbers_and_colons_from_end(prompt_var)
    print(f"\nCUT PROMPT: {cut_prompt}\n")
    try:
        print(f"\nTRY CLAUSE PREPEND: {prepend_var}\n")
        full_prompt = (prepend_var+cut_prompt)
        print(f"\nTRY CLAUSE FULL PROMPT: {full_prompt}\n")
    except:
        full_prompt = cut_prompt
        print(f"\nEXCEPT CLAUSE FULL PROMPT: {full_prompt}\n")
    print(f"\n\FULL PROMPT: {full_prompt}\n\n")
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
