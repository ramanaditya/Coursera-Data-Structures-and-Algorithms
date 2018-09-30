# Uses python3
'''
Problem Description
Task. The goal in this problem is to find the minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5, and 10.
Input Format. The input consists of a single integer 𝑚.
Constraints. 1 ≤ 𝑚 ≤ 10^3.
Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes 𝑚.

'''

import sys

def get_change(m):
	coins = [10,5,1]
	val = 0
	count = 0
	for i in range(len(coins)):
		if m - coins[i] >= 0:
			count += m//coins[i]
			val = (m//coins[i]) * coins[i]
			m -= val
	return count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
