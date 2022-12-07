# Must download prqrcode package
import pyqrcode

qrcode_link = "https://store.steampowered.com/app/2149290/Demo_Grounds/"

def generate_qrcode(url):
    qrcode = pyqrcode.create(url)
    qrcode.svg("qr-code.svg", scale = 10)
    qrcode.eps("qr-code.eps", scale = 2)
    qrcode.show()


generate_qrcode(qrcode_link)

