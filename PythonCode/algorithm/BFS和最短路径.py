Graph = {
    "A": ["B", "C"],
    "B": ["C", "D", "A"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def BFS(graph, s):
    # 队列记录当前在搜索的元素
    Queue = list()
    Queue.append(s)
    # 记录已经遍历过的元素
    seen = set()
    seen.add(s)
    # 父亲表
    parents = dict()
    parents[s] = None
    # 队列不空
    while len(Queue) > 0:
        # 取出开头元素和对应有联系的元素
        vertex = Queue.pop(0)
        nodes = graph[vertex]

        for i in nodes:
            # 如果其联系的元素已经搜索过就跳过，否则添加到下一个要搜索的列表，将该元素设置为已经看过，记录其父元素
            if i not in seen:
                Queue.append(i)
                seen.add(i)
                parents[i] = vertex
    return parents


def getPath(fr, to):
    parents = BFS(Graph, fr)
    print(parents)
    path = list()
    while to != None:
        path.append(to)
        to = parents[to]
    path.reverse()
    return path


path = getPath("A", "F")
print(" ".join(path))
