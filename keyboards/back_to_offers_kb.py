from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back_to_offers_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вернуться', callback_data='back_to_offers')],
])
