import os
import telebot
from telebot import types

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

BOOKING_LINK = "https://ВАША_ССЫЛКА_НА_ЗАПИСЬ"


def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("📅 Записаться на визит")
    btn2 = types.KeyboardButton("🌿 Протоколы")
    btn3 = types.KeyboardButton("💳 Стоимость")
    btn4 = types.KeyboardButton("⚡ Как проходит сеанс")
    btn5 = types.KeyboardButton("❓ Задать вопрос")

    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)

    return markup


@bot.message_handler(commands=["start"])
def start(message):
    text = (
        "🏆 *AVITA LAB*\n\n"
        "Технологии восстановления и управления состоянием.\n\n"
        "Выберите интересующий раздел:"
    )

    bot.send_message(
        message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=main_menu()
    )


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "📅 Записаться на визит":
        bot.send_message(
            message.chat.id,
            f"Для записи перейдите по ссылке:\n{BOOKING_LINK}",
            reply_markup=main_menu()
        )

    elif message.text == "🌿 Протоколы":
        bot.send_message(
            message.chat.id,
            "Human OS — система восстановления внутренних ресурсов организма.",
            reply_markup=main_menu()
        )

    elif message.text == "💳 Стоимость":
        bot.send_message(
            message.chat.id,
            "⚡ Разовое посещение — 3900 ₽\n\n⭐ Абонементы доступны со скидкой.",
            reply_markup=main_menu()
        )

    elif message.text == "⚡ Как проходит сеанс":
        bot.send_message(
            message.chat.id,
            "Продолжительность визита около 20 минут. Специалист находится рядом и сопровождает вас на протяжении всей процедуры.",
            reply_markup=main_menu()
        )

    elif message.text == "❓ Задать вопрос":
        bot.send_message(
            message.chat.id,
            "Напишите нам в Telegram, и мы обязательно ответим.",
            reply_markup=main_menu()
        )

    else:
        bot.send_message(
            message.chat.id,
            "Выберите пункт меню.",
            reply_markup=main_menu()
        )


print("Bot started...")
bot.infinity_polling(skip_pending=True)
