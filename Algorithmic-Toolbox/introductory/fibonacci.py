# Uses python3

import sys

# This algorithm is quite fast but it uses too much storage to store the data 
def calc_fib(n):
	fib_list = list(range(0,n+1))
	for i in range(2,n+1):
		fib_list[i] = fib_list[i-1] + fib_list[i-2]
	return fib_list[n]

# This algorithm is quite fast as well as doesn't utilises too muc h spaces
# The running time of this algorithm is O(n)
def fib(n):
	ifn<=1:
		return n
	previous , current = 0, 1
	for _ in range(n − 1):
		new_current = previous + current
		previous , current = current , new_current
	return current

a = int(input())
print(calc_fib(a))
