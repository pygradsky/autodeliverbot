from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def process_cmd_start(message: Message):
    text = f"👋 Привет, {message.from_user.username}!"

    await message.answer(
        text=text
    )
