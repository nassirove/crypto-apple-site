import asyncio
from telegram import Bot

BOT_TOKEN = "7988737033:AAGSFvjK_YgxZIvQCsHdMb3plIOy-x0JCck"
CHAT_ID = 7988737033  # твой ID

async def send_text():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text="Привет, мой любимый! 💌")

asyncio.run(send_text())

