inp = "adcb"
arr = list(inp)

# for i in range(0,len(arr)):
#     for j in range(i,len(arr)-1):
#         if arr[j] > arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]

arr.sort()

print(arr)
