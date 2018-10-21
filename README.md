# reading-your-facebook

Facebook learns from your data, you should too!

# Chatbot (deprecated)

Underneath the `chatbot/` directory you will find 3 Jupyter notebooks with the tools to make a chatbot. Data Collection will create a navigable dataset of your messages, while Data Exploration will mine data on specific people. Once you have sufficiently clean data on a specific person stored in JSON files, they will be available to chat with in the Diffy Chatbot notebook. The algorithm does not use AI, and instead forms something similar to a lookup table for messages.

There are also two other files, `person.py` which has some convenience tools for loading different people, and `bot.py` which is the scaffolding for a FB Messenger bot based off of this.