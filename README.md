# Chistulya project

Chistulya is our school project to build an autonomous street cleaning robot.

## Required
- Arduno UNO (or anouther ver.)
- - Adafruit Motor Shield L293D
- Raspberry Pi 3 (or better)
- - Stable wi-fi
- - Python 3.x
- - Linux module *cdc_acm*
- - USB camera

## Installation
1. Clone repo - ``` git clone https://github.com/braginantonev/chistulya```
2. Replace clonned folder to pi home - ``` mv chistulya /home/pi/ ```
3. Copy the chistulya service to systemd: ``` sudo cp chistulya.service /etc/systemd/system ```
4.  Reload systemd services: ``` sudo systemctl daemon-reload ```
5.  Start chistulya service (**Arduino must be connected to RPi by USB!**): ``` sudo systemctl enable chistulya```

 

