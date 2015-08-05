CompScore = 0
YourScore = 0
Ties = 0

print "Let's play Rock Paper Scissors!"
print "Choose either Rock, Paper, or Scissors!"

user = str(raw_input())

user = user.lower()

def RPS(y):	
	
	import random

	L = ["rock", "paper", "scissors"]

	a = random.choice(L)

	global user 
	global b


	def rps(x):
	
		global user 

		global CompScore
		global YourScore
		global Ties
		
		while user != "rock" and user != "paper" and user != "scissors":
			print "Sorry, I did not understand your input. Try Again!"
			user = raw_input()
			user = user.lower()
			
		print "Computer picks: " + str(a)
			
		
		if a == user:
			print "It's a tie!"
			Ties += 1

		else: 

			if a == "rock":
				if user == "paper":
					print "You win!"
					YourScore += 1
				if user == "scissors": 
					print "Sorry, you lose!"
					CompScore += 1

			if a == "paper":
				if user == "scissors":
					print "You win!"
					YourScore += 1
				if user == "rock": 
					print "Sorry, you lose!"
					CompScore += 1

			if a == "scissors":
				if user == "rock":
					print "You win!"
					YourScore += 1
				if user == "paper": 
					print "Sorry, you lose!"
					CompScore += 1
			
		print "Computer Score: " + str(CompScore)
		print "Your Score: " + str(YourScore)
		print "Number of Ties: " + str(Ties)
			
		print "Want to play again? Type Y for yes or N for no!"
			
		b = raw_input()
		b = b.lower()
			
		while b != "y" and b != "n":
			print "Sorry, I did not understand your input. Try Again!"
			b = raw_input()
			b = b.lower()
		
		
		if b == "y":
			print "Let's play Rock Paper Scissors!"
			print "Choose either Rock, Paper, or Scissors!"
			user = raw_input()
			user = user.lower()
			return RPS(y)
		if b == "n":
			print "Game Over."

				
	rps(user)
	
RPS(1)
