from random import randint

print("Welcome to the rock, paper and Scissors.".lower())
rounds = int(input("Best of how many rounds? "))

human_wins = 0
computer_wins = 0
ties = 0
round = 1

while True:
	player1 = input("Human selects: ")
	computer = randint(1,3)
	if computer == 1:
		player2 = "rock"
	elif computer == 2:
		player2 = "paper"
	else:
		player2 = "scissors"
	print(f"computer selects {computer} and its {player2}")

	if player1 == player2:
		ties += 1
		print("opps!! its a tie.")
	elif player1 == "rock":
		if player2 == "scissors":
			human_wins += 1
			print(f"round {round} goes to Human.")
		elif player2 == "paper":
			computer_wins += 1
			print(f"round {round} goes to Computer.")
	elif player1 == "paper":
		if player2 == "scissors":
			computer_wins += 1
			print(f"round {round} goes to Computer.")
		elif player2 == "rock":
			human_wins += 1
			print(f"round {round} goes to Human.")
	elif player1 == "scissors":
		if player2 == "paper":
			human_wins += 1
			print(f"round {round} goes to Human.")
		elif player2 == "rock":
			computer_wins += 1
			print(f"round {round} goes to Computer.")
	else:
		print("opps!! select proper options.\n")

	print(f"Total Rounds: {round}: \nHumans - {human_wins}, \nComputer - {computer_wins}, \nTie - {ties} \n")
	round += 1

	if human_wins == rounds:
		print("hurray!! Human wins")
		break;
	elif computer_wins == rounds:
		print("Opps!! computer wins.")
		break;