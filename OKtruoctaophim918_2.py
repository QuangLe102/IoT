from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import json


wiotoken_IOT = '2ebe19f544259356d81fb78431de10d2'

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Xin Chào {update.effective_user.first_name} {update.effective_user.last_name}\nWIOBOT có thể giúp gì cho bạn ?')
    update.message.reply_text(f'Các lệnh hỗ trợ:\n\n/hello : START \n/info : THÔNG TIN  \n/NHIETDOPHONG : HIỂN THỊ NHIỆT ĐỘ PHÒNG \n/DOAMKHONGKHI : ĐO ĐỘ ẨM KHÔNG KHÍ\n/BATDEN : MỞ ĐÈN \n/TATDEN : TẮT ĐÈN \n/DOAMDAT : ĐO ĐỘ ẨM ĐẤT\n/MOBOM : MỞ BƠM NƯỚC\n/TATBOM : TẮT BƠM NƯỚC')
  

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

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Các lệnh hỗ trợ:\n\n/hello : START \n/info : THÔNG TIN  \n/NHIETDOPHONG : HIỂN THỊ NHIỆT ĐỘ PHÒNG \n/DOAMKHONGKHI : ĐO ĐỘ ẨM KHÔNG KHÍ\n/BATDEN : MỞ ĐÈN \n/TATDEN : TẮT ĐÈN \n/DOAMDAT : ĐO ĐỘ ẨM ĐẤT\n/MOBOM : MỞ BƠM NƯỚC\n/TATBOM : TẮT BƠM NƯỚC')
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


updater = Updater('5354867750:AAGz-aBecCDNx_bkrm-wSz6mWwvFfhEALIM')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('BATDEN', BATDEN))
updater.dispatcher.add_handler(CommandHandler('TATDEN', TATDEN))
updater.dispatcher.add_handler(CommandHandler('NHIETDOPHONG', NHIETDOPHONG))
updater.dispatcher.add_handler(CommandHandler('DOAMKHONGKHI', DOAMKHONGKHI))
updater.dispatcher.add_handler(CommandHandler('info', info))
updater.dispatcher.add_handler(CommandHandler('h', help))
updater.dispatcher.add_handler(CommandHandler('DOAMDAT', DOAMDAT))
updater.dispatcher.add_handler(CommandHandler('MOBOM',MOBOM))
updater.dispatcher.add_handler(CommandHandler('TATBOM',TATBOM))
updater.start_polling()
updater.idle()
