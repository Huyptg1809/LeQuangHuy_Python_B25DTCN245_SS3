numbers = list(map(int, input().split()))

result = []

for number in numbers:
    if number >= 10:
        result.append(number)

if len(result) > 0:
    print(*result)
else:
    print("Không có số nào lớn hơn 10")