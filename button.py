#!/usr/bin/python

import RPi.GPIO as GPIO
import time

BUTTON = 2

def main():
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # BUTTON

  while (1):
    if GPIO.input(BUTTON):
      print "Button pushed"
      time.sleep(1)

if __name__ == '__main__':
  main()

