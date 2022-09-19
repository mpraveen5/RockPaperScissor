import random
print("Rules : \n"
								+"Rock vs paper: paper wins \n"
								+ "Rock vs scissor: Rock wins \n"
								+"paper vs scissor: scissor wins \n")

while True:
	print("Enter choice \n 1 - Rock, \n 2 - paper, and \n 3 - scissor \n")
	# get input from user
	choice = int(input("User turn: "))
	
	# looping until user enter invalid input
	while choice > 3 or choice < 1:
		choice = int(input("enter valid input: "))
	
	if choice == 1:
		choice_name = 'Rock'
	elif choice == 2:
		choice_name = 'paper'
	else:
		choice_name = 'scissor'
		
	print("Your choice is: " + choice_name)
	
	comp_choice = random.randint(1, 3)
	
	# looping until comp_choice value
	# is equal to the choice value
	while comp_choice == choice:
		comp_choice = random.randint(1, 3)

	# initialize value of comp_choice_name
	# variable corresponding to the choice value
	if comp_choice == 1:
		comp_choice_name = 'Rock'
	elif comp_choice == 2:
		comp_choice_name = 'paper'
	else:
		comp_choice_name = 'scissor'
		
	print("Computer choice is: " + comp_choice_name)

	print(choice_name + " V/s " + comp_choice_name)
	#we need to check of a draw
	if choice == comp_choice:
		print("Draw=> ", end = "")
		result = Draw
	
	# condition for winning
		if((choice == 1 and comp_choice == 2) or
		(choice == 2 and comp_choice ==1 )):
			print("paper wins => ", end = "")
			result = "paper"

		elif((choice == 1 and comp_choice == 3) or
			(choice == 3 and comp_choice == 1)):
			print("Rock wins =>", end = "")
			result = "Rock"
		else:
			print("scissor wins =>", end = "")
			result = "scissor"
	# Printing either user or computer wins or draw
	if result == Draw:
		print("<== Its a tie ==>")
	if result == choice_name:
		print("<== User wins ==>")
	else:
		print("<== Computer wins ==>")
		
	print("Do you want to play again? (Y/N)")
	ans = input().lower
	# if user input n or N then condition is True
	if ans == 'n':
		break
	

