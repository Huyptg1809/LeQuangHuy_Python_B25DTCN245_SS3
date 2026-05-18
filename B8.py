def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


numbers = []

while True:
    print("================== MENU ===================")
    print("1. Nhập số phần tử cần nhập và giá trị các phần tử")
    print("2. In ra giá trị các phần tử đang quản lý")
    print("3. In ra giá trị các phần tử chẵn và tính tổng")
    print("4. In ra giá trị lớn nhất và nhỏ nhất trong mảng")
    print("5. In ra các phần tử là số nguyên tố trong mảng và tính tổng")
    print("6. Nhập vào một số và thống kê trong mảng có bao nhiêu phần tử đó")
    print("7. Thêm một phần tử vào vị trí chỉ định")
    print("8. Thoát")
    print("============================================")

    choice = int(input("Lựa chọn của bạn: "))

    if choice == 1:
        n = int(input("Nhập số phần tử: "))

        numbers = []

        for i in range(n):
            number = int(input(f"Nhập phần tử thứ {i + 1}: "))
            numbers.append(number)

    elif choice == 2:
        print(numbers)

    elif choice == 3:
        even_numbers = []
        total = 0

        for number in numbers:
            if number % 2 == 0:
                even_numbers.append(number)
                total += number

        print("Các số chẵn:", even_numbers)
        print("Tổng:", total)

    elif choice == 4:
        if len(numbers) == 0:
            print("Mảng không có phần tử")
        else:
            print("Số lớn nhất:", max(numbers))
            print("Số nhỏ nhất:", min(numbers))

    elif choice == 5:
        prime_numbers = []
        total = 0

        for number in numbers:
            if is_prime(number):
                prime_numbers.append(number)
                total += number

        print("Các số nguyên tố:", prime_numbers)
        print("Tổng:", total)

    elif choice == 6:
        x = int(input("Nhập số cần thống kê: "))
        count = 0

        for number in numbers:
            if number == x:
                count += 1

        print("Số lần xuất hiện:", count)

    elif choice == 7:
        value = int(input("Nhập giá trị cần thêm: "))
        position = int(input("Nhập vị trí cần thêm: "))

        if position < 0 or position > len(numbers):
            print("Vị trí không hợp lệ")
        else:
            numbers.insert(position, value)
            print(numbers)

    elif choice == 8:
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ")