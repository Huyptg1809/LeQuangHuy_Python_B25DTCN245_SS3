n = int(input())

if n < 0:
    print("Số lượng phần tử không được âm")
elif n == 0:
    print("Mảng không có phần tử")
else:
    characters = []

    for i in range(n):
        char = input()
        characters.append(char)

    total = 0
    found = False

    for char in characters:
        if char.lstrip("-").isdigit():
            total += int(char)
            found = True

    if found:
        print(total)
    else:
        print("Không có phần tử nào là số")