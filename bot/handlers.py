from aiogram import types, Router
from aiogram.filters import CommandStart, Command

from services import QuestionService

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    start_text = 'Используйте /next для получения вопросов.'
    await message.answer(start_text)


@router.message(Command(commands=['next']))
async def cmd_next(message: types.Message):
    user_id = message.from_user.id
    service = QuestionService(user_id)
    text = await service.get_question()
    await message.answer(text)