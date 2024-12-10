import qrcode
import qrcode as qr
img = qr.make("https://www.linkedin.com/in/muhammad-saim-shafi/")
img.save("saimshafi's_Linkedin.png")
import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=4, )
qr.add_data("https://www.linkedin.com/in/muhammad-saim-shafi/")
qr.make(fit=True)
img= qr.make_image(fill_color="blue", back_color="white")
img.save("saimshafi's_Linkedin.png")