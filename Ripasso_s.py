# Write a program that asks the user for their name and greets them with their name.
# Modify the previous program such that only the users Alice and Bob are greeted with their names.

def nomi():
	x = input("Enter your name ")
	if x == "Sara" or x=="Dario":
		print (f"Hello {x}")
	else:
		print ("Your name is not in the list.")
		return

#Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
	pick_a_number = input(f"Draw a number {x} ")
	z = int(pick_a_number)
	total=0
	for i in range(0, z+1, 1):
		total += i
	print(f"{total}")

if __name__ == '__main__':
	print(nomi())
#per @dario why does it also print None?



