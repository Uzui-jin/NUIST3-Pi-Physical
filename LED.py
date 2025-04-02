import RPi.GPIO as GPIO # import the RPi.GPIO liberary and alias it as GPIO for easier use
import time # improt the time liberary for sleep/dealy functions
GPIO.setmode(GPIO.BCM) # Set the GPIO pin numbering mode to Broadcom (BCM) numbering
GPIO.setwarnings(False) # Disable runtime warning messages
GPIO.setup(18,GPIO.OUT) # Set GPIO pin 18 as an output pin
print ("LED on")  # Print "LED on" message to the console
GPIO.output(18,GPIO.HIGH) # Set GPIO pin 18 to HIGH (turns the LED on)
time.sleep(1) # Pause the program for 1 second
print  ("LED off") # Print "LED off" message to the console
GPIO.output(18,GPIO.LOW) # Set GPIO pin 18 to LOW (turns the LED off)
