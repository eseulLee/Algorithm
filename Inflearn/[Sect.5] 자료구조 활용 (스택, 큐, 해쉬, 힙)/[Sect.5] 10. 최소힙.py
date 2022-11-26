import sys
sys.stdin = open('../input.txt', 'rt')

'''
양쪽 자식보다 부모 노드값이 무조건 더 작아야 함 
숫자는 부모 노드에 먼저 입력이 되고, level 별로 채워져 나간다
입력되고 나서 부모와 크기 비교하여 자식이 부모보다 작으면 자리 교환 (up heap)
heap pop 하면 root node 값이 나옴 > 가장 오른쪽 아래(last level)의 노드 값이 부모 노드에 올라오게 되고, 다시 최소힙 진행(down heap)
'''
import heapq as hq

a = []
while True:
    n=int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a)) # a에서 root node 값 꺼내줌
    else:
        hq.heappush(a, n)
