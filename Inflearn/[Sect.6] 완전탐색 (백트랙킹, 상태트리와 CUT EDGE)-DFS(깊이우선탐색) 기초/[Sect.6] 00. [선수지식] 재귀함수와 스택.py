import sys
sys.stdin = open('../input.txt', 'rt')

def DFS(x):
    if x>0:
        # print(x, end=' ') < 여기에 print 걸었을 때는 3 2 1 출력 (선 print 후 stack)
        DFS(x-1)
        print(x, end=' ') # stack에 DFS(3) > DFS(2) > DFS(1) > DFS(0) 순으로 쌓였다가 하나씩 호출되면서 거꾸로 출력이 일어나게 됨

if __name__=="__main__":
    n = int(input())
    DFS(n)