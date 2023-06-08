from PIL import Image
import pytesseract

image_path = "C:/Users/Tushar/Desktop/Work/Captcha.png"
image = Image.open(image_path)


text = pytesseract.image_to_string(image)
print(text)