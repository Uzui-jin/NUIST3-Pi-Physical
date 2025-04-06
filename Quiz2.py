#name: Zhao renzhe ID: 202283890024 Date: 06/04/2025
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GREEN_LED = 17
RED_LED = 18
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

def quiz():
	print("Welcome to the Python Quiz!")

	questions = [
		"1) Which of the following is NOT a python data type?\na) int\nb) float\nc) rational\nd) string\ne) bool",
		"2) Which of the following is NOT a built-in operation in Python?\na) +\nb) %\nc) abs()\nd) sqrt()",
		"3) In a mixed-type expression involving ints and floats, Python will convert:\na) floats to ints\nb) ints to strings\nc) floats and ints to strings\nd) ints to floats",
		"4) The best structure for implementing a multi-way decision in Python is:\na) if\nb) if-else\nc) if elif-else\nd) try",
		"5) What statement can be executed in the body of a loop to cause it to terminate?\na) if\nb) exit\nc) continue\nd) break"
]

	answers = ["c", "d", "d", "c", "d"]
	score = 0

	try:
		for i in range(len(questions)):
			user_answer = input(questions[i] + "\nYour answer: ").strip().lower()
			if user_answer == answers[i]:
				print("Correct!")
				GPIO.output(GREEN_LED, GPIO.HIGH)
				time.sleep(1)
				GPIO.output(GREEN_LED, GPIO.LOW)
				score += 1
			else:
				print("Incorrect!")
				GPIO.output(RED_LED, GPIO.HIGH)
				time.sleep(1)
				GPIO.output(RED_LED, GPIO.LOW)

		print(f"\nFinal Score: {score}/{len(questions)}")

	finally:
		GPIO.cleanup()

quiz()

