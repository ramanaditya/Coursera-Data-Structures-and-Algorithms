# Uses python3
'''
Problem Description
Task. Given two integers 𝑎 and 𝑏, find their least common multiple.
Input Format. The two integers 𝑎 and 𝑏 are given in the same line separated by space.
Constraints. 1 ≤ 𝑎,𝑏 ≤ 2·10^9.
Output Format. Output the least common multiple of 𝑎 and 𝑏.
'''

import sys

def gcd(a, b):
	if b==0:
		return a
	else:
		a = a % b
		return gcd(b,a)

def lcm(a,b): 
    lcm_res = (a*b) // gcd(a,b)
    return(int(lcm_res))

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm(a, b))
