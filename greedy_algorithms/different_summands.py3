# Uses python3
'''
Problem Introduction
You are organizing a funny competition for children. As a prize fund you have 𝑛 candies. You would like to use these candies for top 𝑘 places in a competition with a natural restriction that a higher place gets a larger number of candies. To make as many children happy as possible, you are going to find the largest value of 𝑘 for which it is possible.

Problem Description
Task. The goal of this problem is to represent a given positive integer 𝑛 as a sum of as many pairwise distinct positive integers as possible. That is, to find the maximum 𝑘 such that 𝑛 can be written as 𝑎1+𝑎2+···+𝑎𝑘 where𝑎1,...,𝑎𝑘 arepositiveintegersand𝑎𝑖 ̸=𝑎𝑗 forall1≤𝑖<𝑗≤𝑘.
Input Format. The input consists of a single integer 𝑛.
Constraints. 1 ≤ 𝑛 ≤ 10^9.
Output Format. In the first line, output the maximum number 𝑘 such that 𝑛 can be represented as a sum of 𝑘 pairwise distinct positive integers. In the second line, output 𝑘 pairwise distinct positive integers that sum up to 𝑛 (if there are many such representations, output any of them).
Sample 1.
Input:6
Output: 3 
	1 2 3
Sample 2.
Input:8
Output: 3
	1 2 5
Sample 3.
Input:2
Output: 1 
	2
'''
import sys

#This algorithm is fast upto 10^9
def optimal_summands(n):
    summands = []
    #write your code here
    i = 1
    while True:
        if n <= 2 * i:
            summands.append(n)
            break
        else:
            summands.append(i)
            n = n - i
            i += 1
    return summands

#This algorithm is fast upto 10^8
def optimal_summands(n):
	summands = []
	#write your code here
	i = 1
	while True:
		if sum(summands) + i > n:
			summands.pop()
		if sum(summands) < n:
			summands.append(i)
			i += 1
		if sum(summands) == n:
			break
	return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
