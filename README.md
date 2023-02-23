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

Before using GPT-Complete, you need to get an OpenAI API key and add it to the config.py file. You can get one on OpenAI's site [here](https://openai.com/blog/openai-api/).

Once you've added the API key, you are ready to go!


 ## Use:

The program needs to run in the background. Open a terminal window, navigate to wherever you have saved this folder of code, and run the file:

```py
python3 gpt-complete.py
```


You can now minimize or hide this terminal window. It will run in the background, taking up essentially no memory. Its functions are only activated when the hotkeys are hit.

## Config
The program will work right out of the box, but there are several user-settable parameters that you can customize located in the config.py file:

*(there are also comments in the actual python file that provide more info on each)*

#### Model
Choose which OpenAI model you would like to send your prompt to. The default is DaVinci (their most powerful model).

#### Creativity
How "creative" and unpredictable you would like the response to be. This corresponds to OpenAI's "temperature" setting, and ranges from 0 to 1. The default here is set to 0.8

**Lines To Send** - If you have text selected already when you hit the hotkey, the program will send that text. Otherwise, it will send the last N lines before your current cursor position.  The default is 4. More lines will get you better results but will also be more expensive, as you are charged for the tokens you send as well as the ones you receive.

#### Hotkey
Choosing a hotkey for this program can be a little tricky. There are currently four options to choose from which have all been tested and work well. 
>**1.** Left Alt + Right Ctrl
>**2.** Ctrl + 0
>**3.** Command + Enter
>**4.** Ctrl + Shift + K

#### Multiple HotKeys for Multiple Models
you can now define different hotkeys to send your prompt to different models. 

*For example:* if you have a simple list you need completed, you probably don't need the power (and expense) of the DaVinci model. So you could have Ctrl-0 set to send your prompt to the Curie model. But if you are trying to finish a poem, you could hot Ctrl + Shift + K to send the prompt to DaVinci.

#### Prepend
Uncomment this variable if you'd like to prepend a string to all your prompts. This can be helpful if you always want a specific behavior from your completions, for instance, if you want your completions to always have a cheerful demeanor, you could add a prepend string of "finish this text the way a cheerful person would:"

Keep in mind that you are charged for the words you send to the model, as well as the ones you recieve. So don't go too crazy on the prepending.



# Future Development

- More user-configurable hotkeys

- Be able to run the program as a mac menu bar item, not as a python script.