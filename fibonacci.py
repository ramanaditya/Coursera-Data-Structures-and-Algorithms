# Uses python3
# Given an integer 𝑛, find the 𝑛th Fibonacci number 𝐹𝑛
import sys

def calc_fib(n):
	fib_list = list(range(0,n+1)) # First we create a list upto n+1 number(exclusive n+1)
	for i in range(2,n+1):	# We start a loop from position 2 because first two numbers in fib_list is already 0 and 1 so no need to declare them
		fib_list[i] = fib_list[i-1] + fib_list[i-2]
	return fib_list[n]

a = int(input())
print(calc_fib(a))

#Input Format: The input consists of a single integer 𝑛. 
