from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def process_cmd_start(message: Message):
    text = (f"👋 Привет, {message.from_user.username}!\n"
            "Я - бот, у которого ты можешь купить различные товары.\n"
            "Используй команды в меню, чтобы узнать больше!")


    await message.answer(
        text=text
    )
