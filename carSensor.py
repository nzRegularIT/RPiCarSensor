#!/usr/bin/python
import RPi.GPIO as GPIO
import time
#from time import localtime, strftime
from datetime import datetime
#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
TRIG = 4
ECHO = 18
GREEN = 17
YELLOW = 27
RED = 22
maxDistance = 400
errorDistance = 2000
initialApproachDistance = 200
greenDistance = 100
greenYellowDistance = 75
yellowDistance = 50
#yellowRedDistance =
redDistance = 20
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(YELLOW,GPIO.OUT)
GPIO.setup(RED,GPIO.OUT)
def noLights():
  GPIO.output(GREEN, GPIO.LOW)
  GPIO.output(YELLOW, GPIO.LOW)
  GPIO.output(RED, GPIO.LOW)
def allLightsFlash():
  GPIO.output(GREEN, GPIO.HIGH)
  GPIO.output(YELLOW, GPIO.HIGH)
  GPIO.output(RED, GPIO.HIGH)
  time.sleep(0.1)
  GPIO.output(GREEN, GPIO.LOW)
  GPIO.output(YELLOW, GPIO.LOW)
  GPIO.output(RED, GPIO.LOW)
def allLightsSteady():
  GPIO.output(GREEN, GPIO.HIGH)
  GPIO.output(YELLOW, GPIO.HIGH)
  GPIO.output(RED, GPIO.HIGH)
def greenLight():
  GPIO.output(GREEN, GPIO.HIGH)
  GPIO.output(YELLOW, GPIO.LOW)
  GPIO.output(RED, GPIO.LOW)
def greenYellowLight():
  GPIO.output(GREEN, GPIO.HIGH)
  GPIO.output(YELLOW, GPIO.HIGH)
  GPIO.output(RED, GPIO.LOW)
def yellowLight():
  GPIO.output(GREEN, GPIO.LOW)
  GPIO.output(YELLOW, GPIO.HIGH)
  GPIO.output(RED, GPIO.LOW)
def yellowRedLight():
  GPIO.output(GREEN, GPIO.LOW)
  GPIO.output(YELLOW, GPIO.HIGH)
  GPIO.output(RED, GPIO.HIGH)
def redLight():
  GPIO.output(GREEN, GPIO.LOW)
  GPIO.output(YELLOW, GPIO.LOW)
  GPIO.output(RED, GPIO.HIGH)
def getDistance():
  GPIO.output(TRIG, False)
  time.sleep(0.5)
  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)
  while GPIO.input(ECHO) == False:
    start = time.time()
  while GPIO.input(ECHO) == True:
    end = time.time()
  signal_time = end-start
  #distance = round((signal_time / 0.000058),1)
  distance = round((signal_time * 17150),1)
  return distance
try:
  while True:
    distance = getDistance()
    print "[INFO][",datetime.now().strftime("%d/%m %H:%M:%S.%f")[:-3],"] Distance in cm:",distance
    if distance > errorDistance:
      allLightsFlash()
    elif distance > maxDistance:
      noLights()
    elif maxDistance > distance > initialApproachDistance:
      allLightsSteady()
    elif distance > greenDistance:
      greenLight()
    elif distance > greenYellowDistance:
      greenYellowLight()
    elif distance > yellowDistance:
      yellowLight()
    elif distance > redDistance:
      yellowRedLight()
    elif distance <= redDistance:
      redLight()
    time.sleep(0.1)
except KeyboardInterrupt:
  # here you put any code you want to run before the program
  # exits when you press CTRL+C
  print "\nCtrl-C pressed, exiting"

#except:
  # this catches ALL other exceptions including errors.
  # You won't get any error messages for debugging
  # so only use it once your code is working
  #print "Other error or exception occurred!"

finally:
  print "\nCleaning up GPIO"
  GPIO.cleanup() # this ensures a clean exit
