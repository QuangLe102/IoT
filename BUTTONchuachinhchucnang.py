from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import json
import telegram

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint

wiotoken_IOT = '2ebe19f544259356d81fb78431de10d2'

bot = Bot(token='5354867750:AAGz-aBecCDNx_bkrm-wSz6mWwvFfhEALIM')
dp = Dispatcher(bot)

button1 = InlineKeyboardButton(text="📑 Thông tin", callback_data="randomvalue_of20")
button2 = InlineKeyboardButton(text="🌡 Nhiệt độ phòng", callback_data="randomvalue_of30")
button3 = InlineKeyboardButton(text="🌦 Độ ẩm không khí", callback_data="randomvalue_of40")
button4 = InlineKeyboardButton(text="💧 Độ ẩm đất", callback_data="randomvalue_of50")
button5 = InlineKeyboardButton(text="🔦 Trạng thái đèn", callback_data="randomvalue_of60")
button6 = InlineKeyboardButton(text="🌕 Mở đèn", callback_data="randomvalue_of70")
button7 = InlineKeyboardButton(text="🌑 Tắt đèn", callback_data="randomvalue_of80")
button8 = InlineKeyboardButton(text="☔ Mở bơm nước", callback_data="randomvalue_of90")
button9 = InlineKeyboardButton(text="🌞 Tắt bơm nước", callback_data="randomvalue_of100")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3, button4, button5, button6, button7, button8, button9)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add( "📑 Thông tin", "🌡 Nhiệt độ phòng", "🌦 Độ ẩm không khí", "💧 Độ ẩm đất", "🔦 Trạng thái đèn", "🌕 Mở đèn", "🌑 Tắt đèn", "☔ Mở bơm nước", "🌞 Tắt bơm nước")

@dp.message_handler(commands=['start', 'help'])
async def welcom(message: types.Message):
    #await message.reply_text(f'Xin Chào {message.effective_user.first_name} {message.effective_user.last_name}')
    await message.reply("Xin chào! \nWIOBOT có thể giúp gì cho bạn ?", reply_markup=keyboard1)

@dp.callback_query_handler(text=["randomvalue_of20", "randomvalue_of30","randomvalue_of40","randomvalue_of30", "randomvalue_of100"])
async def random_value(call: types.CallbackQuery):
    if call.data == "randomvalue_of20":
        await call.message.answer(randint(1, 20))
    if call.data == "randomvalue_of30":
        await call.message.answer(randint(1, 30))
    if call.data == "randomvalue_of40":
        await call.message.answer(randint(1, 40))
    if call.data == "randomvalue_of50":
        await call.message.answer(randint(1, 50))
    if call.data == "randomvalue_of60":
        await call.message.answer(randint(1, 60))
    if call.data == "randomvalue_of70":
        await call.message.answer(randint(1, 70))
    if call.data == "randomvalue_of80":
        await call.message.answer(randint(1, 80))
    if call.data == "randomvalue_of90":
        await call.message.answer(randint(1, 90))
    await call.answer()


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == '📑 Thông tin':
        await message.reply('------------------------------\nNhóm 1:        \nNguyễn Văn Tâm    19146384 \nLê Quang Chiến      19146310 \nNguyễn Anh Quốc  19146380\n-------------------------------', reply_markup=keyboard1)
    elif message.text == '🌡 Nhiệt độ phòng':
        await message.reply("https://youtube.com/gunthersuper", reply_markup=keyboard1)
    elif message.text == '🌦 Độ ẩm không khí':
        await message.reply('------------------------------\nNhóm 1:        \nNguyễn Văn Tâm    19146384 \nLê Quang Chiến      19146310 \nNguyễn Anh Quốc  19146380\n-------------------------------', reply_markup=keyboard1)
    elif message.text == '💧 Độ ẩm đất':
        await message.reply("https://youtube.com/gunthersuper", reply_markup=keyboard1)
    elif message.text == '🔦 Trạng thái đèn':
        await message.reply('------------------------------\nNhóm 1:        \nNguyễn Văn Tâm    19146384 \nLê Quang Chiến      19146310 \nNguyễn Anh Quốc  19146380\n-------------------------------', reply_markup=keyboard1)
    elif message.text == '🌕 Mở đèn':
        await message.reply("https://youtube.com/gunthersuper", reply_markup=keyboard1)
    elif message.text == '🌑 Tắt đèn':
        await message.reply("https://youtube.com/gunthersuper", reply_markup=keyboard1)
    elif message.text == '☔ Mở bơm nước':
        await message.reply('------------------------------\nNhóm 1:        \nNguyễn Văn Tâm    19146384 \nLê Quang Chiến      19146310 \nNguyễn Anh Quốc  19146380\n-------------------------------', reply_markup=keyboard1)
    elif message.text == '🌞 Tắt bơm nước':
        await message.reply("https://youtube.com/gunthersuper", reply_markup=keyboard1)
    else:
        await message.reply(f"Your message is: {message.text}", reply_markup=keyboard1)

updater = Updater('5354867750:AAGz-aBecCDNx_bkrm-wSz6mWwvFfhEALIM')

executor.start_polling(dp)
