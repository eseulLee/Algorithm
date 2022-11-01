import sys
sys.stdin = open('../input.txt', 'rt')

'''
[접근]
1. 입력 n 크기의 리스트 생성(값은 0으로 초기화)
2. 소수의 대상에 1는 포함되지 않으므로 2부터 시작 ~ n까지
ex. 2의 경우
- 리스트의 2번째 원소에 chk하고 cnt를 1증가
- 소수 2의 배수인 4, 6, 8 등에 chk == 소수가 아님 (체로 거르는 행위)
'''

n = int(input())
chk = [0] * (n+1)
cnt = 0

for i in range(2, n+1):
    if chk[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            chk[j] = 1
print(cnt)

