import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
import hendlers.mainhen as mainhen
import hendlers.graphhen as graphhen
import hendlers.datahen as datahen


logging.basicConfig(level=logging.INFO)

bot = Bot(token="6921390682:AAEsuCWzsxXIgPhdq5OhuloVl1EXyg4JlVk")

async def main():
    dp = Dispatcher()
    dp.include_routers(mainhen.router)
    dp.include_routers(graphhen.router)
    dp.include_routers(datahen.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())