import sys
sys.stdin = open('../input.txt', 'rt')

n, m = map(int, input().split())
a = list(map(int, sys.stdin.readline().split()))

'''
1. lt, rt 설정 후 mid = (lt + rt)//2 인 mid 생성
2. a[mid] == m 인 경우부터 시작
2-1. True 인 경우 바로 인덱스인 mid 호출 후 종료
2-2. False 인 경우 mid와 비교 후 앞과 뒤 중 한쪽으로만 search
3. rt = mid-1 | lt = mid+1 로 설정 후 재 탐색
 
'''

a.sort()
# print(a.index(m)+1) > 얘 말고 이분탐색으로 해보기

lt, rt = 0, n-1
while lt <= rt:
    mid = (lt+rt) // 2
    if a[mid] == m:
        print(mid + 1)
        break
    elif a[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1
