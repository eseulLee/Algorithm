import sys
sys.stdin = open('../input.txt', 'rt')

'''
☆ str1.get('A',0) : str1이라는 딕셔너리에 A라는 key값이 없으면 0, 있으면 그 value값 return
단어에 사용된 알파벳의 수 count해서 누적
최종적으로 dict 같은지 비교
'''
a = input()
b = input()
str1 = dict()
str2 = dict()
for x in a:
    str1[x] = str1.get(x, 0) + 1
for x in b:
    str2[x] = str2.get(x, 0) + 1

for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i] :
            print('NO')
            break
    else:
        print('NO')
        break
else:
    print('YES') # 아나그램일 경우, for문을 다 돌고 정상적으로 종료할 것! 따라서 else문에 YES 달아준다

'''a = input()
dica = dict()
for x in a:
    if x in dica:
        dica[x] += 1
    else:
        dica[x] = 1

b = input()
dicb = dict()
for x in b:
    if x in dicb:
        dicb[x] += 1
    else:
        dicb[x] = 1

if sorted(dica.items()) == sorted(dicb.items()):
    print('YES')
else:
    print('NO')
'''