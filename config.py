# How unpredicatable do you want the bot to be? 

creativity = 0.8



# The max number of tokens you want to recieve in response. OpenAI charges by the
# token so this variable is important to keeping your costs down.

max_tokens = 100



# Which model you would like to send your prompts to.
# The options, from least powerful and cheap, to most powerful and expensive, are:
# text-ada-001
# text-babbage-001
# text-curie-001
# text-davinci-003

model1 = "text-curie-001"

model2 = "text-davinci-003"


# If not manually selecting the prompt, how many lines above the 
# current cursor position do you want to send as the prompt

lines_to_send = 4



##Hotkey
# choosing a shortcuts can be a little tricky with this program, so
# there are currently 3 options to choose from.
# 1 == Left Alt + Right Ctrl 
# 2 == Ctrl + 0
# 3 == Command + Enter
# 4 == Command + Shift + K

hotkey1 = 4

hotkey2 = 2



# Prepend - uncomment this variable if you'd like to prepend a string to all your
# prompts. This can be helpful if you want specific behavior from your completions, for
# instance, if you want your completions to always have a cheerful demeanor, you
# could prepend "finish this text the way a cheerful person would:"
# Keep in mind that you are charged for the words you SEND to the model, as well as the
# ones you recieve.

# prepend = "finish this text:"