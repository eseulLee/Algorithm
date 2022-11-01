import sys
sys.stdin = open('../input.txt', 'rt')

T = int(input())

for t in range(T) :
    n, s, e, k = map(int, sys.stdin.readline().split())
    test = list(map(int, sys.stdin.readline().split()))
    print('#{} {}'.format(t+1, sorted(test[s-1:e])[k-1]))
    # test 리스트의 s~e번째 slicing 시, 끝은 포함되지 않음 주의
