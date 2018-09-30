# Uses python3

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
