import qrcode

data = "https://www.python.org"
img = qrcode.make(data)
img.save("python_qr.png")
print("QR-код сохранён как python_qr.png")
