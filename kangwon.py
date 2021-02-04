from datetime import datetime
from bs4 import BeautifulSoup
import urllib.request
import telegram

def samcheok_notify():
  data = []
  
  samcheok_url = 'https://www.kangwon.ac.kr/www/selectBbsNttList.do?bbsNo=81&key=298&searchCtgry=%EC%A0%84%EC%B2%B4%40%40%EC%82%BC%EC%B2%99%40%40%EC%82%BC%EC%B2%99%C2%B7%EB%8F%84%EA%B3%84&'
  html = urllib.request.urlopen(samcheok_url).read()
  soup = BeautifulSoup(html, 'html.parser')

  infos = soup.find("tbody", class_="tb").findAll("tr")
  for info in infos:
    day = info.find(class_="date").text.strip()
    title = info.find("a").text.strip()
    url = "https://www.kangwon.ac.kr/www" + info.find("a").get("href")[1:]
    mag = title + url
    data.append([day, mag])
  
  return data

my_token = 'token'   #토큰을 변수에 저장합니다.
channel_id = 
bot = telegram.Bot(token = my_token)   #bot을 선언합니다.

today = datetime.now().strftime("%Y.%m.%d") 

notify = samcheok_notify()

for day, mag in notify:
  if today == day:
    bot.sendMessage(chat_id = channel_id, text= mag)





  