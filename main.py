import os
import asyncio

from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
BOOKING_URL = "https://n2229960.yclients.com"

MENU = ReplyKeyboardMarkup(
    [
        ["🗓 Записаться на визит"],
        ["🌱 Система протоколов восстановления"],
        ["✨ Как проходит сеанс?"],
        ["💎 Программы AVITA LAB"],
        ["❓ Задать вопрос"],
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
)

BOOKING_BUTTON = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🗓 Записаться на визит", url=BOOKING_URL)]]
)

QUESTION_BUTTONS = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("📩 Написать в Telegram", url="https://t.me/Info_avitalab")],
        [InlineKeyboardButton("🗓 Записаться на визит", url=BOOKING_URL)],
    ]
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "AVITA LAB\n\n"
        "<b><i>Human OS</i></b>\n"
        "Система протоколов восстановления\n\n"
        "Добро пожаловать в AVITA LAB.\n\n"
        "Ниже вы можете выбрать интересующий раздел и подробнее узнать о принципах работы Human OS, форматах посещения и программах восстановления.",
        parse_mode=ParseMode.HTML,
        reply_markup=MENU,
    )

    await update.message.reply_text(
        "🗓 Для записи выберите удобное время:",
        reply_markup=BOOKING_BUTTON,
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🗓 Записаться на визит":
        await update.message.reply_text(
            "🗓 Записаться на визит\n\n"
            "Выберите удобное время для посещения AVITA LAB и работы с системой протоколов восстановления Human OS.\n\n"
            "Мы позаботимся о том, чтобы каждый визит был максимально комфортным и соответствовал вашим текущим задачам и состоянию.",
            reply_markup=BOOKING_BUTTON,
        )

    elif text == "🌱 Система протоколов восстановления":
        await update.message.reply_text(
            "🌱 Система протоколов восстановления\n\n"
            "<b><i>Human OS (операционная система человека)</i></b> — это система протоколов восстановления, созданная для поддержки ресурса, энергии и качества повседневной жизни.\n\n"
            "Мы рассматриваем состояние человека как систему, которой можно управлять более осознанно. Поэтому вместо отдельных процедур используем протоколы — специальные сценарии восстановления, которые подбираются в зависимости от текущего состояния и задач человека.\n\n"
            "Среди них:\n\n"
            "• <b><i>RESET</i></b> — снижение перегрузки и внутреннего напряжения;\n"
            "• <b><i>FOCUS</i></b> — поддержка концентрации и внимания;\n"
            "• <b><i>FLOW</i></b> — состояние потока и продуктивности;\n"
            "• <b><i>SLEEP</i></b> — вечерний режим и подготовка к отдыху;\n"
            "• <b><i>RECOVERY</i></b> — восстановление после нагрузок;\n"
            "• <b><i>POST FLIGHT</i></b> — поддержка после перелётов и смены ритма.\n\n"
            "Протокол — это не отдельная процедура, а часть комплексного подхода к управлению внутренними ресурсами и качеством жизни.\n\n"
            "🏆 Наша задача — не «исправить» человека, а создать условия, в которых организм может эффективнее использовать собственные ресурсы и легче возвращаться в состояние баланса.",
            parse_mode=ParseMode.HTML,
            reply_markup=MENU,
        )

    elif text == "✨ Как проходит сеанс?":
        await update.message.reply_text(
            "✨ Как проходит сеанс?\n\n"
            "Каждое посещение AVITA LAB начинается с короткой беседы со специалистом. Мы уточняем особенности состояния, отвечаем на вопросы и помогаем подобрать наиболее подходящий протокол.\n\n"
            "Сам запуск <b><i>Human OS</i></b> занимает около <b><i>10 минут</i></b>, а общее время визита составляет порядка <b><i>20 минут</i></b>. В течение всего визита специалист находится рядом и всегда готов помочь, ответить на вопросы и обеспечить максимально комфортную атмосферу.\n\n"
            "<b><i>Во время запуска не требуется выполнять никаких действий</i></b> — достаточно расслабиться и уделить время себе. Многие люди отмечают ощущение расслабления, внутреннего спокойствия, снижения напряжения и общего восстановления ресурса.\n\n"
            "Каждый организм индивидуален, поэтому восприятие и ощущения могут отличаться.\n\n"
            "🤍 Для нас важно, чтобы каждый визит был не только комфортным, но и максимально внимательным и безопасным. Поэтому перед первым посещением мы всегда уточняем важные особенности здоровья и при необходимости рекомендуем предварительно проконсультироваться с лечащим врачом.",
            parse_mode=ParseMode.HTML,
            reply_markup=MENU,
        )

    elif text == "💎 Программы AVITA LAB":
        await update.message.reply_text(
            "💎 Программы AVITA LAB\n\n"
            "В AVITA LAB доступны различные форматы знакомства и регулярной работы с <b><i>Human OS</i></b>.\n\n"
            "⚡ <b><i>Ознакомительный визит — Бесплатно</i></b>\n\n"
            "Первое знакомство с системой протоколов восстановления <b><i>Human OS</i></b> и возможность получить собственный опыт взаимодействия с технологией.\n\n"
            "⚡ <b><i>RESET Session — 3 950 ₽</i></b>\n\n"
            "Разовый запуск <b><i>Human OS</i></b> для тех, кто хочет познакомиться с отдельными протоколами восстановления и получить первый опыт работы с системой.\n\n"
            "⭐️ <b><i>Абонемент Human OS Upgrade 10 — 31 600 ₽</i></b>\n\n"
            "Экономия — <b><i>7 900 ₽</i></b>\n\n"
            "Абонемент из 10 запусков для тех, кто хочет встроить работу с ресурсом и восстановлением в привычный ритм жизни.\n\n"
            "Включает:\n\n"
            "• любые протоколы платформы <b><i>Human OS</i></b>;\n"
            "• приоритетную запись;\n"
            "• возможность регулярной работы с состоянием;\n"
            "• экономию <b><i>7 900 ₽</i></b> по сравнению с разовыми посещениями.\n\n"
            "⭐️ <b><i>Флагманский абонемент Human OS Transformation 15 — 35 500 ₽</i></b>\n\n"
            "Экономия — <b><i>23 700 ₽</i></b>\n\n"
            "Абонемент из 15 запусков, позволяющий пройти через серию протоколов восстановления и получить максимально устойчивый эффект от использования <b><i>Human OS</i></b>.\n\n"
            "Включает:\n\n"
            "• персональный подбор протоколов;\n"
            "• любые протоколы платформы <b><i>Human OS</i></b>;\n"
            "• приоритетную запись;\n"
            "• комплексную работу с состоянием и ресурсом;\n"
            "• экономию <b><i>23 700 ₽</i></b> по сравнению с разовыми посещениями.",
            parse_mode=ParseMode.HTML,
            reply_markup=MENU,
        )

    elif text == "❓ Задать вопрос":
        await update.message.reply_text(
            "❓ Задать вопрос\n\n"
            "Если у вас остались вопросы, мы будем рады помочь!\n\n"
            "Для более комфортного общения рекомендуем написать нам в Telegram — так мы сможем быстрее ответить, подробнее рассказать о <b><i>Human OS</i></b> и помочь подобрать наиболее подходящий формат работы с системой.\n\n"
            "Telegram:\n"
            "@Info_avitalab\n\n"
            "📞 +7 (905) 773-80-49\n\n"
            "🤍 С удовольствием ответим на ваши вопросы и поможем сделать взаимодействие с AVITA LAB максимально комфортным.",
            parse_mode=ParseMode.HTML,
            reply_markup=QUESTION_BUTTONS,
        )

    else:
        await update.message.reply_text(
            "Пожалуйста, выберите раздел в меню ниже.",
            reply_markup=MENU,
        )


async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("AVITA LAB bot is running...")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    while True:
        await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())
