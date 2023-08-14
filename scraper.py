import requests
from bs4 import BeautifulSoup
import smtplib

url = 'https://www.amazon.in/Portronics-Vertical-Advanced-Ergonomic-Adjustable/dp/B0BTPXTYYZ/ref=sr_1_12_sspa?crid=2T5J607RQJNNS&keywords=bluetooth+mouse&qid=1691946718&sprefix=bluetooth+mouse%2Caps%2C220&sr=8-12-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&psc=1'

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' 
    
    }

def check_email():
# "upgtnndenhlxdlfw"
    page = requests.get(url, headers=headers)# this returns all the data from that website

    soup = BeautifulSoup(page.content, 'html.parser') # this allows us to extract particular(individual) data from the website

    price= soup.find(id='acrCustomerReviewText').get_text() # this extracts the price(a-price-whole is the Div name that holds the price)
    converted_price = float(price[0:4])

    if(converted_price <828):
        send_mail()

    if(converted_price < 830):
        send_mail()

    print(converted_price)
    # price(converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()  # command sent by an email server
    server.starttls()
    server.ehlo()
    server.login('kaliraotaran@gmail.com', 'upgtnndenhlxdlfw')
    subject= 'Price fell down'  
    body='check the amazon link https://www.amazon.in/Portronics-Vertical-Advanced-Ergonomic-Adjustable/dp/B0BTPXTYYZ/ref=sr_1_12_sspa?crid=2T5J607RQJNNS&keywords=bluetooth+mouse&qid=1691946718&sprefix=bluetooth+mouse%2Caps%2C220&sr=8-12-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&psc=1'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail('kaliraotaran@gmail.com', 'tarankalirao1@gmail.com', msg)

    print('message sent ')
    server.quit()




check_email()