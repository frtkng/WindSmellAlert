import smtplib
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# 風向きを示す画像と実際の風向きのマッピング
wind_mapping = {
    "wind_0_00.png": "方向なし",
    "wind_1_01.png": "北北東",
    "wind_1_02.png": "北東",
    "wind_1_03.png": "東北東",
    "wind_1_04.png": "東",
    "wind_1_05.png": "東南東",
    "wind_1_06.png": "南東",
    "wind_1_07.png": "南南東",
    "wind_1_08.png": "南",
    "wind_1_09.png": "南南西",
    "wind_1_10.png": "南西",
    "wind_1_11.png": "西南西",
    "wind_1_12.png": "西",
    "wind_1_13.png": "西北西",
    "wind_1_14.png": "北西",
    "wind_1_15.png": "北北西",
    "wind_1_16.png": "北",
}

MY_ADDRESS = os.environ.get('MY_ADDRESS')
PASSWORD = os.environ.get('EMAIL_PASSWORD')
TO_ADDRESSES = os.getenv('TO_ADDRESSES').split(',')

def fetch_data():
    latitude = os.environ.get('LATITUDE')
    longitude = os.environ.get('LONGITUDE')
    URL = f'http://weathernews.jp/onebox/{latitude}/{longitude}/temp=c&lang=en'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup, URL

def get_wind_info(weather_row):
    wind_info_element = weather_row.find('p', {'class': 'wTable__item w'})
    wind_direction_element = wind_info_element.find('i', {'class': 'wdir'})
    wind_direction_url = wind_direction_element.find('img').get('src')
    wind_direction_img = wind_direction_url.split("/")[-1]
    wind_direction = wind_mapping.get(wind_direction_img, "Unknown direction")
    wind_speed = wind_info_element.text.strip('m')
    return wind_direction, wind_speed

def send_email(next_m, next_d, next_h, wind_direction, wind_speed, URL):
    
    if wind_direction in ["東北東"]:
        sub_text = f'風の臭い 警報'
        msg_text = f'風の臭いが来るかもしれません。すぐに家の窓を閉めてください！\n {next_m}月{next_d}日{next_h}時 風向き: {wind_direction}, 風速: {wind_speed}m/s \n ※この通知はウェザーニューズの情報を利用しています \n {URL}'
    
    if wind_direction in ["北東","東","方向なし"]:
        sub_text = f'風の臭い 注意報'
        msg_text = f'風の臭いが来るかもしれません。\n {next_m}月{next_d}日{next_h}時 風向き: {wind_direction}, 風速: {wind_speed}m/s \n ※この通知はウェザーニューズの情報を利用しています \n {URL}' 
    
    #create server
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    server.starttls()

    # Login Credentials for sending the mail
    server.login(MY_ADDRESS, PASSWORD)

    # send the message via the server.
    for recipient in TO_ADDRESSES:
        
        msg = MIMEMultipart()       # create a message
        
        msg['To'] = recipient
        msg['From']=MY_ADDRESS
        msg['Subject'] = sub_text
        msg.attach(MIMEText(msg_text, 'plain'))
        
        server.send_message(msg)

    server.quit()

def get_next_hour():
    now = datetime.now()
    one_hour_later = now + timedelta(hours=1)

    return one_hour_later.month, one_hour_later.day, one_hour_later.hour

def get_next_hour_weather(soup):
    swc2 = soup.find('div', {'class':'switchContent__item act', 'data-num':'2'})
    wTable_row = swc2.find_all('div', {'class':'wTable__row'})
    next_m, next_d, next_h = get_next_hour()
    for windinfo_hour in wTable_row:
        hour_w = windinfo_hour.find('p', {'class':'wTable__item time'}).text
        if hour_w == str(next_h):
            wind_direction, wind_speed = get_wind_info(windinfo_hour)
            return next_m, next_d, next_h, wind_direction, wind_speed
    return None,None,None,None,None

def main():
    soup, URL = fetch_data()
    next_m, next_d, next_h, wind_direction, wind_speed = get_next_hour_weather(soup)
    if next_h is not None:
        print(f'{next_m}月{next_d}日{next_h}時 風向き: {wind_direction}, 風速: {wind_speed}m/s')
        if wind_direction in ["北東","東","東北東","方向なし"]:
            send_email(next_m, next_d, next_h, wind_direction, wind_speed, URL)
            print(f'メール送信しました')

if __name__ == '__main__':
    main()
