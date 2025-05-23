import asyncio
from telegram import Bot

BOT_TOKEN = "7988737033:AAGSFvjK_YgxZIvQCsHdMb3plIOy-x0JCck"
CHAT_ID = 420354567  # например 420354567

async def main():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text="Привет! Это тестовое сообщение от твоего бота 😊")

if __name__ == "__main__":
    asyncio.run(main())
