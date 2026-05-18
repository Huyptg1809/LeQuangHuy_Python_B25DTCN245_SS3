n = int(input())

if n == 0:
    print("Không có ký tự số")
else:
    characters = []
    
    for i in range(n):
        char = input()
        characters.append(char)

    result = []

    for char in characters:
        if char.isdigit():
            result.append(char)

    if len(result) > 0:
        print(*result)
    else:
        print("Không có ký tự số")