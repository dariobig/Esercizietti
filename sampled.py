from typing import Iterable, List, TypeVar, Iterator
from random import random, randint, sample

T = TypeVar('T')

def sampled(input_data: Iterable[T], sample_size: int) -> List[T]:
    """reservoir sampling https://en.wikipedia.org/wiki/Reservoir_sampling"""
    iter: Iterator[T] = iter(input_data)
    sample: List[T] = list()
    i = 0
    while len(sample) < sample_size:
        try:
            e = next(iter)
            sample.append(e)
        except StopIteration:
            break

    j = len(sample_size)
    while True:
        try:    
            new_e = next(iter)
            j += 1
            r = random()
            selection_prob = sample_size / (j - 1)
            if r >= selection_prob:
                # pick element
                replacement = randint(0, sample_size - 1)
                sample[replacement] = new_e
        except StopIteration as e:
            break
    return sample

SAMPLE_SIZE = 10
test_list = list(range(SAMPLE_SIZE))
positions = {i: 0 for i, e in enumerate(test_list)}
REPETITIONS = 500

positions = {i: 0 for i, e in enumerate(test_list)}
for i in range(REPETITIONS):
    sampled = sample(test_list, SAMPLE_SIZE)
    assert sampled != test_list, f'different order shuffled: {sampled}, original: {test_list}'
    assert len(sampled) == SAMPLE_SIZE, f'same elements shuffled: {sampled}, original: {test_list}'
    #print(f'sampled: {sampled}, original: {test_list}')
    for i, e in enumerate(sampled):
        positions[e] += 1
    
# check that shuffles are really random: increasing the number of shuffle should make average position converge
sample = {}
for i, sum in positions.items():
    positions[i] = sum / REPETITIONS
print(f'positions {positions}')
deltas = {i: v - positions[0] for i, v in positions.items()}

print(f'deltas: {deltas}')
print(f'deltas: {max(deltas.values())}')


