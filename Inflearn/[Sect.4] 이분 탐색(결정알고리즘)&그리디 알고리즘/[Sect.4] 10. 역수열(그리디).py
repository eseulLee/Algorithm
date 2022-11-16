import sys
sys.stdin = open('../input.txt', 'rt')

'''
- 1~n까지 정렬된 숫자 필요 (오름차순)
- seq라는 0 * n으로 이루어진 리스트 생성하여 해당 숫자를 배치
- 배치시 0의 개수를 세서 진행
- 들어가려던 자리에 자리잡은 숫자가 있는 경우 그 뒤로 들어감
- 1부터 순차적으로 배치가 되기 때문에 무조건 기존의 숫자는 자신보다 작음 주의
'''

'''n = int(input())
a = list(map(int, input().split())) # 역수열
seq = [0] * n   # 원수열 (0~n-1까지 사용)
for i in range(n) :  # 1~n 까지 순차적으로 숫자 입력하기 위한 for문
    for j in range(n) :
        if a[i] == 0 and seq[j] == 0:
            # a[i] == 0 : 자기 앞에 빈 공간을 확보했다 (자신보다 큰 숫자가 들어가야 할)
            # seq[j] == 0 : 자신보다 작은 숫자가 이미 자리를 차지하고 있는 경우 거기엔 하지 말라는 의미
            seq[j] = i+1
            break  # j를 break
        elif seq[j] == 0: # 자기 자리는 못 찼았지만 빈 자리는 맞을 때
            a[i] -= 1 # 빈자리 발견할 때마다 1씩 작아짐 (a는 작아지고 j는 커지는 형태)
for x in seq:
    print(x, end=' ')'''

# 역수열 한번더 풀어보기!
'''
역수열 > 원수열 만들기
idx+1이 원수열로 들어갈 숫자
value가 숫자가 들어갈 위치
1부터 n까지 숫자가 커지기 때문에 순서대로 넣는 거로 하면 앞에 0만 고려해주면 됨
그 자리에 0이 아닌 숫자가 있는 경우, 그 뒤로 넣어줘야 함 고려 필요
'''
n = int(input())
a = list(map(int, input().split()))  # 역수열
seq = [0] * n # 원수열(여기다가 배치해서 넣을 거)

for i in range(n): # 1~n
    for j in range(n): # 들어갈 자리 찾기
        if a[i] == 0 and seq[j] == 0 :
            seq[j] = i+1  # idx는 0부터, 수열은 1부터 시작하기 떄문에 +1
            break
        elif seq[j] == 0: # 내자린 아닌데 빈자린 맞음
            a[i] -= 1  # a[i]를 1씩 빼주면서 seq의 j를 1씩 증가시켜서 위치 이동

for x in seq:
    print(x, end=' ')


