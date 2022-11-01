import sys
sys.stdin = open('../input.txt', 'rt')

s = input()
res = 0
for i in s:
    if i.isdecimal():   # isdigit() 의 경우 숫자면 다 True
        res = res*10 + int(i)

res1 = 0
for j in range(1, res + 1) :
    if res % j == 0:
        res1 += 1

print(res)
print(res1)
