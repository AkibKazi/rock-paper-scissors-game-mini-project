import random 

print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
	+ "Rock vs Paper -> Paper wins \n"
	+ "Rock vs Scissors -> Rock wins \n"
	+ "Paper vs Scissors -> Scissor wins \n")

while True:
	
	print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
	
	
	
	choice=int(input("Enter your choice :"))
	match (choice):
		case 1:
			choice_name= 'Rock'
		case 2:
			choice_name= 'Paper'
		case 3:
			choice_name= 'Scissors'
		
	#  choice=int(input('Enter a valid choice please '))
		

		
	print('User choice is \n',choice_name)
	print('Now its Computers Turn....')
	
	
	comp_choice = random.randint(1,3)
	match (comp_choice):
		case 1:
			comp_choice= 'Rock'
		case 2:
			comp_choice= 'Paper'
		case 3:
			comp_choice= 'Scissors'
	
	print("Computer choice is \n", comp_choice)
	print(choice_name,'Vs',comp_choice)
	
	result = ""
	if choice == comp_choice:
		print('Its a Draw',end="")
		result="DRAW"
	 
	if (choice==1 and comp_choice==2):
		print('paper wins =>',end="")
		result='papeR'
	elif (choice==2 and comp_choice==1):
		print('paper wins =>',end="")
		result='Paper'
		
	
	if (choice==1 and comp_choice==3):
		print('Rock wins =>\n',end= "")
		result='Rock'
	elif (choice==3 and comp_choice==1):
		print('Rock wins =>\n',end= "")
		result='rocK'
		
	if (choice==2 and comp_choice==3):
		print('Scissors wins =>',end="")
		result='scissoR'
	elif (choice==3 and comp_choice==2):
		print('Scissors wins =>',end="")
		result='Rock'
	
	if result == 'DRAW':
		print("<== Its a tie ==>")
	if result == choice_name:
		print("<== User wins ==>")
	else:
		print("<== Computer wins ==>")
	print("Do you want to play again? (Y/N)")
	
	ans = input().lower
	if ans =='n' or ans=="N":
		exit

print("thanks for playing")
