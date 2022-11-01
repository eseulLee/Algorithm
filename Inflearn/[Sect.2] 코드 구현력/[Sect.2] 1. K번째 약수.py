import sys
sys.stdin = open("../input.txt", 'rt')

N, K = map(int, input().split())
cnt = 0

for i in range(1, N+1) :
    if N % i == 0 :
        cnt += 1
    if cnt == K:
        print(i)
        break
else:
    print(-1)
    # else문의 경우 for문을 온전히 다 돈 경우에만 출력됨
    # for문을 다 돌았다는 것은? k번째 약수를 찾지 못하고 끝났다는 것 의미미
