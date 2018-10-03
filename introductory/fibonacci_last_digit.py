# Uses python3
import sys
'''
Problem Description
Task. Given an integer 𝑛, find the last digit of the 𝑛th Fibonacci number 𝐹𝑛 (that is, 𝐹𝑛 mod 10). Input Format. The input consists of a single integer 𝑛.
Constraints. 0 ≤ 𝑛 ≤ 107.
Output Format. Output the last digit of 𝐹𝑛.
Sample 1.
Input:3
Output:2
Sample 2.
Input:331
Output:9
𝐹331 = 668996615388005031531000081241745415306766517246774551964595292186469
Sample 3.
Input: 327305
Output: 5
'''

#It is quite fast and effective alorithm to get the last digit of any larger fibonacci number

def get_fibonacci_last_digit(n):
    fib_list = list(range(0,n+1))
    for i in range(2,n+1):
        fib_list[i] = (fib_list[i-1] + fib_list[i-2])%10
    return fib_list[n]


n = int(input())
print(get_fibonacci_last_digit(n))
