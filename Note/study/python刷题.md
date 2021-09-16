```python
# 创建二维数组
arr = [[0] * m for i in range(0, n)]
# enumerate每次循环可以得到下表及元素
for i in range(0, n):
    line = input().split()
    for j, v in enumerate(line):
        arr[i][j] = v
```

```python
# 将输入的字符串转为数组
arr = list(inp)
# 从0开始取出所有奇数索引元素
ret = arr[1::2]
```

```python
# A^A = 0 ; A^A^A = A
```

```python
# (x - 1) & x 的效果：消掉最低位的1
```

#### 用数组表示一棵树（层序遍历）

子节点：左： $2*i+1$    右： $2*i+1$

父节点：$\frac{i-1}{2}$ （向下取整）