a, b = [1, 10]

for i in range(a, b + 1):
    num = i
    print(f"{i} = ",end="")
    while num > 1:
        for j in range(2, num + 1):
            if num % j == 0:
                # 如果能被2-i之间的数整除，就将商继续整除
                num = num // j
                if num == 1:
                    print(f"{j}")
                else:
                    print(f"{j} * ",end="")
                break

