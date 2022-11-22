import sys
sys.stdin = open('../input.txt', 'rt')

'''
연산자 우선순위: */ > +-
- stack에는 연산자만 담는다
- 숫자는 그대로 출력하면서 진행됨에 따라 연산자 중간중간 출력
- 괄호의 경우 일단 append, 닫힌 괄호를 만나야 꺼낼 수 있음(쌍이니까)
- 괄호 안에서 연산자 등장한 경우, 열린 괄호 전까지 쌓여있는 연산자 확인 필요
'''

S = input()
stack = []
res = ''

'''for s in S:
    # 피연산자인 경우
    if s.isdecimal():
        res += s
    # 연산자인 경우
    else:
        if s == '(' :
            stack.append(s)
        elif s == '*' or s == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()   # stack에서 제거하면서 동시에 res에 추가
            stack.append(s)
        elif s == '+' or s == '-' :
            while stack and stack[-1] != '(' :
                res += stack.pop()
            stack.append(s)
        elif s == ')' :
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()  # 열린 괄호 제거

# for문 돌고 나서 stack에 남은 경우 처리
while stack:
    res += stack.pop()

print(res)'''


for x in S:
    if x.isdecimal():
        res+=x
    else:
        if x == '(':
            stack.append(x)
        elif x in ('*', '/'):
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x in ('+', '-'):
            while stack and stack[-1] != '(' :
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()
print(res)