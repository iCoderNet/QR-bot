from qr import *
import telebot

bot = telebot.TeleBot("1817152864:AAF64N1g5rwGUeJnVwci92Q5RnIo8XkYKcw")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, f"""🧾 QR kod ni o'qish uchun rasmni yuboring!!!

📇 O'zingiz QR kod yasamoqchi bo'lsangiz  `/qr va text` shunday tartibda
""", parse_mode='MarkDown')

@bot.message_handler(commands=['qr'])
def send_welcome(message):
	try:
		soz = message.text.split(' ')[1]
		qr_code(soz)
		img = open('code.png', 'rb')
		bot.send_photo(message.chat.id, img , caption=f'Siz kiritgan *{soz}* so\'ziga QR kod rasm tayyor', parse_mode='MarkDown')
	except:
		bot.reply_to(message,'QR Kod yaratish uchun\n\n`/qr Salom`\n\nShu ko\'rinishda yuboring''', parse_mode='MarkDown')



@bot.message_handler(content_types = ['photo'])
def read(message):
	raw = message.photo[0].file_id
	path = raw+".jpg"
	file_info = bot.get_file(raw)
	downloaded_file = bot.download_file(file_info.file_path)
	with open('qr.png','wb') as new_file:
		new_file.write(downloaded_file)
	text = read_qr('qr.png')
	bot.reply_to(message,f"""🔣QR KODdagi Matn:⤵️\n\n`{text}`\n\n🎯By: @iCoderNet""",parse_mode='MarkDown')
bot.infinity_polling()