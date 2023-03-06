![GPT-Complete logo](photos/GPT-Complete-logo-clear-2.png)

# Description
GPT-Complete allows you to incorporate OpenAI's GPT into your workflow with the touch of a button.

Anywhere you are entering text, you can just hit the GPT-Complete hotkey, and the last few lines of your text will be sent to the GPT Model. Within a few seconds, the results pasted back at your cursor.

Writing an email and don’t know what to say next? Hit the shortcut. Making a list of ideas and need a few more to help you brainstorm? You’ve got a hotkey for that. Is the code you’re working on getting a bit repetitive? Let  AI finish it for you - just hit the button.

Be default, the script will send the last 4 lines above your current cursor position. But you can set this to be whatever number want.

Or, if you'd like, you can manually highlight the text you want to send as the prompt. If you have text highlighted when you hit the hotkey, the script will notice and send that as the prompt. The results will be pasted back directly following the highlighted text (and also copied to your clipboard).

## Build:

Install these dependencies:
- pyperclip
- pyautogui
- pynput
- openai
- regex
- rumps

You can install them using this command

```bash
pip3 install pyperclip pyautogui pynput openai regex rumps
```

Before using GPT-Complete, you need to get an OpenAI API key and add it to the config.py file. You can get one on OpenAI's site [here](https://openai.com/blog/openai-api/).

Once you've added the API key, you are ready to go!


 ## Use:

The program needs to run in the background as a Mac Menu Bar item. However currently you must start the program from the command line. Open a terminal window, navigate to wherever you have saved the code, and run the file:

```py
python3 gpt-complete.py
```

You can now minimize or hide this terminal window.

## Config
The program will work right out of the box, but there are several user-settable parameters. Some of can be set in the menu in the menu bar, others are set in the config.py file

#### How Many Lines To Select (config file)
You can now tell the model how many lines above your cursor to select by simply typing it before you hit the hotkey. If you want to select 15 lines, put it between two colons like this - **:15:** (this needs to be the last thing typed before the cursor). The model will read the number and select that many lines.

If you do not set this number by typing it, the program will use "lines_to_send" variable in the config file to decide how many lines it will select. The default is 6.

As always, you can also just select the text you want to send before you hit the hotkey.

#### Model (Menu)
Choose which OpenAI model you would like to send your prompt to. The default is DaVinci (their most powerful model).

#### Max Tokens (Menu)
Upper limit on how many tokens the model should return in it's response. Current options are 100, 250, 500, and 800
  
#### Creativity (config file)
How "creative" and unpredictable you would like the response to be. This corresponds to OpenAI's "temperature" setting, and ranges from 0 to 1. The default here is set to 0.8

**Lines To Send** - If you have text selected already when you hit the hotkey, the program will send that text. Otherwise, it will send the last N lines before your current cursor position.  The default is 4. More lines will get you better results but will also be more expensive, as you are charged for the tokens you send as well as the ones you receive.

#### Hotkey (Menu)
Choosing a hotkey for this program can be a little tricky. There are currently four options to choose from which have all been tested and work well. 
>**1.** Left Alt + Right Ctrl
>**2.** Ctrl + 0
>**3.** Command + Enter
>**4.** Ctrl + Shift + K


# Future Development

- Move all config options to the Menu

- Add more dynamically-typed options like the :linesNumber: is now