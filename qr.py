import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

def qr_code(text):
	import qrcode
	img = qrcode.make(text)
	img.save('code.png')


def read_qr(file):
	data = decode(Image.open(file))
	return data[0].data.decode("utf-8")
