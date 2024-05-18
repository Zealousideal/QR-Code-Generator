import qrcode as qr

#URL for which we want to make the QR of
img = qr.make("https://pythonhosted.org/PyQRCode/")

#Provide the name of the image you want to save of ith the extention
img.save("Docs_for_PyQRCode.png")

print(img)