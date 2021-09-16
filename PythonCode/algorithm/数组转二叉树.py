class Array2Tree:
    def preOrder(self, arr, index):
        if index >= len(arr):
            return None
        print(arr[index],end=" ")
        self.preOrder(arr, (2 * index) + 1)
        self.preOrder(arr, (2 * index) + 2)

    def __init__(self):
        pass


arr = [78, 56, 34, 43, 4, 1, 15, 2, 23]
A2T = Array2Tree()
A2T.preOrder(arr, 0)
