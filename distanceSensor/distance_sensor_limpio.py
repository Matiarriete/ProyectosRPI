#!/usr/bin/python
import RPi.GPIO as GPIO
import time

try:
      GPIO.setmode(GPIO.BOARD)

      PIN_TRIGGER = 7
      PIN_ECHO = 11
      PIN_RELAY = 13
      PIN_LED = 15

      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN)
      GPIO.setup(PIN_RELAY, GPIO.OUT)
      GPIO.setup(PIN_LED, GPIO.OUT)

      GPIO.output(PIN_LED, GPIO.LOW)
      GPIO.output(PIN_RELAY, GPIO.HIGH)
      GPIO.output(PIN_TRIGGER, GPIO.LOW)
      while True:
      	print "Waiting for sensor to settle"

      	time.sleep(1)

      	print "Calculating distance"
  	GPIO.output(PIN_LED, GPIO.LOW)
	GPIO.output(PIN_RELAY, GPIO.HIGH)
     	GPIO.output(PIN_TRIGGER, GPIO.HIGH)

      	time.sleep(0.00001)

      	GPIO.output(PIN_TRIGGER, GPIO.LOW)

      	while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
      	while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()

      	pulse_duration = pulse_end_time - pulse_start_time
      	distance = round(pulse_duration * 17150, 2)
      	if distance > 20:
		if distance < 100:
      			print "Distance:",distance,"cm"
		else:
			print "Distance:", distance/100,"m"
      	else: 
		print "------------------------------"
		print "Esta muy cerca alejese un poco"
		print "------------------------------"
		GPIO.output(PIN_RELAY, GPIO.LOW)
		GPIO.output(PIN_LED, GPIO.HIGH)

finally: GPIO.cleanup()
