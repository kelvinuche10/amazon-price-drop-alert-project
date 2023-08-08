import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

# sender_email = 'your_email@example.com'
# receiver_email = 'recipient@example.com'
# subject = 'Subject of the Email'
# body = 'This is the body of the email.'


endpoint = "https://www.amazon.com/ANMESC-Quad-Core-Processors-Computers-Bluetooth/dp/B0CC1XWGD6/ref=sr_1_1_sspa?keywords=laptop&qid=1691494482&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

header = {
	'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
	'Accept-Language': 'en-US,en;q=0.9'
}

response = requests.get(url=endpoint, headers=header)
page = response.text


soup = BeautifulSoup(page, 'lxml')
price = int(soup.find(name='span', class_="a-price-whole").getText().split('.')[0])
product_name = soup.find(name='h1', id='title').getText().split()

my_email = 'amkelvinuche@gmail.com'
subject = 'AMAZON price alert!'
body = f'''{product_name} just dropped to {price},\n'
 			'click {endpoint} to make your purchase'''
smtp_password = 'fezrcyvsvdrxoklt'


with smtplib.SMTP('smtp.gmail.com') as connection:
	connection.starttls()  # Start TLS encryption
	connection.login(user=my_email, password=smtp_password)
	if price < 400:
		connection.sendmail(from_addr=my_email, 
				to_addrs=my_email, 
				msg=f'Subject: {subject} \n\n {body} ')

print('code completed')