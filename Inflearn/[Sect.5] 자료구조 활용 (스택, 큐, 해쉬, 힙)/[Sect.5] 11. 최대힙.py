import sys
sys.stdin = open('../input.txt', 'rt')
import heapq as hq
'''
heapq 는 기본적으로 최소힙으로 작동
최소힙을 이용해서 최대힙을 하려면? 
>> 부호를 바꿔서 큰 값을 작은 값으로 바꾸기!
>> 입/출력시에 부호를 바꿔주면 OK
'''
a = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a)) # 출력시 음수>양수로 변환
    else:
        hq.heappush(a, -n) # push할 때 양수>음수로 변환하여 push