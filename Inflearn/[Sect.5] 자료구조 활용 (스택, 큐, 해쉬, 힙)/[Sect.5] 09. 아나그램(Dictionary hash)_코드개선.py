import sys
sys.stdin = open('../input.txt', 'rt')

'''
☆ str1.get('A',0) : str1이라는 딕셔너리에 A라는 key값이 없으면 0, 있으면 그 value값 return
단어에 사용된 알파벳의 수 count해서 누적
최종적으로 dict 같은지 비교
'''
a = input()
b = input()
sH = dict()
for x in a:
    sH[x] = sH.get(x, 0) + 1

for x in b:
    sH[x] = sH.get(x, 0) - 1   # 원 상태로 복귀 > 다 있으면 0이 될 것!

for x in a:
    if sH.get(x) > 0 :
        print('NO')
        break
else:
    print('YES')