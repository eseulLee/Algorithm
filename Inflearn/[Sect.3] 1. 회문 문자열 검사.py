import sys
sys.stdin = open('input.txt', 'rt')

# case 1
n = int(input())
for i in range(1, n+1):
    s = sys.stdin.readline().strip().lower()
    if s == s[::-1]:
        print("#%d YES" %(i))
    else:
        print("#%d NO" % (i))

''' # case 2
n = int(input())
for i in range(1, n+1):
    s = sys.stdin.readline().strip().lower()
    for j in range(len(s) // 2):
        if s[j] != s[-j-1] :
            print("#%d NO" % (i))
            break
    else:
        print("#%d YES" % (i))
'''
