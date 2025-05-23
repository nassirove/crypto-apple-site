import os
import asyncio
from telegram import Bot
from telegram.error import TelegramError

BOT_TOKEN = "7988737033:AAGSFvjK_YgxZIvQCsHdMb3plIOy-x0JCck"
CHAT_ID = 420354567
PROJECT_DIR = "/Users/fazliddinnosirov/Desktop/telegram-bot/project"  # Абсолютный путь

bot = Bot(token=BOT_TOKEN)

async def send_files():
    for root, dirs, files in os.walk(PROJECT_DIR):
        for file in files:
            if file.startswith("."):
                continue
            filepath = os.path.join(root, file)
            print(f"📁 Найден файл: {filepath}")
            try:
                with open(filepath, "rb") as f:
                    await bot.send_document(chat_id=CHAT_ID, document=f, filename=file)
                    print(f"✅ Отправлен: {file}")
            except TelegramError as e:
                print(f"❌ Ошибка Telegram при отправке {file}: {e}")
            except Exception as e:
                print(f"❌ Другая ошибка при отправке {file}: {e}")

if __name__ == "__main__":
    asyncio.run(send_files())
