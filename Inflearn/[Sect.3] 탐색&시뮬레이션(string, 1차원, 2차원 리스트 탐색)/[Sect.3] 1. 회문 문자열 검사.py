import sys
sys.stdin = open('../input.txt', 'rt')

# case 1
n = int(input())
for i in range(n):
    s = sys.stdin.readline().strip().lower()
    if s == s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" % (i+1))

''' # case 2 << 직접 짤 땐 이렇게!
n = int(input())
for i in range(n):
    s = sys.stdin.readline().strip().lower()
    for j in range(len(s) // 2):
        if s[j] != s[-j-1] :
            print("#%d NO" % (i+1))
            break
    else:
        print("#%d YES" % (i+1))
'''
