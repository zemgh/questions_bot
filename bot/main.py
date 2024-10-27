import asyncio

from bot import dp, bot
from handlers import router


async def main():
    dp.include_router(router)
    print('Bot started')
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())