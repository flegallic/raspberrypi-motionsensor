#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# https://github.com/haxware/
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Detect movement using a PIR module
#
# Author : haxware
# Date   : 11/05/2019

# Import required Python libraries
import RPi.GPIO as GPIO
import time
import subprocess

# Use BCM GPIO references - instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
# Define GPIO to use on Pi
GPIO_PIR = 7
GPIO_LED = 21
# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)
GPIO.setup(GPIO_LED, GPIO.OUT)

Current_State  = 0
Previous_State = 0

try:
  print "Waiting for PIR..."

  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0    

  print "motion sensor is ready"
  # set led status on "OFF"
  GPIO.output(GPIO_LED,0)
    
  # Loop until users quits with CTRL-C
  while True :  
    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)
   
    if Current_State==1 and Previous_State==0:
      # PIR is triggered
      print "Motion detected!"
      # sent an email
      #subprocess.call(["/home/pi/mail.sh"])
      # set led status on "ON"
      GPIO.output(GPIO_LED, 1)
      # Record previous state
      Previous_State=1
    elif Current_State==0 and Previous_State==1:
      # PIR has returned to ready state
      print "motion sensor is ready"
      Previous_State=0
      GPIO.output(GPIO_LED, 0)
      
    # Wait for 10 milliseconds
    time.sleep(0.01)      
      
except KeyboardInterrupt:
  print "Quit" 
  # Reset GPIO settings
  GPIO.cleanup()
  
