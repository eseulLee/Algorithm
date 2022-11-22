import sys
sys.stdin = open('../input.txt', 'rt')

'''
- stack에 괄호를 하나씩 쌓아주면서 (와 쌍인 )가 나올 때마다 스택에서 ( 제거
- pipe의 합계는 res += len(s) 형태로 진행
- 닫힌 괄호가 쓰인 경우 1) 레이저(기존 막대 개수 그대로 추가) 2) 막대기의 끝(시작되었던 괄호 하나 제거)
'''

s = input()
stack = []
res = 0
for i in range(len(s)):
    if s[i] == '(' :
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == '(' :
            res += len(stack)
        else:
            res += 1
print(res)