import sys
sys.stdin = open('../input.txt', 'rt')
'''
sol) dictionary 사용!
- 문자, 단어도 key값으로 사용 가능(!= list)
- 단어를 key, value를 1로 한 dictionary를 만들고 n-1개의 단어가 들어올 때 value를 0으로 바꿈
- 1로 남은 단어가 쓰이지 않은 단어!
'''
n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1
for i in range(n-1):
    word = input()
    p[word] = 0

for key, val in p.items():
    if val == 1:
        print(key)
        break

'''n = int(input())
words = [input() for _ in range(n)]
for _ in range(n-1):
    words.remove(input())
print(words[0])'''
