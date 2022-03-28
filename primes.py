"""Write a program that prints all prime numbers. (Note: if your programming language does not support arbitrary size numbers, printing all primes up to the largest number you can easily represent is fine too.)"""
from typing import List

def find_primes(max_num: int = 1024) -> List[int]:
    primes = [2]
    print(f'finding primes between 1 and {max_num}')
    for i in range(2, max_num):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
        if is_prime:
            primes.append(i)
    return primes

if __name__ == '__main__':
    print(find_primes())