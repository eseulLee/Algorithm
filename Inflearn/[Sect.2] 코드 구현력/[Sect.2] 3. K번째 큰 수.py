import sys
sys.stdin = open("../input.txt", 'rt')

n, k = map(int, sys.stdin.readline().split())
num_lst = list(map(int, sys.stdin.readline().split()))
result = set()  # set은 중복을 제거!
for i in range(n):
   for j in range(i+1, n):
       for l in range(j+1, n):
           result.add(num_lst[i] + num_lst[j] + num_lst[l])
res = sorted(list(result), reverse=True) # set은 sort가 되지 않으므로 리스트로 형변환 필요
print(res[k-1])

