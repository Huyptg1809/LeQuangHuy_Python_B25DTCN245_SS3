numbers = list(map(int, input().split()))

if len(numbers) == 0:
    print("Không có số lớn nhất")
else:
    max_number = numbers[0]
    position = 0

    for i in range(len(numbers)):
        if numbers[i] > max_number:
            max_number = numbers[i]
            position = i

    print(f"Số lớn nhất: {max_number}")
    print(f"Vị trí: {position}")