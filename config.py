# How unpredicatable do you want the bot to be? 
creativity = 0.9


# The max number of tokens you want to recieve in response. OpenAI charges by the
# token so this variable is important to keeping your costs down.
max_tokens = 100


# Which model you would like to send your prompts to.
# The options, from least powerful and cheap, to most powerful and expensive, are:
# text-001-ada
# text-001-curie
# text-001-babbage
# text-003-davinci
model = "text-davinci-003"


# If not manually selecting the prompt, how many lines above the 
# current cursor position do you want to send as the prompt
lines_to_send = 4

##Hotkey
# choosing a shortcuts can be a little tricky with this program, so
# there are currently 3 options to choose from.
# 1 == Left Alt + Right Ctrl 
# 2 == Ctrl + 0
# 3 == Command + Enter
hotkey = 1