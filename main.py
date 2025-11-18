import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8580197689:AAFt7G-zllno5I8jQllMWoIod8GFrVWTYgE"  # вставь сюда токен

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я буду напоминать тебе про таблетки.")

@dp.message()
async def remind(message: types.Message):
    text = message.text.strip()
    await message.answer(f"Ты написал: {text}. Я сохраню напоминание.")  

async def main():
    try:
        print("Бот запущен!")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
