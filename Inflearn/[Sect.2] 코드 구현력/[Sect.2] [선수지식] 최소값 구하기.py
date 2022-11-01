# 최소값 구하기

arr = [5, 3, 7, 9, 2, 5, 2, 6]

# python에서 가장 큰 값으로 변수 초기화
# arr[0] 으로 해줘도 됨!
arrMin = float('inf')

# arrMin 변수에 arr 리스트 중 가장 작은 값이 저장되도록 알고리즘 짜기
for i in range(len(arr)):
    if arr[i] < arrMin:
        # 값이 중복된 경우 뒤의 값의 index를 가져오라고 할 때는 <= 으로 해준다
        arrMin = arr[i]
print(arrMin)