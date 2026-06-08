from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

my_email = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD")

header = {"Accept-Language": "en-US,en-IN;q=0.9,en;q=0.8,ta;q=0.7,en-GB;q=0.6",
          "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

URL = "https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=asc_df_B01NBKTPTS?mcid=911a75653bdf3ead901a2a09a0a79538&tag=hyprod-20&linkCode=df0&hvadid=693071387707&hvpos=&hvnetw=g&hvrand=14352099867958722105&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9014243&hvtargid=pla-310773953640&th=1"
response = requests.get(URL,headers=header)
website = response.text
soup = BeautifulSoup(website, "html.parser")
get_price = soup.find(name= "span", class_="aok-offscreen")
price = get_price.getText().split()[0]
final_price = price.replace("$","")

get_title = soup.find(name="span" , id="productTitle").getText()
x=get_title.split()
title = ''.join(x)


if float(final_price) <= 100:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email, password)
    message = f"subject:Amazon Price Alert \n\n {title} {price}\n{URL}".encode('UTF-8')
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg= message
    )





