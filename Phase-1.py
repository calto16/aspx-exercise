# import requests
from PIL import Image
import pytesseract


# url = "https://ceoelection.maharashtra.gov.in/searchlist/Captcha.aspx"

# response = requests.get(url,stream=True)

# cookies = response.cookies

# for cookie in cookies:
#     print(f"{cookie.name}={cookie.value}")


# filename = "Captcha.png"  

# with open(filename, "wb") as file:
#     for chunk in response.iter_content(chunk_size=4096):
#         file.write(chunk)

# print(f"Image saved as {filename}")


image_path = "C:/Users/Tushar/Desktop/aspx exercise/Captcha.png"
image = Image.open(image_path)


text = pytesseract.image_to_string(image)
print(text)