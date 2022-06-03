#1. Write a function that returns the largest element in a list.
#2. Write function that reverses a list, preferably in place.

def max_num(l) -> int:
	x=l[0]
	for i in l:
		if i > x:
			x=i
	return x

def max_num2(l) -> int:
	current = l[0]
	for i in range(1,len(l)):
		e = l[i]
		if e > current:
			current = e
	return current

def reverse_list(nums):
	nums.sort(reverse=True)
	return nums


if __name__ == '__main__':
	nums = [1000, 4, 2, 7, 81, 1002]
	print(f"{max_num(nums)} AND {max_num2(nums)} AND {reverse_list(nums)}")