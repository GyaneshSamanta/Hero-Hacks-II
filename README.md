# Doo Doo Alert

Save yourself from unsuspected doodoos.

## Inspiration 💡
Have you ever walked out of your house, extremely motivated to kickstart your day right with your best shoes on, and stepped on an unsuspected 💩 accident? Yeah right, it takes one happy-looking stray cat (or dog)  to make your day (and shoes) miserable.

We were thinking about the prospective villains around our community and got reminded of the adorable kittens that don't think twice before doing a doodoo in front of our gates and hence came up with Doo Doo Alert, to brace ourselves from unsuspected accidents in front of our house.

## What it does 🧭
Doo Doo Alert is built over a Raspberry Pi that uses a PIR Sensor to monitor the front gate, or wherever a stray animal can unload. Once the animal is in the set proximity, an alarm is played and a notification is sent over to the user's phone stating that a stray has been spotted.

In case the animal stays for longer than 15 seconds, there is a high probability that the deed is done, and hence another notification is sent, asking the user to tread carefully.

## How we built it 🔧
A PIR (passive infrared sensor) is an analog sensor that measures infrared (IR) light radiating from objects in its field of view. They are most often used in PIR-based motion detectors. We used the same sensor to detect the presence of stray animals and raise an alarm once spotted.

We are using Twilio to send SMS notifications to the registered mobile numbers on the Twilio Console to alert the user about the situation. Apart from that, we are also using State LEDs to showcase the status of the whole apparatus.

## Technology Stack ⚙️
 - Raspberry Pi
 - Twilio
 - Python
 - PIR Sensor
 - TensorFlow
 - OpenCV
 - Google Cloud Platform

## Challenges we ran into 🏃‍♂️
1. Interfacing an analog sensor with a Raspberry Pi and using it to satiate the problem statement was extremely difficult and took hours of our time.
2. Initiating Twilio functions within motion detection phases without significant delay was pretty tedious as well.

## Accomplishments that we're proud of 🏅
1. We were able to create a stray animal detector with an inexpensive setup, without having to actually use a Camera.

## What we learned 🧠
1. Dealing with analog sensors on Raspberry Pi.
2. Using Twilio on board an IoT setup.

## What's next for Doo Doo Alert ⏭
1. Addition of accurate models with a camera to monitor the whole situation.