def flip(arr, i): 
    start = 0 
    while start < i: 
        arr[start], arr[i] = arr[i], arr[start]
        start += 1 
        i -= 1 
    print(arr)

def find_max(arr, current_size): 
    mi = 0 
    for i in range(0, current_size): 
        if arr[i] > arr[mi]: 
            mi = i
    return mi 

def pancake_sort(arr): 
    current_size = len(arr) 
    while current_size > 1: 
        mi = find_max(arr, current_size)
        if mi != current_size - 1: 
            flip(arr, mi)
            flip(arr, current_size -1)
        current_size -= 1
    return arr


arr = [40, 20, 28, 8, 60, 33]
print(pancake_sort(arr))
