from twilio.rest import Client
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

# Twilio Account Setup
account_sid = '$SID'
auth_token = '$AUTH'
client = Client(account_sid, auth_token)

# Twilio Functions
# Alarm Message
def twilAlarm(channel): 
   print("Twilio alarm message sent.")
   message = client.messages \
    .create(
         body='Stray spotted, alarm initiated.',
         from_='+19124612542',
         to='+$PHONE'
     )
   print(message.sid)

# Warning Message
def twilWarning(channel): 
   print("Twilio warning message sent.")
   message = client.messages \
    .create(
         body='Suspected poop alert, tread carefully!',
         from_='+19124612542',
         to='+$PHONE'
     )
   print(message.sid)


# Check Sensor Data
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
        GPIO.output(LED_Green, GPIO.LOW)
        GPIO.output(LED_Yellow, GPIO.HIGH)
        GPIO.output(LED_Red, GPIO.LOW)
        GPIO.output(BUZZER, GPIO.HIGH)
        twilAlarm()
        time.sleep(5)
        # No Motion
    if i == 0:
        GPIO.output(LED_Green, GPIO.HIGH)
        GPIO.output(LED_Yellow, GPIO.LOW)
        GPIO.output(LED_Red, GPIO.LOW)
        GPIO.output(BUZZER, GPIO.LOW)
    elif i == 1:
        GPIO.output(LED_Green, GPIO.LOW)
        GPIO.output(LED_Yellow, GPIO.LOW)
        GPIO.output(LED_Red, GPIO.HIGH)
        GPIO.output(BUZZER, GPIO.LOW)
        twilWarning()
        time.sleep(5)
    time.sleep(1)

GPIO.cleanup()