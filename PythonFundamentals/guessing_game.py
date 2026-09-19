from random import randint

computer_guess = randint(1,10)

play = "y"

while play == "y":
	human_guess = int(input("guess the number between 1 to 10: "))
	if(human_guess == computer_guess):
		print("You guessed it correctly")
		play = input("do you want to play again (y/n)? ")
		computer_guess = randint(1,10)
	elif human_guess < computer_guess and human_guess > 0 :
		print("your guess is lower. try again")
	elif human_guess > computer_guess and human_guess < 11:
		print("your guess is higher. try again")
	else:
		print("wrong input range. try again between 1 and 10")

print("Thanks for playing.")