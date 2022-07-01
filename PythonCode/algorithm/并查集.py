N = 16
edges = [

]

for i in range(N):
    edges.append(tuple(map(int, input().split())))
print(edges)
print(len(edges))
parent = [-1] * 999


def find_root(x, parent):
    x_root = x
    while parent[x_root] != -1:
        x_root = parent[x_root]
    return x_root


def union(x, y, parent):
    x_root = find_root(x, parent)
    y_root = find_root(y, parent)
    if x_root == y_root:
        return False
    else:
        parent[x_root] = y_root
        return True


cnt = 0
for i in range(len(edges)):
    x = edges[i][0]
    y = edges[i][1]
    if union(x, y, parent) == False:
        print("cycle")
        cnt += 1
print(cnt)
print("no")
print(parent)
