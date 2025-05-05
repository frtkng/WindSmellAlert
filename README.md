# WindSmellAlert

WindSmellAlert is a Python tool that monitors wind direction from weather forecasts and sends email alerts when winds might carry unpleasant odors from specific directions. It helps you know when to close your windows to avoid bad smells.

## Demo

https://www.youtube.com/watch?v=L844oqEV11E

## Use Case
![image](https://github.com/frtkng/WindSmellAlert/assets/35648235/eaa7da50-7db2-49b0-b6f0-8ddaf6cb745b)

## System Design
![image](https://github.com/frtkng/WindSmellAlert/assets/35648235/bbe44fc9-c2ac-4277-8ffc-4a04396a3b67)

## Features

- **Real-time Wind Direction Monitoring**: Fetches weather data from weathernews.jp
- **Smart Alert System**: Different alert levels based on wind direction
  - **Warning Level**: East-Northeast (東北東) directions
  - **Caution Level**: Northeast (北東), East (東), and No Direction (方向なし)
- **Email Notifications**: Sends alerts to multiple email addresses
- **Customizable Location**: Works with any location by setting latitude and longitude

## How It Works

1. The script fetches weather data from weathernews.jp for your specified location
2. It analyzes the wind direction for the next hour
3. If the wind is coming from directions that might carry unpleasant odors:
   - Warning alert for East-Northeast direction
   - Caution alert for Northeast, East, and No Direction
4. Email notifications are sent to the configured addresses

## Wind Direction Mapping

The application maps wind direction images from the weather service to actual directions:

| Image Code | Wind Direction |
|------------|---------------|
| wind_1_03.png | East-Northeast (東北東) - Warning Level |
| wind_1_02.png | Northeast (北東) - Caution Level |
| wind_1_04.png | East (東) - Caution Level |
| wind_0_00.png | No Direction (方向なし) - Caution Level |
| (and other directions) | (No alerts sent) |

## Requirements

- Python 3
- Required Python libraries: `smtplib`, `beautifulsoup4`, `requests`, `email`
- Gmail account for sending notifications (with "Less secure app access" enabled or an App Password)

## Environment Variables

The following environment variables must be set:

- `MY_ADDRESS`: Your Gmail address to send notifications from
- `EMAIL_PASSWORD`: Your Gmail password or app password
- `TO_ADDRESSES`: Comma-separated list of email addresses to receive notifications
- `LATITUDE`: Latitude of your location
- `LONGITUDE`: Longitude of your location

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/frtkng/WindSmellAlert.git
   ```

2. Install required packages:
   ```
   pip install beautifulsoup4 requests
   ```

## How to Use (Linux)

1. Open the terminal and edit your crontab:
   ```
   crontab -e
   ```

2. Add the following line to run the script every 15 and 45 minutes of each hour:
   ```
   15,45 * * * * export MY_ADDRESS='your-email@gmail.com'; export EMAIL_PASSWORD='your-password'; export TO_ADDRESSES="email1@example.com,email2@example.com"; export LATITUDE="your-latitude"; export LONGITUDE="your-longitude"; /usr/bin/python3 /path/to/WindSmellAlert.py >> /path/to/cron.log 2>&1
   ```
   
3. Replace the example values with your actual email, password, recipient addresses, and location coordinates

## Troubleshooting

- Make sure all environment variables are properly set
- Check your cron.log file for any error messages
- For Gmail, you may need to create an App Password or enable Less secure app access
- Verify your internet connection to ensure the script can fetch weather data

