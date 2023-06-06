# WindSmellAlert

How to use(Linux):
1) commannd "crontab -e" in terminal
2) write down this description
15,45 * * * * export EMAIL_ADDRESS='your-email@gmail.com'; export EMAIL_PASSWORD='your-password'; export TO_ADDRESSES="xxx.com,xxx.com"; export LATITUDE="yyy"; export LONGITUDE="yyy"; /usr/bin/python3 /home/pi/WindSmellAlert.py >> /home/pi/cron.log 2>&1
