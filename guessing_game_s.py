#Write a guessing game where the user has to guess a secret number. 
# After every guess the program tells the user whether their number 
# was too large or too small. At the end the number of tries needed 
# should be printed. It counts only as one try if they input the 
# same number multiple times consecutively.
n_guesses = 1
secret_number: int = 8
x = int(input("Take your guess: "))
while x != secret_number:
	n_guesses += 1
	if x < secret_number:
		x = int(input(f"Too small! Take another guess: "))
	else:
		x = int(input(f"Too large! Take another guess: "))
print(f"Great! You got it in {n_guesses} guesses!")
