# Uses python3

import sys

def gcd(a, b):
    if b==0:
      return a
    else:
        a = a % b
        return gcd(b,a)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
