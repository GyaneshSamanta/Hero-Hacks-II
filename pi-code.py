import RPi.GPIO as GPIO

PIR = 29
LED = 32
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR, GPIO.IN)	
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

while True:
    if(GPIO.input(PIR)):
        GPIO.output(LED, GPIO.HIGH)
    else:
        GPIO.output(LED, GPIO.LOW)