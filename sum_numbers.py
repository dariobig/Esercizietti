from typing import Callable

def do_stuff(end: int, op: Callable[[int], int]) -> int:
    return op(end)

def mul_numbers(end: int) -> int:
    total = 1
    for i in range(1, end):
        total *= i
    return total

def sum_numbers(end: int) -> int:
    total = 0
    for i in range(end):
        total += i
    return total

def is_multiple(num: int, denominators: Iterable[int]) -> bool:
    for d in denominators:
        if num % d == 0:
            return True
    return False

def sum_numbers(end: int, denominators: Iterable[int]) -> int:
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
