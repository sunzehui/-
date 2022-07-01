def solution(num_rows):
    triangle = []
    # 以下均从起始下标0开始
    # 解法：每一行的第0个元素和最后一个元素都是1
    # 本行i的第1个元素等于上一行（i-1)左边和本行同位置元素之和
    for num in range(num_rows):
        # 生成当前行,大小是行号+1,第0行一个元素,第1行两个元素
        row = [None for i in range(num + 1)]
        # 第0个元素和最后一个元素都是1
        row[0], row[-1] = 1, 1
        # 起始下标1,跳过第0,1行
        for i in range(1, len(row) - 1):
            row[i] = triangle[num - 1][i] + triangle[num - 1][i - 1]
        triangle.append(row)
    return triangle


r = solution(5)
for i in r:
    print(i)
# 算法评估:
#   时间复杂度O(n**2)
#   空间复杂度O(n**2)
