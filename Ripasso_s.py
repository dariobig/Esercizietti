# Write a program that asks the user for their name and greets them with their name.
# Modify the previous program such that only the users Alice and Bob are greeted with their names.

def chek_name() -> str:
	allowed_names = ['Sara', 'Dario']
	x = input('Enter your name ')
	if x in allowed_names:
		return x
	else:
		print (f'{x} is not in the list of allowed_names:{allowed_names}.')
		return None
#Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
def sum():
	pick_a_number = input(f"Please, pick a number ")
	z = int(pick_a_number)
	total=0
	for i in range(0, z+1, 1):
		total += i
	return total

if __name__ == '__main__':
	name = chek_name()
	if name:
		print(f'Welcome {name}')
		calculation = sum()
		print(f'{calculation}')