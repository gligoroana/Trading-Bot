

from time import sleep
from email.message import EmailMessage

from requests import get
import schedule
import smtplib

prag_1 = 5200.0
prag_2 = 7100.0
message_depasire_prag_1 = "pragul 1 a fost depasit"
message_depasire_prag_2 = "pragul 2 a fost depasit"

def get_bitcoin_price():
    
    response = get('https://www.bitstamp.net/api/ticker/').json()

    return float(response['last'])


def send_email(message):
    bitcoin_price = get_bitcoin_price()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("pythontest775@gmail.com", "Testpython775")

    msg=(f"Pragul a fost atins cu pretul {bitcoin_price}")
    server.sendmail("pythontest775gmail.com", "pythontest775@gmail.com", msg)
    server.quit()
def validate(price):

    if (price > prag_1) :
      send_email(message_depasire_prag_1)
    if (price < prag_2):
      send_email(message_depasire_prag_2)

while True:
  sleep(5)
  price = get_bitcoin_price()
  print (price)
  validate(price)
