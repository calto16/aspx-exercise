import requests

# Set the URL of the HTML site
url = "https://ceoelection.maharashtra.gov.in/searchlist/"
url2 = "https://ceoelection.maharashtra.gov.in/searchlist/Captcha.aspx"

# Set the form data for the POST request
form_data = {
    "__EVENTTARGET": "ctl00$Content$AssemblyList",
    "__EVENTARGUMENT": "",
    "__LASTFOCUS": "",
    "__VIEWSTATE": "j2rJCP1qJHW1p3g4c0Q1v8lnHv2qydktzgh1C2BG/M3KgZ9+ZJz596ripPy3H+IKmeHtmQYLdqI7762EWBijyUwfWHsKDpIThjXoDLXlRNppXMGHE227dSsaDN5SBBJFgs/e0g4wrhcC/GNMT4Wcxo6InU1dGD2QOPqADzdA7G1KMjUKLPQNCT+ePuMUBrwGPjsbrIuJ01dJ42SybuS+bq3tV0LeMabJicXPrnT/HTsWuKzj3VFsOJmu5MM/EQsediB0kjbtdQQsXqAlOMTqGE9AI6GWFKakFmenCkK9+oT2eW2HOVku/92nF7SVPKIvstBFeC3tlCQkeB/zY+qZOXZ2ut5VQcXEZlH8W74nO7tPOoNUFWxffXix4FfBLbk7uXqy5ArX/AB81gsKSu7hx/z7BPR57XaDRVr4BoxIcxNmdIGu+tvRSPfo/mrFTpkNSZfCRXtctGfc8JJcaSfnn4HyezoRNMMQaU/TTGlZ+g4SX5op7K6Lkp8iwJonow4qr2C0ep4AK0sp8oGsvcVHfC3d6F3GSNafjheQTr0kfJpSBmcYPFRVVBbViLPVQRGTHxBOMJxhCn9ej0hghnosgXCFWJepGELrD4yfqAueWo4Ztd45jtMrylHSabDfPFhAIoQOTWsO6gYU6UUKDsEi5oz1cEyTmQwrIJh54ntWu/DAHb3E92hnOUdVZRsFqervXATXkmkr8senvqu4UcGezgcq2SMlCD+FExArHHn13yTLe/2SxpQlp7g0v/4xtSiKDc0AyS5GV2NDtxyNuKtY4AX1vHYkLrTWlhd/m/hq4ruPlCr7QVGBHxWml8fyDs7JiEs+nWa16es+tahbLqzKvTWQMhqVkuel1UTv1cLorHrlyv7dnP9sJEf5BiyhP/t9Sk6Q7ldMHqPgJZlPK1p1rmavvnJdoi9SHvCh37UD/YmH73R+gq3I6U+Oc0x9Ek8lxvHEcA0rZJkue9BdJ1ajKafX53AztWXF4SRi01BL1s8GMRMECh0EYV4Hsfx0ntQAc/wFszGe44HSQFba734IcL67H2rYj2vYlLtKiOZUanaio3NMbZ57UgcgeuUUlhFJxAeWnGCG7hFJGyZ7NxhQtaUpJvCGTeEm8MDIgnsoXlXk66OM/HWXOviQjo217JDhqN5OM2MvV4uClsGbUwp4ISleiQ1wtP77WP6+VB04flVd/KCoHHYbNSXfzCCc9LUFxoqtoLj9+J3Oy0vz9hLBYlUtpK16kfwGYnu5R9c2WFN8mroaOPfJptnrAKIC3Bu+Yjs/iqNtjPT1AO9c48hH5uFGJE/xY7j/9n8x0hLI/woHBL8Sji+3v8tf6GPWVH04PAxvY5j40R6HNtl1am+l8w==",
    "__VIEWSTATEGENERATOR": "85D78299",
    "__VIEWSTATEENCRYPTED": "",
    "__EVENTVALIDATION": "diV4UVQAazRg+rnkxpKvSZYh1sPLfrGiXGOJNRiU/qzrYLc9H7gjaD4U0m7otQDABoRaCM+43L4u+08qBHtg2+OLdWyKSDp6c5VuqhnSXl/nnUYW0R3fMO/I2yfzCgoPY4k2NPv0Bakdu1mL7rhfb98wK2q1/GGmMe9Vt+KQ2L+ao6SyiLd6fbLvhyjXGNwUOnOQY07WY8Ssjy45YDCNgJo0/AjkK3QD2zT0SrXIHdLl9xSElm5Q69SETNv3fb/h3DYEuIpxUfG+/omBIscBeWB/c4Z2ws2EIeaWFOdFDh2nW7CUOVDagqOZR37wR4MIw477nAflW6CmoQm7Qqsjf2rMt4sY61AthmQALg9SQYX7QYK0ys6nCatuZf0gIZZgkmrbqzyLy4d2/Uq3fe2BWXIhryAnozVhdJM7EqvACUNbLEaUh6UwNtRvr/cZNHrV6PVvtuKLLpZoG7H4WG3aU+VbfhNjJbAiC5t6KhWkiRD2aXdKktYvUCOBtkNyCZkrLCzNwqMsgxSiA4PYhKlcovVjsHOCJuLktIfb/QfnjtQWGMPTK4mb74DirujFjiTJkHwhZzXVDGfE0RwIg9ZgyJMPhMRKKbmk8IaZ+X2eENpUruRFOSz17MstDchwrQqx+wH04VhfXC9akMnzd/CSXAK0FuW5IGec0sw7QOgzZwlSbCBqyn/ZgYOdgP32vCMp9yRUcqSEqnIRyYs1xt5EvXh/bU2kligQctMaX9hj9SBTCPKn2kmKsaLHuhXPsrCpWrgRsAxew4/cKpcVIfGq/gH5frFmpRg6oyHTRVwLI8Kgy7huWOjS4pAltb6gUvZvqx+pdnstKFDn2cfvCNBO0EZ9D7lMgv8jWn/vqEl4keCWpNB2UnguMw1idO0D+OxfoIfv3xc+AYnrRR8eVb5cRjsaP1MPOpPTC3vig3NIoiqLfVGtXcBLG9UKohY1sV4OmGv08d5RqGFMg/lT20y4TDhsIfXbZ5rB/n6SlEwgL1HpFYbk0KWPgMk5KqNe1YvweKu+keFdYZtJRsrOqQ+oYK3vTc/TJP2+KirkQoHvCUVHGA727/My1M7yFqlu4vQB0p/pBtgKyz/DnhhcdxFfZ0yOgSA7comhbSxBvNffb774hpHviNEXTpOcNK8uCpY+OHGV5Qp9NePvUZHX3Lk91/qwBxB0AQjA9S4GzHXGsiCOxdx70yUeCIsUgNO01Hl0Mu1vM6w1jfa2NZ8VTSnatXwx3IDqkRqZ9gsCH+2ULSe2moKJN0/y9+Wrc816/mPJ8+LvxP32ASUjHA+Ti7zKG58rE22NAB5ooDw0snoK0Kw=",
    "ctl00$Content$DistrictList": "1",
    "ctl00$Content$AssemblyList": "1",
    "ctl00$Content$listrollrevision": "1",
    "ctl00$Content$LangTypepdf": "1",
    "ctl00$Content$PartList": "",
    # "ctl00$Content$txtcaptcha": "7Gnrjc",
    # "ctl00$Content$OpenButton": "Open PDF"
}

# Set the request headers
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "19403",
    "Cookie": "_ga=GA1.3.1814187270.1683026567; _ga_ZY7C73RHJX=GS1.1.1684989268.1.1.1684989343.0.0.0; ASP.NET_SessionId=1kyzl50lpwpwqosrzjuilf1l",
    "Host": "ceoelection.maharashtra.gov.in",
    "Origin": "null",
    "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Microsoft Edge\";v=\"114\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37"
}

# Send a POST request to the site with the form data and headers
response = requests.post(url, data=form_data, headers=headers)
# response2 = requests.post(url2,  headers=headers)
# Print the HTTP response
print(response.text)

# filename = "Captcha.png"  

# with open(filename, "wb") as file:
#     for chunk in response2.iter_content(chunk_size=4096):
#         file.write(chunk)

# print(f"Image saved as {filename}")