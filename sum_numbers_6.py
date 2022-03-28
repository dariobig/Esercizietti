from typing import Callable, Iterable

def do_stuff(end: int, op: Callable[[int], int]) -> int:
    return op(end)

def mul_numbers(end: int) -> int:
    total = 1
    for i in range(1, end):
        total *= i
    return total

def is_multiple(num: int) -> bool:
    for d in denominators:
        if num % d == 0:
            return True
    return False

def sum_numbers(end: int) -> int:
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
    choice: str = input('should I sum [s] or multitply: [m]?')
    if choice.lower() == 's':
        op = sum_numbers
        end = get_number() + 1
        total = do_stuff(end, op=op)
        print(f'op: {op} till {end} = {total}')
    else:
        op = mul_numbers
        end = get_number() + 1
        total = do_stuff(end, op=op)
        print(f'op: {op} till {end} = {total}')
