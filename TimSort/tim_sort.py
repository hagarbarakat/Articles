minrun = 32
def min_run(n): 
    run = 0 
    while n >= minrun:
        run |= n & 1 
        n >>= 1 
    return n + run

def insertion_sort(arr, left, right): 
    for i in range(left + 1, right + 1): 
        j = i 
        while j > left and arr[j] < arr[j - 1]: 
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def merge(arr, left, mid, right): 
    len_arr1, len_arr2 = mid - left + 1, right - mid
    left_arr, right_arr = [],[]
    for i in range(0, len_arr1): 
        left_arr.append(arr[left + i])
    for i in range(0, len_arr2): 
        right_arr.append(arr[mid + 1 + i])
    
    i, j, k = 0, 0, left
    while i < len_arr1 and j < len_arr2:
        if left_arr[i] <= right_arr[j]: 
            arr[k] = left_arr[i]
            i += 1
        else: 
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len_arr1: 
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len_arr2:
        arr[k] = right_arr[j]
        j += 1
        k += 1

def tim_sort(arr): 
    minimum_run = min_run(len(arr))
    for start in range(0, len(arr), minimum_run): 
        end = min(start + minimum_run - 1, len(arr) - 1)
        insertion_sort(arr, start, end)

    size = minimum_run
    while size < len(arr): 
        for left in range(0, len(arr), 2 * size): 
            mid = min(len(arr) - 1, left + size - 1)
            right = min(left + 2 * size -1, n - 1)
            merge(arr, left, mid, right)
        size = 2 * size 

array = [4, 14, 52, 21, 6, 40, 19, 13] 
  
print("Array:") 
print(array) 
  
tim_sort(array) 
  
print("Sorted Array:") 
print(array)
