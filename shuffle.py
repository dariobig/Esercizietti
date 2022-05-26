# fisher-yates shuffle https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm
from random import randint
from typing import List, TypeVar

T = TypeVar('T')

def shuffle(data: List[T]) -> List[T]:
    for i in range(len(data) - 1, 1, -1):
        j = randint(0, i)
        if j != i:
            data[i], data[j] = data[j], data[i]
        return data

def str_shuffle(original: str) -> str:
    data = [c for c in original]
    shuffled = shuffle(data)
    return ''.join(shuffled)

for i in range(15):
    print(shuffle(list(range(15))))
    print(str_shuffle('ciao!'))