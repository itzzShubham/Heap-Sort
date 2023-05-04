def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        Heap(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        Heap(arr, i, 0)
    print(arr)

def Heap(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] 
        Heap(arr, n, largest)

arr = [10,0,1,7,2,36,8,5]
heap_sort(arr)