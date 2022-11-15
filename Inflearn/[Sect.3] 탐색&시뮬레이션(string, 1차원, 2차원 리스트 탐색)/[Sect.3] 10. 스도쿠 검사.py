import sys
sys.stdin = open('../input.txt', 'rt')

# a = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

''' # case 01.
# 행/열 검사
res = 'YES'
for i in range(9) :
    if len(set(a[i])) != 9:
        res = 'NO'

    tmp = [a[j][i] for j in range(9)]
    if len(set(tmp)) != 9:
        res = 'NO'

for i in [0, 3, 6]:
    for j in [0, 3, 6]:
        tmp = []
        for k in range(3):
            for l in range(3):
                tmp.append(a[i+k][j+l])
                print(i+k, j+l)
        if len(set(tmp)) != 9:
            res = 'NO'
print(res)
'''

# case 02.
def check(x):
    for i in range(9):
        chk1 = [0]*10
        chk2 = [0]*10
        for j in range(9):
            chk1[x[i][j]] = 1
            chk2[x[j][i]] = 1
        if (sum(chk1) != 9)  or (sum(chk2) != 9):
            return False
    for i in range(3):
        for j in range(3):
            chk3 = [0]*10
            for k in range(3):
                for s in range(3):
                    chk3[x[i*3+k][j*3+s]] = 1
            if sum(chk3) != 9:
                return False
    return True

a = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

if check(a):
    print('YES')
else:
    print('NO')