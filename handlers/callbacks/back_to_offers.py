from aiogram import F, Router
from handlers.cmds.cmd_offers import offers_keyboard

router = Router()


@router.callback_query(F.data == 'back_to_offers')
async def process_cmd_offers(callback_query):
    text = f"🔥 Выберите предложение из списка ниже:"

    await callback_query.message.edit_text(
        text=text,
        reply_markup=offers_keyboard,
    )
