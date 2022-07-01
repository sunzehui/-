arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lp = 0
rp = len(arr) - 1
while lp < rp:
    if arr[lp] % 2 == 0:
        arr[lp], arr[rp] = arr[rp], arr[lp]
        rp -= 1
    else:
        lp += 1
print(arr)
