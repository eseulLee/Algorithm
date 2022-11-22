import sys
sys.stdin = open('../input.txt', 'rt')
'''
# stack
- LIFO(last in, first out) like 구덩이!
- list의 append(), pop() 으로 그대로 구현

- 가장 top에 있는 숫자와 크기 비교 후 본인보다 크면 기존 숫자 pop 후 본인 append
- stack이라는 리스트에 값을 담을 경우, minus(-) index 이용하여 stack[:-m]형태로 남은 제거 횟수 반영
'''
num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []  # 담을 빈 리스트
for x in num:
    while stack and m>0 and stack[-1] <x:
        stack.pop()
        m -= 1
    stack.append(x)
if m!=0:
    stack = stack[:-m]

res = ''.join(map(str, stack))
print(res)



''' # case 01. 스택 사용하지 않은 경우
k = len(n) - int(m)
s = n
res = ''
while s:
    if len(res) == (len(n)-int(m)):
        break
    print(s[:len(s)-k+1])
    tmp = [i for i in s[:len(s)-k+1]]
    maxIdx = tmp.index(max(tmp))
    print(maxIdx)
    res += s[maxIdx]
    s = s[maxIdx+1:]
    k -= 1
    print('k',k)
    print('res',res)
    print('s',s)
print(res)'''