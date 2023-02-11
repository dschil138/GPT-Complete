import openai

# insert your OpenAI key here
openai.api_key = "YOUR_API_KEY_HERE"

# How unpredicatable do you want the bot to be? 
creativity = 0.9

maxTokens = 100

# Which model you would like to send your prompts to.
# The options, from least powerful and cheap, to most powerful and expensive, are:
# text-001-ada
# text-001-curie
# text-001-babbage
# text-003-davinci

model = "text-davinci-003"