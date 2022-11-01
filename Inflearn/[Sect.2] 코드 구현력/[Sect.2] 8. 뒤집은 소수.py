import sys
sys.stdin = open('../input.txt', 'rt')

def reverse(x):
    rev = int(x[::-1])
    return rev

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    return True

n = int(input())
a = input().split()  # str

for i in a :
    if isPrime(reverse(i)) :
        print(reverse(i), end=' ')

'''
def reverse(x):
    res = 0
    while x>0 :
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res
    
def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1):
        if x%1 == 0 :
            return False
    else:
        return True
'''

