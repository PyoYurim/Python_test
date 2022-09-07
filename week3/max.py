#입력 받기
n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))
#입력받은 수들 정렬
num_list.sort()

first = num_list[n - 1]
second = num_list[n - 2]

result = 0

while True:
    for num in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)






