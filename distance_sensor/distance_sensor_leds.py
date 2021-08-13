#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys

try:
	distance = 0
	while True:
     		GPIO.setmode(GPIO.BOARD)

      		PIN_TRIGGER = 7
      		PIN_ECHO = 11
		PIN_LED_CORRECTO = 13
		PIN_LED_CERCA = 15

      		GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      		GPIO.setup(PIN_ECHO, GPIO.IN)
		GPIO.setup(PIN_LED_CORRECTO, GPIO.OUT)
		GPIO.setup(PIN_LED_CERCA, GPIO.OUT)
      		GPIO.output(PIN_TRIGGER, GPIO.LOW)

      		print "Waiting for sensor to settle"

      		time.sleep(2)

      		print "Calculating distance"

     		GPIO.output(PIN_TRIGGER, GPIO.HIGH)

      		time.sleep(0.00001)
      		GPIO.output(PIN_TRIGGER, GPIO.LOW)
      		while GPIO.input(PIN_ECHO)==0:
            		pulse_start_time = time.time()
      		while GPIO.input(PIN_ECHO)==1:
            		pulse_end_time = time.time()
      		pulse_duration = pulse_end_time - pulse_start_time
      		distance = round(pulse_duration * 17150, 2)
      		if distance >= 20:
			if distance < 100:
				print "Distance:",distance,"cm"
			else:
				print "Distance:",distance/100,"m"
			GPIO.output(PIN_LED_CORRECTO, True)
			time.sleep(1)
			GPIO.output(PIN_LED_CORRECTO, False)
		else:
			GPIO.output(PIN_LED_CERCA,True)
			print "---------------------------------------------"
			print "Usted se encuentra muy cerca alejese un poco."
			print "---------------------------------------------"
			time.sleep(1)
			GPIO.output(PIN_LED_CERCA,False)
except:
	print sys.exc_info()

finally:
      GPIO.cleanup()
