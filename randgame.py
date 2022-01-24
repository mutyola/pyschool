import random
num = random.randint(1,5)
guess = int(input("Enter a number: "))
if guess == num:
	print("Well done")
elif guess > num:
	print("Too high")
	guess = int(input("Guess again: "))
	if guess == num:
		print("Correct")
	else:
		print("You lose")
elif guess < num:
	print("Too low")
	guess = int(input("Guess again: "))
	if guess == num:
		print("Correct")
	else:
		print("You lose")	