n = int(input())

if n < 0:
    print("Số lượng phần tử không hợp lệ")
elif n == 0:
    print("Mảng không có phần tử")
else:
    numbers = []

    for i in range(n):
        number = float(input())
        numbers.append(number)

    count = 0

    for number in numbers:
        if number < 0 and number == int(number):
            count += 1

    print(count)