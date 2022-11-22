import sys
sys.stdin = open('../input.txt', 'rt')

a = input()
stack = []
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        a = stack.pop()
        b = stack.pop() # 먼저 들어간 거
        if x == '+':
            stack.append(b + a)
        elif x == '-' :
            stack.append(b - a)
        elif x == '*' :
            stack.append(b * a)
        elif x == '/' :
            stack.append(b / a)
print(stack[0])