# Must download prqrcode package
import pyqrcode

def generate_qrcode(url):
    qrcode = pyqrcode.create(url)
    qrcode.svg("qr-code.svg", scale = 10)
    qrcode.eps("qr-code.eps", scale = 2)
    qrcode.show()

user_url = input("Enter your url to convert to a qr code: ")
generate_qrcode(user_url)

