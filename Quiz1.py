# NUIST Quiz Game in python
def quiz():
	print("Welcome to animal Quzi")
	print("Answer the following questions")

# questions and answers
	questions = [
		"1. What is the largest animal on Earth?: a. Blue Whale, b. Mouse, c. Cat",
		"2.Which bird can fly backwarsd?: a. Cuckoo, b. Eagle, C. Hummingbird",
		"3. What is the only animal capable of flight?: a. Bat, b. Squirrel, c. Dolphin"
	]
	answer = [
		"Blue Whale",
		"Hummingbird",
		"Bat"
	]
	score = 0

# Ask questions
	for i in range(len(questions)):
		user_answer = input(questions[i].strip().lower())
		if user_answer == answer[i]:
			print("Correct!")
			score += 1
		else:
			print("Incorrect!")

# Provide final score
	print("\nQuiz completed!")
	print(f"You got {score}/{len(questions)} questions correct.")

# Run the quiz function
quiz()
