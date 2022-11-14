import qrcode
img = qrcode.make("https://github.com/Faizcodess")
img.save("qrcodeimage.jpg")