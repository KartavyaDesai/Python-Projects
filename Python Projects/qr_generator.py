#Quick Response Code Generator
import pyqrcode as qr
link = input("Enter the link to generate QR CODE: ")
qr_code = qr.create(link)
qr_code.svg("qr_1.svg", scale=8)
