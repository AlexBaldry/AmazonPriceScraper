import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'YOUR AMAZON LINK HERE'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price < 1.700):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price > 1.700):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('EMAIL HERE', 'GOOGLE AUTH HERE')

    subject = 'Price fell down!'
    body = 'Check the amazon link AMAZON LINK HERE'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'YOUR EMAIL',
        'YOUR EMAIL',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()


while(True):
    check_price()
    time.sleep(500 * 60)
