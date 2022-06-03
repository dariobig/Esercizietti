
#Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6].
# You can do this quicker than concatenating them followed by a sort.
from typing import List

def merge(first: List, second: List) -> List:
    i = 0
    j = 0
    combined = []
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            current = first[i]
            combined.append(current)
            i += 1
        else:
            current = second[j]
            combined.append(current)
            j += 1

    if i < len(first):
        combined.extend(first[i:])
    elif j < len(second):
        combined.extend(second[j:])
    return combined

def skip_one_list(list: List) -> List:
    """[1,2,3, 4, 5] -> [2, 3, 5]"""
    [1, 2, 3]
    # list comprehension
    return [e for i, e in enumerate(list) if i % 2 == 0]

if __name__ == '__main__':
    print(f"{merge([1,4,6,9],[2,3,5])}")