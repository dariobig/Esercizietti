from typing import Callable, List

def do_stuff(end: int, op: Callable[[int], int]) -> int:
    return op(end)

def mul_numbers(end: int) -> int:
    total = 1
    for i in range(1, end):
        total *= i
    return total

def is_multiple(num: int, denominators: List[int]) -> bool:
    for d in denominators:
        if num % d == 0:
            return True
    return False

def sum_numbers(end: int, denominators: List[int]) -> int:
    total = 0
    for i in range(end):
        if is_multiple(i, denominators):
            total += i
        else:
            continue
    return total

def get_number() -> int:
    return int(input('how many numbers?'))

if __name__ == '__main__':
    denominators = [3, 5]
    end = get_number() + 1
    total = sum_numbers(end, denominators)
    print(f'sum_numbers till {end} if multiple of {denominators} = {total}')