n, k = map(int, input().split())
index = 0

while True :
    if n % k != 0:
        n -= 1
        index += 1

    elif n % k == 0:
        n = n/k
        index += 1

    if n == 1:
        break

print(index)
