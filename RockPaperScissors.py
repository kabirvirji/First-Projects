def RPS(y):	
	
	import random

	L = ["Rock", "Paper", "Scissors"]

	a = random.choice(L)

	print str(a)

	print "Let's play Rock Paper Scissors!"
	print "Choose either Rock, Paper, or Scissors!"

	user = raw_input()

	print str(user)

	def rps(x):

		CompScore = 0
		YourScore = 0
		Ties = 0
		
		if user != "Rock" and user != "Paper" and user != "Scissors":
			print "Sorry, I did not understand your input."
		
		if a == user:
			print "It's a tie!"
			Ties += 1

		else: 

			if a == "Rock":
				if user == "Paper":
					print "You win!"
					YourScore += 1
				if user == "Scissors": 
					print "Sorry, you lose!"
					CompScore += 1

			if a == "Paper":
				if user == "Scissors":
					print "You win!"
					YourScore += 1
				if user == "Rock": 
					print "Sorry, you lose!"
					CompScore += 1

			if a == "Scissors":
				if user == "Rock":
					print "You win!"
					YourScore += 1
				if user == "Paper": 
					print "Sorry, you lose!"
					CompScore += 1
			
		print "Computer Score: " + str(CompScore)
		print "Your Score: " + str(YourScore)
		print "Number of Ties: " + str(Ties)
			
		print "Want to play again? Type Y for yes or N for no!"
			
		b = raw_input()
		
		print str(b)
			
		if b == "Y":
			return RPS(y)
		if b == "N":
			print "Game Over."
		else:
			print "Sorry, I did not understand your input."
				
	rps(user)
	
RPS(1)