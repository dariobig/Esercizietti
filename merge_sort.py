from __future__ import annotations



from random import shuffle

from abc import abstractmethod
from typing import List, TypeVar, Optional, Protocol, TypeVar, Tuple, Iterator


class Comparable(Protocol):
    """Protocol for annotating comparable types."""

    @abstractmethod
    def __lt__(self: T, other: T) -> bool:
        pass

T = TypeVar('T', bound=Comparable)

def next_or_none(i: Iterator[T]) -> Optional[T]:
    i
    try:
        return next(i)
    except StopIteration as e:
        return None

K = TypeVar('K')

def shuffled(original: List[K]) -> List[K]:
    randomized = list(original)
    shuffle(randomized)
    return randomized



def min_if_not_None(l: Optional[T], r: Optional[T]) -> Optional[T]:
    if l is None and r is None:
        return None
    else:
        return min(l, r)

def merge(left: List[T], right: List[T]) -> List[T]:
        merged: List[T] = []
        left_i = iter(left)
        right_i = iter(right)
        l: Optional[T] = next_or_none(left_i)
        r: Optional[T] = next_or_none(right_i)
        next_e = min_if_not_None(l, r)
        while next_e is not None:
            merged.append(next_e)
            l = next_or_none(left_i)
            r = next_or_none(right_i)
            next_e = min_if_not_None(l, r)

        return merged

def split(list: List[T]) -> Tuple(List[T], List[T]):
    middle = len(list) // 2
    return (list[:middle], list[middle:])

def merge_sort(list: List[T]) -> List[T]:
    if not list:
        return list
    if len(list) <= 1:
        return list
    left, right = split(list)
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

print([i for i in range(12)])

cases = [(shuffled(list(range(i))), list(range(i))) for i in range(12)]
for randomized, sorted in cases:
    shuffle(sorted)
    merge_sorted = merge_sort(randomized)
    print(randomized, sorted, merge_sorted)
    # assert sorted == merge_sorted, f'merge_sorted should be sorted {merge_sorted} == {sorted}!'
