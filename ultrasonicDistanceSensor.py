    #Libraries
import RPi.GPIO as GPIO
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client

GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 4
GPIO_ECHO = 17

# send to sonic pi
sender = udp_client.SimpleUDPClient('127.0.0.1',4559)

#set GPIO inputs and outputs
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# set Trigger to HIGH and after some time return to LOW
GPIO.output(GPIO_TRIGGER, True)
time.sleep(0.00001)
GPIO.output(GPIO_TRIGGER, False)

# ECHO trigger - pulse returned
while GPIO.input(GPIO_ECHO) == 0:
StartTime = time.time()

# ECHO trigger - pulse returned
while GPIO.input(GPIO_ECHO) == 1:
StopTime = time.time()


# calculate distance    
# multiply the time with the sonic speed (34300 cm/s)
#and divide by 2 because it's going there and back
TimeDifference = StopTime - StartTime
distance = (TimeDifference * 34300) / 2 

pitch = round(distance + 60)
sender.send_message('/play_this', pitch)
print ("Pitch = %d" % pitch)

time.sleep(0.1)

GPIO.cleanup()
    

