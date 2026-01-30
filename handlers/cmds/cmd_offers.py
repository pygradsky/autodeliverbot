from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

offers_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Discord Nitro', callback_data='nitro_offer')],
    [InlineKeyboardButton(text='Counter Strike 2', callback_data='cs2')],
])


@router.message(Command('offers'))
async def process_cmd_offers(message: Message):
    text = f"🔥 Выберите предложение из списка ниже:"

    await message.answer(
        text=text,
        reply_markup=offers_keyboard,
    )
