#Write a function that concatenates two lists. [a,b,c], [1,2,3] → [a,b,c,1,2,3]

from typing import List

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

def concat(original: List, other: List) -> List:
	combined = list(original)
	combined.extend(other)
	return combined


if __name__ == '__main__':
	print(f"Ecco {concat(list1, list2)}")


