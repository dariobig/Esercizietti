from typing import List
#Write a function that checks whether an element occurs in a list.
grocery = ['bread', 'milk', 'yogurt', 'cereal' ]

def find(needle: str, haystack: List[str]) -> bool:
	for item in haystack:
		if item == haystack:
			print(f'{item} found')
			return True
	return False

test = {'g': 12,
 'f': 1}

for (key, val) in test:
	print(key, val)



test[123] == 12
test[7] = 1

if 'g' in 'grocery':
	print('Found')

print('bread' in grocery)
print(find('bread', grocery))