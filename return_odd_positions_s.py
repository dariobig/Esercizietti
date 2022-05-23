from typing import Dict, Tuple, Iterable. TypeVar
grocery = ['0. bread', '1. milk', '2. yogurt', '3. cereal' ]
print("Elements in odd position: ");

ingredients: Dict[int, str] = {'a' :'bread', 'b' :'milk', 'c' :'yogurt', 'd' :'cereal' }

for i, (k, val) in enumerate(ingredients):
	if i % 2 != 0:
		print(val)

T = TypeVar('T')

def enumerate_1(data: Iterable[T]) -> Iterable[Tuple[int, T]]:
	i = 0
	for val in data:
		yield (i, val)
		i += 1

