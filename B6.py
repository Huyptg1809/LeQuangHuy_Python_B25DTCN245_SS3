n = int(input())

if n < 0:
    print("Số lượng phần tử không được nhỏ hơn 0")
elif n == 0:
    print("Mảng không có phần tử nào")
else:
    numbers = []

    for i in range(n):
        number = int(input())
        numbers.append(number)

    max_number = max(numbers)
    second_max = None

    for number in numbers:
        if number != max_number:
            if second_max is None or number > second_max:
                second_max = number

    print(second_max)