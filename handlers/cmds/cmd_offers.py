from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Discord Nitro (Full)', callback_data='nitro_full')],
    [InlineKeyboardButton(text='Discord Nitro (Basic)', callback_data='nitro_basic')],
])


@router.message(Command('offers'))
async def process_cmd_offers(message: Message):
    text = f"🔥 Выберите предложение из списка ниже:"

    await message.answer(
        text=text,
        reply_markup=keyboard,
    )
