![GPT-Complete logo](photos/GPT-Complete-logo-clear-2.png)

# Description
GPT-Complete allows you to incorporate OpenAI's GPT into your workflow with the touch of a button.

Anywhere you are entering text, you can just hit the GPT-Complete hotkey, and the last few lines of your text will be sent to the GPT Model. Within a few seconds, the results pasted back at your cursor.

Writing an email and don’t know what to say next? Hit the shortcut. Making a list of ideas and need a few more to help you brainstorm? You’ve got a hotkey for that. Is the code you’re working on getting a bit repetitive? Let  AI finish it for you - just hit the button.

Be default, the script will send the last 4 lines above your current cursor position. But you can set this to be whatever number want.

Or, if you'd like, you can manually highlight the text you want to send as the prompt. If you have text highlighted when you hit the hotkey, the script will notice and send that as the prompt. The results will be pasted back directly following the highlighted text (and also copied to your clipboard).
## Build:

GPT-Complete uses these dependencies:
- pyperclip
- pyautogui
- pynput
- openai

You can install them using this command

```bash
pip3 install pyperclip pyautogui pynput openai
```

Before using this script, you need to add your API key to the config.py file. You can get an API key on OpenAI's site [here](https://openai.com/blog/openai-api/).

Once you've added the API key, you are ready to go!


 ## Use:

The program needs to run in the background. Open a terminal window, navigate to wherever you have saved this folder of code, and run the file:

```py
python3 gpt-complete.py
```


You can now minimize or hide this terminal window.It will run in the background, taking up essentially no memory. Its functions are only activated when the hotkeys are hit.

## Config
The program will work right out of the box, but there are several user-settable parameters that you can customize located in the config.py file:

*(there are also comments in the actual python file that provide more info on each)*

**Model** - choose which OpenAI model you would like to send your prompt to. The default is DaVinci (their most powerful model).

**Creativity** - how "creative" and unpredictable you would like the response to be. This corresponds to OpenAI's "temperature" setting, and ranges from 0 to 1. The default here is set to 0.8

**Lines To Send** - If you have text selected already when you hit the hotkey, the program will send that text. Otherwise, it will send the last N lines before your current cursor position.  The default is 4. More lines will get you better results but will also be more expensive, as you are charged for the tokens you send as well as the ones you receive.

**Hotkey** - Currently the hotkey is CMD-Enter. This will be a user configurable variable in future versions. If you feel comfortable enough with Python, you can edit this currently in the main file (GPT-Complete.py)


# Future development

- User-configurable hotkeys.

- Have separate shortcuts for different models 

    - *IE:  `CMD-Enter` would send prompt to DaVinci, `CMD-Shift-Enter` would send prompt to Curie*

- Add option to prepend a string to any text that is sent to the model.

- Be able to run the program as a menu bar item, not as a python script. Ideally one that can be installed as a daemon to run at startup