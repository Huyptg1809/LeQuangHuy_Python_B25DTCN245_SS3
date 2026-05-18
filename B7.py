n = int(input())

if n < 0:
    print("Số lượng phần tử không được nhỏ hơn 0")
elif n == 0:
    print("Không phải dãy số fibonacci")
else:
    numbers = []

    for i in range(n):
        number = int(input())
        numbers.append(number)

    is_fibonacci = True

    if n >= 3:
        for i in range(2, n):
            if numbers[i] != numbers[i - 1] + numbers[i - 2]:
                is_fibonacci = False
                break

    if is_fibonacci:
        print("Là dãy số fibonacci")
    else:
        print("Không phải dãy số fibonacci")