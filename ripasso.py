# Write a program that asks the user for their name and greets them with their name.
# Modify the previous program such that only the users Alice and Bob are greeted with their names.

def chek_name(name: str) -> str:
	allowed_names = ['Sara', 'Dario']
	if name in allowed_names:
		return name
	else:
		return (f'{name} is not in the list of allowed_names:{allowed_names}.')

#Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
def summation(number: int) -> int:
	z = int(number)
	total=0
	for i in range(0, z+1, 1):
		total += i
	return total
