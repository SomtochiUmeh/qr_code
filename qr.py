import qrcode
from PIL import Image
import cv2

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data('https://github.com/SomtochiUmeh')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('github.jpg')

# https://github.com/SomtochiUmeh

im=cv2.imread("github.jpg")
det=cv2.QRCodeDetector()
val, pts, st_code=det.detectAndDecode(im)
print(val)