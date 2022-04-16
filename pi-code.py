from pickle import TRUE
import RPi.GPIO as GPIO
import time
t=30
def countdown(t):
	
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1

PIR = 29
LED_R = 11
LED_G = 13
LED_Y = 15
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LED_G,GPIO.OUT)
GPIO.setup(LED_Y, GPIO.OUT)
GPIO.output(LED_G, GPIO.HIGH)
GPIO.output(LED_Y, GPIO.LOW)


if(GPIO.input(PIR)==TRUE):
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_Y, GPIO.HIGH)
        countdown()
        if(GPIO.input(PIR)==True):
                GPIO.output(LED_G, GPIO.LOW)
                GPIO.output(LED_Y, GPIO.LOW)
                GPIO.output(LED_R, GPIO.HIGH)
else:
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_Y, GPIO.LOW)