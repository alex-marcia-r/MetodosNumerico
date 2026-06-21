import qrcode 

url="https://docs.google.com/forms/d/e/1FAIpQLSdNMWnTIDE3g4OmDu7ynvY_yZc6tixymvHMmWRB9MXU4aKIqg/viewform?usp=sharing"
qr = qrcode.QRCode( version=1, box_size= 28, border= 4)
qr.add_data(url)
qr.make(fit=True)

imagen= qr.make_image()
imagen.save("encuesta.png")