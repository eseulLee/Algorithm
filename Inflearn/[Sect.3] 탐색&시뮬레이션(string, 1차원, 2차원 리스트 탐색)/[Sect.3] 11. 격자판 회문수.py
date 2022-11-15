import sys
sys.stdin = open('../input.txt', 'rt')

a = [list(map(int, sys.stdin.readline().split())) for _ in range(7)]
res = 0

for i in range(3):
    for j in range(7):
        # 세로 회문
        for k in range(2):
            if a[i+k][j] != a[i+4-k][j]:
                break
        else:
            res += 1
        # 가로 회문
        for k in range(2):
            if a[j][i+k] != a[j][i+4-k]:
                break
        else:
            res += 1
        ''' tmp 1차원 리스트 이므로 slicing 사용 가능
        tmp = a[j][i:i+5]
        if tmp == tmp[::-1]:
            res += 1
        '''
print(res)
