from aiogram import F, Router
from keyboards.back_to_offers_kb import back_to_offers_keyboard

router = Router()


@router.callback_query(F.data == 'nitro_full')
async def process_nitro_basic_callback(callback_query):
    text = (
        "🎉 Вы выбрали предложение: Discord Nitro (Full)!\n\n"
        "📌 Особенности Nitro Full:\n"
        "• Доступ ко всем функциям Nitro\n"
        "• Улучшенные эмодзи и аватары\n"
        "• Возможность использования анимированных аватаров\n"
        "• Серверные бусты и эксклюзивные привилегии\n\n"
        "📌 _Всю информацию о подписках Nitro можете найти_ [здесь](https://discord.com/nitro).\n\n"
        "Если у вас есть вопросы, не стесняйтесь обращаться!"
    )

    await callback_query.message.edit_text(
        text=text,
        parse_mode='Markdown',
        reply_markup=back_to_offers_keyboard,
        disable_web_page_preview=True
    )
