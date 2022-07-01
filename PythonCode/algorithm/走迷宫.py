import queue


# 四个方向：右，上，下，左
dirs = [ (-1, 0), (0, -1),(0, 1), (1, 0)]


def check(maze, pos):
    return maze[pos[0]][pos[1]] == 0


def mark(maze, pos):  # 给迷宫maze的位置pos标"2"表示“倒过了”
    maze[pos[0]][pos[1]] = 2


def dfs(maze, pos, end):
    # 标记已经走过，防止死循环
    mark(maze, pos)
    if pos == end:
        # 打印终点
        print(pos)
        return True

    for i in range(0, 4):
        nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        # 计算出下一个位置，检查能不能通过，然后状态转换
        if check(maze, nextp):
            if dfs(maze, nextp, end):
                # 返回True就代表这条路可以走，打印出来
                print(pos)
                return True
    # 没找到路，return False
    return False
def getPath(maze,parents,to):
    path = list()
    while to != None:
        path.append(to)
        to = parents[to]
    path.reverse()
    see_path(maze,path)
    return path


def bfs(maze,start,end):
    parent = dict()
    parent[start] = None
    path = []
    q = queue.Queue()
    mark(maze,start)
    q.put(start)
    while not q.empty():
        pos = q.get()
        for i in range(0,4):
            nextp = dirs[i][0] + pos[0] , dirs[i][1] + pos[1]
            if check(maze,nextp):
                parent[nextp] = pos
                if nextp == end:
                    path.append(nextp)

                    getPath(maze,parent,end)
                    return path
                mark(maze,nextp)
                q.put(nextp)
                path.append(nextp)


def see_path(maze,path):     #使寻找到的路径可视化
    for i,p in enumerate(path):
        if i==0:
            maze[p[0]][p[1]] ="E"
        elif i==len(path)-1:
            maze[p[0]][p[1]]="S"
        else:
            maze[p[0]][p[1]] =3
    print("\n")
    for r in maze:
        for c in r:
            if c==3:
                print('\033[0;31m'+"*"+" "+'\033[0m',end="")
            elif c=="S" or c=="E":
                print('\033[0;34m'+c+" " + '\033[0m', end="")
            elif c==2:
                print('\033[0;32m'+"#"+" "+'\033[0m',end="")
            elif c==1:
                print('\033[0;;40m'+" "*2+'\033[0m',end="")
            else:
                print(" "*2,end="")
        print()
def solution():
    start = (1, 1)
    end = (10, 12)
    maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    # dfs(maze, start, end)
    bfs(maze,start,end)
    # see_path(maze,path)
solution()
