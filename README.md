# Doo Doo Alert

Save yourself from unsuspected doodoos.

## Inspiration 💡
Have you ever walked out of your house, extremely motivated to kickstart your day right with your best shoes on, and stepped on an unsuspected 💩 accident? Yeah right, it takes one happy-looking stray cat (or dog)  to make your day (and shoes) miserable.

We were thinking about the prospective villains around our community and got reminded of the adorable kittens that don't think twice before doing a doodoo in front of our gates and hence came up with Doo Doo Alert, to brace ourselves from unsuspected accidents in front of our house.

## What it does 🧭
Doo Doo Alert is built over a Raspberry Pi that uses a PIR Sensor to monitor the front gate, or wherever a stray animal can unload. Once the animal is in the set proximity, an alarm is played and a notification is sent over to the user's phone stating that a stray has been spotted.

In case the animal stays for longer than 15 seconds, there is a high probability that the deed is done, and hence another notification is sent, asking the user to tread carefully.

There's also a Camera based model that we have been working on but couldn't integrate due to time constraints, which identifies dogs and cats from live footage and triggers respective events.

## How we built it 🔧
A PIR (passive infrared sensor) is an analog sensor that measures infrared (IR) light radiating from objects in its field of view. They are most often used in PIR-based motion detectors. We used the same sensor to detect the presence of stray animals and raise an alarm once spotted.

We are using Twilio to send SMS notifications to the registered mobile numbers on the Twilio Console to alert the user about the situation. Apart from that, we are also using State LEDs to showcase the status of the whole apparatus.

Doo Doo Alert has another camera-powered variant which needs some polishing up but at the moment it uses cocomo model to classify dogs and cats and can trigger Twilio functions like the hardware apparatus.

## Technology Stack ⚙️
 - Raspberry Pi
 - Twilio
 - Python
 - PIR Sensor
 - TensorFlow
 - OpenCV
 - Google Cloud Platform
 - cocomo Model

## Challenges we ran into 🏃‍♂️
1. Interfacing an analog sensor with a Raspberry Pi and using it to satiate the problem statement was extremely difficult and took hours of our time.
2. Initiating Twilio functions within motion detection phases without significant delay was pretty tedious as well.
3. We tried to build our own Stray Detection model, but given the time constraints, we could not build the model that would be supported on cloud, but resorted to using the TFOD API in order to make the process simpler. 
4. For the APAC region, we did not have Google Cloud Platform credits to test out the model on and had to rely on the TensorFlow Object Detection documentation which gave us an idea on how to add GCP to our model. Eventually we used cocomo model to create a working model that runs on Pi.

## Accomplishments that we're proud of 🏅
1. We were able to create a stray animal detector with an inexpensive setup, without having to actually use a Camera.
2. Regardless of the first pointer, we created another version which supported live detection of cats and dogs.

## What we learned 🧠
1. Dealing with analog sensors on Raspberry Pi.
2. Using Twilio on board an IoT setup.
3. Setting up ML Models.

## What's next for Doo Doo Alert ⏭
1. The GCP project and storage bucket are to be configured on the Raspberry Pi itself so that most of the computationally heavy work can be processed on the cloud rather than locally. Given the Pi's WiFi capabilities it should make things easier.
2. Addition of accurate models with a camera to monitor the whole situation.