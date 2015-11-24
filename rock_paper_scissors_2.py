import random

def Rock_Paper_Scissors():

    x = 0

    while x == 0:

        Computer_Choices = ['rock', 'paper', 'scissors']
		
        Computer_Choice = random.choice(Computer_Choices)
		
        User_Input = input("Do you pick rock, paper, or scissors? ")
	
        User_Input = User_Input.lower()
	
        while User_Input != 'rock' and User_Input != 'paper' and User_Input != 'scissors':
            print("Sorry! I did not understand your input. Please try again.")
            User_Input = input("Do you pick rock, paper, or scissors? ")	
            User_Input = User_Input.lower()
            
	
        wins = 0
        losses = 0
        ties = 0
	
        print("Computer picks: " + Computer_Choice)
		
        if Computer_Choice == 'rock':
            if User_Input == 'rock':
                print("It's a tie!")
                ties += 1
            elif User_Input == 'paper':
                print("You win!")
                wins += 1
            elif User_Input == 'scissors':
                print("Sorry, you lose!")
                losses += 1
	
        if Computer_Choice == 'scissors':
            if User_Input == 'scissors':
                print("It's a tie!")
                ties += 1
        elif User_Input == 'rock':
                print("You win!")
                wins += 1
        elif User_Input == 'paper':
                print("Sorry, you lose!")
                losses += 1
	
        if Computer_Choice == 'paper':
            if User_Input == 'paper':
                print("It's a tie!")
                ties += 1
            elif User_Input == 'scissors':
                print("You win!")
                wins += 1
            elif User_Input == 'rock':
                print("Sorry, you lose!")
                losses += 1
		
        print("Wins: " + str(wins))
        print("Losses: " + str(losses))
        print("Ties: " + str(ties))

        play_again = input("Would you like to play again? y/n ")

        play_again = play_again.lower()

        while play_again != 'y' and play_again != 'n':
            print("Sorry! I did not understand your input. Please try again")
            User_Input = input("Would you like to play again? ")
            User_Input = User_Input.lower()

        if play_again == 'y':
            pass
        else:
            x += 1
		
if __name__ == '__main__':
	Rock_Paper_Scissors()
