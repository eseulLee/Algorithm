import sys
sys.stdin = open('../input.txt', 'rt')
'''
- 키 기준 리스트 정렬
- 아래로 갈수록 키는 점점 작아지기 때문에 위에 나온 지원자를 이기려면 몸무게가 무조건 더 많이 나가야 함
- 몸무게만 따져가면서 최대값 저장해서 비교하는 형태로 진행
 >> 이중 for문으로 인한 시간복잡도 증가 방지 가능
'''
n = int(input())
cand = [ tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
cand.sort(reverse=True)

cnt = 0
maxh = 0
for h, w in cand:
    if w > maxh :
        cnt += 1
        maxh = w
print(cnt)

