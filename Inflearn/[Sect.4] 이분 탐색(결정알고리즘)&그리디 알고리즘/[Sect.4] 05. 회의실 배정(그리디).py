import sys
sys.stdin = open('../input.txt', 'rt')

'''
Greedy Algorithm
- 현재 단계에서 최선의 답을 선택해 나가는 것
- 보통의 문제에서는 '정렬'해서 차례차례 선택해 나가면 됨

# 문제 접근
- 회의 '끝나는' 시간 기준으로 정렬 필요
 >> why? 회의가 빨리 끝나야 다음 회의를 또 진행할 수 있으니까!
- 회의 시작 시간이 끝나는 시간과 같거나 그보다 큰 경우 회의 진행 가능
 >> 회의 끝나는 시간과 회의 시작 시간 비교
'''

n = int(input())
meeting = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
res = 0

# meeting 끝나는 시간 기준 정렬(key)
meeting.sort(key= lambda x: (x[1], x[0]))

et = 0 # 회의 끝나는 시간
cnt = 0
for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1
print(cnt)