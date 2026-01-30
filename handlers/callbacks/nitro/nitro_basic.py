from aiogram import F, Router

router = Router()


@router.callback_query(F.data == 'nitro_basic')
async def process_nitro_basic_callback(callback_query):
    text = (
        "🎉 Вы выбрали предложение: Discord Nitro (Basic)!\n\n"
        "💎 Особенности Nitro Basic:\n"
        "- Доступ к базовым функциям Nitro\n"
        "- Улучшенные эмодзи и аватары\n"
        "- Возможность использования анимированных аватаров\n\n"
        "💰 Цена: $4.99 в месяц\n\n"
        "Чтобы оформить подписку, перейдите по [ссылке](https://discord.com/nitro/basic)\n\n"
        "Если у вас есть вопросы, не стесняйтесь обращаться!"
    )

    await callback_query.message.answer(
        text=text,
        parse_mode='Markdown',
    )
