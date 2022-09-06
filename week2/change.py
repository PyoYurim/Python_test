change = int(input("숫자를 입력해 주세요 : "))

array = [500, 100, 50, 10]

for x in array:
    result = change // x
    change = change % x
    print(f"{x}원의 개수는 {result}개 입니다.")

