In this project i created a simple circuit with an RaspberryPi Zero and motion sensor that can detect movement. An LED will light up when movement is detected.

## Shema
![](motionsensor-schema.png)

## Install motion sensor
- Follow step by step
    - https://www.raspberrypi.org/documentation/installation/noobs.md
    - raspi-config (active ssh), apt-get update && apt-get dist-upgrade -y
    - modify /etc/dhcpcd.conf (only if you want a static ip address)
    - copy motionsensor.py => /home/pi/
    - install the raspberry pi zero simple circuit (schema example)
    - run script : python /home/pi/motionsensor.py
    - enjoy !
