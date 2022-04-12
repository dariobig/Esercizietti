# define moltiplication of numebers multiple of 5 or 3 in a range
def mult_numbers(n:int) -> int:
    pick_number: int = n
    mult = 1  
    x = range(1, pick_number+1)      
    for i in x:
        if(i % 5 == 0 or i % 3 == 0):
            # print(f"Ecco {i}")
            mult *= i
    return mult
# define sum of numbers in a range
def sum_numbers(n: int) -> int:
    pick_number: int = n
    total = 0
    x = range(1, pick_number+1)
    for i in x:
         if(i % 5 == 0 or i % 3 == 0):
             # print(f"Ecco {i}")
             total += i
    return total
# execute sum if user input is Sum; execute multiplication if user input is Mult
if __name__ == '__main__':
    r = input("Sum (write S) o Multiplication (write M)? ")
    if r == "S":
        total = sum_numbers(int(input("Pick a number: ")))
        print(f'total: {total}')
    elif r == "M":
        mult = mult_numbers(int(input("Pick a number: ")))
        print(f'total: {mult}')
    else:
        print("Invalid input")



        #Test
# tests = [(17, sum([3, 5, 6, 9, 10, 12, 15])), (1, 0), (3, 3), (5, 8)]
#     for (n, expected) in tests:
#         actual = sum_numbers(n + 1, denominators)
#         print(f'sum of {n} of multiples of {denominators} should be: {expected} {actual == expected}')
#         assert actual == expected, f'actual={actual} == {expected} = {actual == expected}'  