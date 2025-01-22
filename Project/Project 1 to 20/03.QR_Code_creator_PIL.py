import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qrcodedata = input("Enter the Url: ")
qr.add_data(qrcodedata)
qr.make(fit=True)
img = qr.make_image(fill_color="white", back_color="blue")
img.save("qrcode.png")
