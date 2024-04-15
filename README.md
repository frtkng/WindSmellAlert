# Effect

https://www.youtube.com/watch?v=L844oqEV11E

# UseCase
![image](https://github.com/frtkng/WindSmellAlert/assets/35648235/eaa7da50-7db2-49b0-b6f0-8ddaf6cb745b)

# Design
![image](https://github.com/frtkng/WindSmellAlert/assets/35648235/bbe44fc9-c2ac-4277-8ffc-4a04396a3b67)


# How to use(Linux):
1) commannd "crontab -e" in terminal
2) write down this description
15,45 * * * * export EMAIL_ADDRESS='your-email@gmail.com'; export EMAIL_PASSWORD='your-password'; export TO_ADDRESSES="xxx.com,xxx.com"; export LATITUDE="yyy"; export LONGITUDE="yyy"; /usr/bin/python3 /home/pi/WindSmellAlert.py >> /home/pi/cron.log 2>&1

