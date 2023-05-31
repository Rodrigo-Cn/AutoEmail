!pip install bs4
!pip install requests

import requests
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def gett(url):
  x = requests.get(url)
  return x

url1 = 'https://www.fapesb.ba.gov.br/category/edital/'
x1 = gett(url1)
x2 = x1.content
site = BeautifulSoup(x2,'html.parser')
quadro = site.find('div', attrs={'class':'edital-item col-md-12'})
url = quadro.find('a')['href']
print(url)
xx1 = gett(url)
xx2 = xx1.content
site2 = BeautifulSoup(xx2,'html.parser')
quadro2 = site2.find('div', attrs={'class':'edital-sigle-block col-md-8'})
print(quadro2.text)
analisador = quadro2.text+'\nEdital: '+url

arquivo1 = open("dados.txt","r")
analisador2 = arquivo1.read()
arquivo1.close()

if analisador != analisador2:
  arquivo = open("dados.txt","w")
  arquivo.write(analisador)
  arquivo.close()

  msg = MIMEMultipart()
  msg['subject'] = 'Acabou de sair um novo edital da FAPESB'
  message = quadro2.text+'\nEdital: '+url
  msg['From'] = 'e-mail'
  msg['To'] = 'e-mail'
  msg.attach(MIMEText(message, 'plain'))

  server = smtplib.SMTP('smtp.gmail.com:587')
  server.starttls()
  server.login('your e-mail adress','your password google')
  server.sendmail(msg['From'],msg['To'],msg.as_string())
  server.quit()
