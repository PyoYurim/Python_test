# 더하기 연산

array = [2, 5, 6, 8, 4]    # 5개의 데이터(N = 5)
sum = 0                    # 합계를 저장할 변수

# 모든 데이터를 하나씩 확인하며 합계를 계산
for x in array:
    sum += x

# 결과 출력
print(sum)