num = 0.625
s = ['0', '.']
while num > 0:
    v = num * 2
    if v >= 1:
        s.append('1')
        num = v - 1
    else:
        s.append('0')
        num = v
result = "".join(s)
print(result)
