class job:
    def __init__(self, s, e):
        self.startTime = s
        self.endTime = e

    def __lt__(self, other):
        return self.endTime < other.endTime

    def __str__(self):
        return "start:" + str(self.startTime) + "   end:" + str(self.endTime)


arr = [job(s, e) for s, e in [(1, 3), (2, 5), (4, 7), (6, 9), (8, 10)]]
arr = sorted(arr)
task = [arr[0]]
y = arr[0].endTime
for i in range(1, len(arr)):
    if arr[i].startTime > y:
        task.append(arr[i])
        y = arr[i].endTime

for i in task:
    print(i)
