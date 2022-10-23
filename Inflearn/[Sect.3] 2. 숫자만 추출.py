import sys
sys.stdin = open('input.txt', 'rt')

s = input()
str = ''
for i in s:
    if i.isdigit():
        str += i
res1 = int(str)
res2 = 2
for j in range(2, res1//2 + 1) :
    if res1 % j == 0:
        res2 += 1

print(res1)
print(res2)
