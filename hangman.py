name = input("Enter your name: ")
print("WELCOME TO HANGMAN")

import time
time.sleep(2)
print("start guessing...")
time.sleep(0.5)
kelimeler=["ability","above"]
#word="secret"
word=random.choice(kelimeler) #word to be guessed
guesses=" "
#determine number of turns
turns = 10
#check if the turns are more than zero
while(turns>0):
	#make a counter that starts with zero
	failed = 0
	#for every character in secret_word
	for char in word:
		#see if the character is in the player's guess
		if char in guesses:
			print(char)
		else:
			#if not found, print dash
			print("_")
			failed += 1
	if failed==0:
		print("You Won")
		break

	guess=input("guess a character:")
	#set the player guess to guesses

	guesses += guesses
	#if the guess is not found in the secret word
	if guess not in word:
		#Decrese the no of turns
		turns-=1
		print("Wrong")
		#how many turns are left
		print("You have", + turns,'more guesses')

		#if the turns are equal to zero
		if turns == 0:
			print("You loose")	             
