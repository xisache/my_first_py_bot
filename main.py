from telebot import TeleBot   # TeleBot kutubxonasini import qilamiz
from knopka import media_button, orqaga   # Tugmalar bor faylni import qilamiz

bot = TeleBot("6165678324:AAGJVLBNPy44Wr6kBF1fY_xVqM9UK2P32ew")  # Bot tokeni yoziladigan joy

# Salomlashuv rasm bilan va tugmalarni chiqaramiz
@bot.message_handler(commands=['start'])
def send_welcome(message):
    image = 'https://cybersport.metaratings.ru/upload/iblock/cfa/cfadee5567c5b27d3aec7fce74a256ed.png'
    # Botga rasm yuborish
    bot.send_photo(message.chat.id,   # Foydalanuvchi ID si
                   image,
                   caption=f"*Assalomu alaykum va rahmatulloh!\n{message.from_user.full_name}* ahvollaringiz qalay)\nMarhamat, kerakli bo'limni tanlang!",   # Rasm tagiga izoh [caption]
                   parse_mode="markdown",   # Tekst formati [markdown or html]
                   reply_markup=media_button    # Tugmalarni menyuga ulab olamiz
                   )

# Tugmalarni bosganda yuboriladigan narsalar
@bot.callback_query_handler(func=lambda call:True)
def handle_media(call):
    if call.data == 'audio':
        audio = "https://t.me/goloslarhostingi/230" # Musiqa manzili
        bot.delete_message(call.message.chat.id, call.message.id)   # Tugmani bosilgan xabarni o'chirib yuborish [dizayn uchun :)]
        bot.send_audio(call.message.chat.id, audio, reply_markup=orqaga)    # Musiqa yuborish
        
    elif call.data == 'photo':
        image = 'https://raw.githubusercontent.com/xisache/my_first_py_bot/main/image.jpg'  # Rasm manzili
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, image, reply_markup=orqaga)  # Rasm yuborish
        
    elif call.data == 'video':
        video = "https://raw.githubusercontent.com/xisache/my_first_py_bot/main/video.mp4"  # Video manzili
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_video(call.message.chat.id, video, reply_markup=orqaga)  # Video yuborish
        
    elif call.data == 'file':
        file = "https://raw.githubusercontent.com/xisache/my_first_py_bot/main/main.py"  # Fayl manzili
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_document(call.message.chat.id, file, reply_markup=orqaga)  # Fayl yuborish
        
    # Orqaga qaytish tugmasi
    elif call.data == 'back':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id,
                         text="🏠Bosh menyuga qaytdingiz!\n🖲Menyulardan birini tanlang!",
                         reply_markup=media_button)

bot.polling(none_stop=True)