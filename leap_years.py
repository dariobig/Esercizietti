#Write a program that prints the next 20 leap years.
from datetime import datetime

def next_leap_year() -> int:
	current_year = datetime.now().year
	for i in range(4):
		current_year += 1
		if current_year % 4 == 0:
			print(current_year)
			return current_year

year = next_leap_year()
for i in range(1, 20):
	print(year + i * 4)

