#Write a function that combines two lists by alternatingly taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].
from typing import List

def alternating_merge(list_1: List, list_2: List) -> List:
    j = 0
    k = 0
    combined = []
    inputs = [list1, list2]
    for i in range(len(list1) + len(list2)):
        if i % 2 == 0:
            input = inputs[0]
            current = input[j]
            combined.append(current)
            j += 1
        else:
            input = inputs[1]
            current = input[k]
            combined.append(current)
            k += 1
    return combined

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']

    print(alternating_merge(list1, list2))