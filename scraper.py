import requests
from bs4 import BeautifulSoup
import smtplib
from secret import secret

# MIDI controller i want to check price on!
URL = 'https://www.amazon.ca/Akai-Professional-MPK-Keyboard-Controller/dp/B00IJ6QAO2/ref=sr_1_3?keywords=MIDI+controller&qid=1564411708&s=electronics&sr=1-3'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
ori_price = 140


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    price_float = float(price[5:])
    print(title.strip())
    print(price_float)
    if(price_float < ori_price):
        print("price has fell down! Sending email...")
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('hsyuting@gmail.com', secret)
    subject = 'Price fell down! Must be a Sale!'
    body = "Check the amazon link to see the price now! https://www.amazon.ca/Akai-Professional-MPK-Keyboard-Controller/dp/B00IJ6QAO2/ref=sr_1_3?keywords=MIDI+controller&qid=1564411708&s=electronics&sr=1-3"
    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'hsyuting@gmail.com',
        'hsyuting@gmail.com',
        msg
    )
    print("Email has been set!")
    server.quit()


check_price()
