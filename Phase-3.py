import requests

reqUrl = "https://ceoelection.maharashtra.gov.in/searchlist/ViewPDF.aspx"

headersList = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "_ga=GA1.3.1814187270.1683026567; _ga_ZY7C73RHJX=GS1.1.1684989268.1.1.1684989343.0.0.0; ASP.NET_SessionId=1kyzl50lpwpwqosrzjuilf1l",
    "Host": "ceoelection.maharashtra.gov.in",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37",
    "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Microsoft Edge\";v=\"114\"",
    "sec-ch-ua-mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
}

payload = ""

response = requests.request("GET", reqUrl, data=payload, headers=headersList)


# Specify the output file path and name
output_file = "response.pdf"

# Write the response content to a PDF file
with open(output_file, "wb") as file:
    file.write(response.content)

print("PDF file created successfully.")
