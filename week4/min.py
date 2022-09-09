# 행과 열 입력 받기
n, m = map(int, input().split())
# 가장 큰 수를 찾기 위한 빈 리스트 만들기
result = []

for i in range(n):
    nums = list(map(int, input().split()))
    num = min(nums)
    # 빈 리스트에 가장 작은 값 추가 해주기
    result.append(num)

print(max(result))







