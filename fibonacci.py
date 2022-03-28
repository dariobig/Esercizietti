# %%
from typing import Dict

def fib(n: int) -> int:
    p1 = 0
    p2 = 1

    # note: wikipedia definition of fibonacci is 0, 1, 1
    if n <= 2:
        return min(n, 1)
    else:
        for i in range(n):
            p1, p2 = (p1 + p2, p1)
    return p1

def fib_r(n: int, mem: Dict[int, int]) -> int:
    # note: wikipedia definition of fibonacci is 0, 1, 1
    if n <= 2:
        return min(n, 1)
    else:
        f = fib_r(n - 1, mem) + fib_r(n - 2, mem)
        mem[n] = f
        return f
    return p1

for i in range(50):
    expected = {}
    f = fib(i)
    f = fib_r(i, {})
    expected[i] = f
    print(f'fib({i}): {f}')
    e = expected.get(i)
    print(f'fib({i}): {f} == {e == f}, e: {e}, f:{f}')
