speed = [1, 2, 5, 10]


def solution():
    left = len(speed)
    ans = 0
    while left > 0:
        if left == 1:
            ans += speed[0]
            break
        elif left == 2:
            ans += speed[0] + speed[1]
            break
        elif left == 3:
            ans += speed[0] + speed[1] + speed[2]
            break
        else:
            s1 = speed[0] + speed[1] + speed[1] + speed[left - 1]
            s2 = speed[left - 1] + speed[left - 2] + 2 * speed[0]
            ans += min(s1, s2)
            left -= 2
    return ans


r = solution()
print(r)
