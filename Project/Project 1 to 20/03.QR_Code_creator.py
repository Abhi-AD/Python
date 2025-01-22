import qrcode as qr

input_url = input("Enter the Url: ")
img = qr.make(input_url)
img.save("qrcode.png")
