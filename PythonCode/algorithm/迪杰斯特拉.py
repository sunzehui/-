Graph = {
    "A": {"B":5, "C":1},
    "B": {"C":2, "D":1, "A":5},
    "C": {"A":1, "B":2, "D":4, "E":8},
    "D": {"B", "C", "E", "F"},
    "E": {"C", "D"},
    "F": {"D"}
}


def BFS(graph, s):
    Queue = []
    Queue.append(s)
    seen = set()
    seen.add(s)
    parents = {}
    parents[s] = None
    while len(Queue) > 0:
        vertex = Queue.pop(0)
        nodes = graph[vertex]
        for i in nodes:
            if i not in seen:
                Queue.append(i)
                seen.add(i)
                parents[i] = vertex
    return parents


def getPath(fr, to):
    parents = BFS(Graph, fr)
    path = list()
    while to != None:
        path.append(to)
        to = parents[to]
    path.reverse()
    return path


path = getPath("A", "F")
print(" ".join(path))
