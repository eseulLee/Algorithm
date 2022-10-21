import sys
# import numpy as np
sys.stdin = open('input.txt', 'rt')

n = int(input())
score = list(map(int, input().split()))

# round > round_half_even 방식 사용!
# 딱 .5에 걸려있을 때 다른 결과 나올 수 있으므로 안전하게!
scoreAvg = int((sum(score) / n) + .5)

gapMin = 2147000000

for idx, val in enumerate(score):
    tmp = abs(val - scoreAvg)
    if tmp < gapMin:
        gapMin = tmp
        score_ = val
        res = idx + 1
    elif tmp == gapMin:
        if val > score_:
            score_ = val
            res = idx + 1

print(scoreAvg, res)

