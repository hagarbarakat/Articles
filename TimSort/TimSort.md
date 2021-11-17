**Tim sort** is a hybrid, stable sorting algorithm which uses insertion sort to sort small blocks and then merge them using merge function of merge sort, the idea is that insertion sort is typically faster for small arrays.  
It is used by sort built-in functions used in python and java languages.
Technically, **Tim sort** was implemented in 2002 by Tim Peters in to be used in Python.

##How it works: 
1. An array is divided to number of blocks known as ***Runs,*** the size of a ***Run*** is either 32 or 64 depending on the size of the array, if the size of an array is less than the **run** then the whole array is sorted just by using insertion sort. 
![Array](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/h1r02874rdzs6vfziaqo.png)
2. Sort each **run** using insertion sort.
![runs](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lzyy713ovdr1z98k9mn3.png)
![sort](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nq2t5vq2x26hr9i3n1lf.png)
3. Merge sorted **run** using merge function of merge sort.
4. Double the size of merged subarray after each iteration.  
![sorted array](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dbihy7g4p51optj335p5.png)

##What's minimum run? 
Minimum run is the smallest size of each **run**, ***minimum run*** shouldn't be: 
- too big as insertion sort is faster with small array.
- too small so that it will give more number of runs that will be merged through merge function of merge sort.  

For better results make sure that size of subarrays **size of array/minimum run** is of power of 2 as merge function of merge sort performs better with this case.
```python 
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

```

###Complexity: 
####Time Complexity: 

Complexity | value
--- | ---
*Best* | **O(n)**
*Average* | **O(n log n)**
*Worst* | **O(n log n)**

#####Best Case: **O(n)** 
- Happens when the array is already sorted.

#####Worst Case: **O(n log n)**
- Happens when the array is sorted in reverse order. 

####Space Complexity: **O(n)**

