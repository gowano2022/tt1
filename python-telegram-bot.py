import random

from telegram import Bot

# Set up your Telegram bot token

bot_token = '5412336519:AAH-HGiiJJ-AZE3D5FF9457pJACcT-jbqQg'

# Create a bot instance

bot = Bot(token=bot_token)

# Generate a random number

random_number = random.randint(1, 100)

# Send the random number to Telegram

bot.send_message(chat_id='373715044', text=f"Random Number: {random_number}")

