from typing import List, TypeVar
from random import randint

T = TypeVar('T')

def shuffled(input_list: List[T]) -> List[T]:
    """Fisher-yates shuffle https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm"""
    randomized: List[T] = list(input_list)
    l = len(randomized)
    for i in range(l - 1, -1, -1):
        j = randint(0, i)
        if i != j:
            val_i, val_j = randomized[i], randomized[j]
            randomized[i], randomized[j] = val_j, val_i
    return  randomized

test_list = list(range(100))
positions = {i: 0 for i, e in enumerate(test_list)}
REPETITIONS = 50000

for i in range(REPETITIONS):
    randomized_list = shuffled(test_list)
    assert randomized_list != test_list, f'different order shuffled: {randomized_list}, original: {test_list}'
    assert sum(randomized_list) == sum(test_list), f'same elements shuffled: {randomized_list}, original: {test_list}'
    # print(f'shuffled: {randomized_list}, original: {test_list}')
    for i, v in enumerate(randomized_list):
        positions[i] += v 

# check that shuffles are really random: increasing the number of shuffle should make average position converge
averages = {}
for i, sum in positions.items():
    averages[i] = sum / REPETITIONS
print(f'averages {averages}')


