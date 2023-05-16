#!/usr/bin/env python3

import time
import re
import smtplib
import requests
from bs4 import BeautifulSoup

site = "https://in.bookmyshow.com/buytickets/x-men-apocalypse-3d-hyderabad/movie-hyd-ET00029820-MT/"  # Replace this with your movie and city URL
date = "20160525"  # Replace the date with the date for which you'd like to book tickets! Format: YYYYMMDD
site = site + date
venue = 'CPCL'  # This can be found by inspecting the element data-id for the venue where you would like to watch
show = '11:30 AM'  # Just replace it with your preferred show timing
delay = 300  # Time gap in seconds between 2 script runs

TO = 'test@gmail.com'  # Mail ID to which you want to get the alerts to
GMAIL_USER = 'sample_username@gmail.com'
GMAIL_PASS = 'sample_password'
SUBJECT = 'Tickets are now available, Book fast'
TEXT = f'The tickets are now available for the {show} show at the venue {venue}'

def send_email():
    print("Sending Email")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtpserver:
        smtpserver.login(GMAIL_USER, GMAIL_PASS)
        header = f'To: {TO}\nFrom: {GMAIL_USER}\nSubject: {SUBJECT}\n'
        print(header)
        msg = f'{header}\n{TEXT}\n\n'
        smtpserver.sendmail(GMAIL_USER, TO, msg)

while True:
    try:
        with requests.Session() as session:
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'
            }
            req = session.get(site, headers=headers)
            req.raise_for_status()
            soup = BeautifulSoup(req.content, 'html.parser')
            soup2 = soup.find_all('div', {'data-online': 'Y'})
            line = str(soup2)
            soup3 = BeautifulSoup(line, 'html.parser')
            soup4 = soup3.find_all('a', {'data-venue-code': venue})
            line1 = str(soup4)
            soup5 = BeautifulSoup(line1, 'html.parser')
            soup6 = soup3.find_all('a', {'data-display-showtime': show})
            line2 = str(soup6)
            result = re.findall('data-availability="A"', line2)
            if len(result) > 0:
                print("Available")
                send_email()
            else:
                print("Not available yet")
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)

    time.sleep(delay)
