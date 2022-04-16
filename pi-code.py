import RPi.GPIO as GPIO
import time

# Raspberry Pi Pin Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
PIR = 26
LED_Red = 13 # Warning LED
LED_Green = 5 # State LED
LED_Yellow = 6 # Alarm LED
BUZZER = 19
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LED_Red, GPIO.OUT)
GPIO.setup(LED_Green,GPIO.OUT)
GPIO.setup(LED_Yellow, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)

# Normal State
GPIO.output(LED_Green, GPIO.HIGH)
GPIO.output(LED_Yellow, GPIO.LOW)
GPIO.output(LED_Red, GPIO.LOW)
GPIO.output(BUZZER, GPIO.LOW)


while True:
    i = GPIO.input(26)
    # No Motion
    if i == 0:
        GPIO.output(LED_Green, GPIO.HIGH)
        GPIO.output(LED_Yellow, GPIO.LOW)
        GPIO.output(LED_Red, GPIO.LOW)
        GPIO.output(BUZZER, GPIO.LOW)

    # Motion Detected
    elif i == 1:
        start = time.time()
        GPIO.output(LED_Green, GPIO.LOW)
        GPIO.output(LED_Yellow, GPIO.HIGH)
        GPIO.output(LED_Red, GPIO.LOW)
        GPIO.output(BUZZER, GPIO.HIGH)

    time.sleep(1)
GPIO.cleanup()