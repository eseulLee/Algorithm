import sys
sys.stdin = open('../input.txt', 'rt')

# from collections import deque
'''
- 양쪽 끝에서부터 lt, rt로 변수에 할당하여 시작
- 빈 tmp 리스트에 양 끝값이 모두 last(증가수열 생성시 기억해야할 전 값)보다 큰 경우 저장
- tmp 내에서 크기 비교하여 더 작은 값으로 선택
- L, R을 tuple 형태로 값과 함께 저장하게 됨
- tuple.sort() 시에 (A, B)에서 A에 의해 정렬
- last값 갱신과 res에 문자 붙이기 동시에 진행
- 양 끝 값 중 하나 선택되면서 lt/rt 1증가/감소
  
'''
n = int(input())
a = list(map(int, input().split()))
# a = deque(a)
lt = 0
rt = n-1
last = 0
res = ''
tmp = []
while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))
    if a[rt] > last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0 :
        break
    else:
        res += tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L' :
            lt += 1
        else:
            rt -= 1
    tmp.clear()

print(len(res))
print(res)
