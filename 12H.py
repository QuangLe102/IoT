from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import json
import telegram
from telegram.ext import CallbackQueryHandler,  ContextTypes
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint

wiotoken_IOT = 'fcea2268837ae9ce160fa29e836de93c'

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

#@dp.message_handler(commands=['start', 'help'])
#def start(update: Update, context: CallbackContext) -> None:
#    update.message.reply_text(f'Xin Chào {update.effective_user.first_name} {update.effective_user.last_name}')
#    update.message.reply_text("Xin chào! \nWIOBOT có thể giúp gì cho bạn ?", reply_markup=keyboard1)

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


def BATDEN(update: Update, context: CallbackContext) -> None:
    requests.post("https://cn.wio.seeed.io/v1/node/GenericDOutD0/onoff/1?access_token="+wiotoken_IOT)
    update.message.reply_text(f' Đèn trong phòng đã được bật!')
def TATDEN(update: Update, context: CallbackContext) -> None:
    requests.post("https://cn.wio.seeed.io/v1/node/GenericDOutD0/onoff/0?access_token="+wiotoken_IOT)
    update.message.reply_text(f'Đèn trong phòng đã tắt!')

def NHIETDOPHONG(update: Update, context: CallbackContext) -> None:
    TempSensor_Url =  "https://cn.wio.seeed.io/v1/node/GroveTempHumD1/temperature?access_token="+wiotoken_IOT
    tempReading = requests.get(TempSensor_Url)
    if tempReading.status_code == 200:
        tempReading = json.loads(tempReading.text)
        tempReading = tempReading['celsius_degree']
        update.message.reply_text(f'Nhiệt độ trong phòng hiện tại là: ' + str(tempReading) + ' °C')
    else:
        update.message.reply_text(f'Chưa cập nhật được nhiệt độ phòng.')

def DOAMKHONGKHI(update: Update, context: CallbackContext) -> None:
    doam_url= "https://cn.wio.seeed.io/v1/node/GroveTempHumD1/humidity?access_token="+wiotoken_IOT
    doam = requests.get(doam_url)
    if doam.status_code == 200:
        doam= json.loads(doam.text)
        doam = doam['humidity']
        update.message.reply_text(f'Độ ẩm không khí hiện tại trong phòng là:' + str(doam) + ' %')
        if doam < 40:
          update.message.reply_text(f'Độ ẩm không khí đang quá thấp! \nĐộ ẩm ở mức thấp làm cho làn da khô rát, khó chịu.')
          help()
        if doam > 70:
          update.message.reply_text(f'Độ ẩm không khí đang quá cao! \nĐộ ẩm ở mức cao dễ gây các bệnh về hô hấp, tạo điều kiện thuận lợi để các loại vi khuẩn có hại phát triển mạnh mẽ.')
    else:
        update.message.reply_text(f'Chưa cập nhật được độ ẩm phòng')

def DOAMDAT(update: Update, context: CallbackContext) -> None:
    m = requests.get("https://cn.wio.seeed.io/v1/node/GroveMoistureA0/moisture?access_token=" + wiotoken_IOT)
    if m.status_code == 200:
        m = json.loads(m.text)
        m = round(((m['moisture']*100)/1023),2)
        farstr = "Độ ẩm trong đất hiện tạo là : " + str(m) + ' %'
        update.message.reply_text(f'{farstr}')
        if m < 55:
          update.message.reply_text(f'Đất đang bị quá khô! \nBạn nên mở bơm nước để tưới cho cây.')
          
        if m > 75:
          update.message.reply_text(f'Đất đang quá ẩm! \nCây trong chậu có thể bị úng.')
    else:
        update.message.reply_text(f'Chưa cập nhật được độ ẩm trong đất')

def info(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('------------------------------\nNhóm 1:        \nNguyễn Văn Tâm    19146384 \nLê Quang Chiến      19146310 \nNguyễn Anh Quốc  19146380\n-------------------------------')


def MOBOM(update: Update, context: CallbackContext) -> None:
    requests.post("https://cn.wio.seeed.io/v1/node/GenericPWMOutD2/pwm/50?access_token="+wiotoken_IOT)
    update.message.reply_text(f' Mở bơm nước')
def TATBOM(update: Update, context: CallbackContext) -> None:
    requests.post("https://cn.wio.seeed.io/v1/node/GenericPWMOutD2/pwm/0?access_token="+wiotoken_IOT)
    update.message.reply_text(f'Tắt bơm nước')


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == '/start':
        await message.reply(f"Xin Chào!\nWIOBOT có thể giúp gì cho bạn ?", reply_markup=keyboard1)
    elif message.text == '📑 Thông tin':
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

#updater = Updater('5354867750:AAGz-aBecCDNx_bkrm-wSz6mWwvFfhEALIM')

executor.start_polling(dp)
