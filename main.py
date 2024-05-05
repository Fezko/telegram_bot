import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

bot = Bot("6994333913:AAFZIKWxh9rWIzChd9hTKMvEq9ue6LeLT84")
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Hello!")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
