
Pancake sort is a sorting algorithm that focuses on decreasing number of reversals instead of decreasing the number of comparisons which is done by traditional sorting techniques. 


It's called pancake sort as it seems like we are flipping pancakes with a spatula, thus, what we can do to sort an array is to use ***flip*** function. 


##Pancake sort algorithm: 

####flip(): 
Reverse all values from the beginning of the unsorted array till the specified index. 
####find_max(): 
Find index of maximum number within the specified range of an unsorted array. 

####pancake_sort(): 
![Unsorted Array](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8ne29l78h8xjku5ch1vc.png)
Iteratively, decrease **current_size** of the array, knowing for a fact that array is sorted in a bottom-up manner. 
- Get the index of maximum value in the unsorted array within specified **current_size**, checks if index of maximum value doesn't equal **current_size - 1**, then we can ***flip(index of maximum value)*** and finally ***flip(current_size - 1)***

![PancakeSort 1](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fit3cvg9d5fcgbxr097w.png)

![PancakeSort 2](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/0ils96uwbepg4gf8aqm7.png)

```python
def flip(arr, i): 
    start = 0 
    while start < i: 
        arr[start], arr[i] = arr[i], arr[start]
        start += 1 
        i -= 1 

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
            flip(arr, current_size - 1)
        current_size -= 1
    return arr


arr = [40, 20, 28, 8, 60, 33]
print(pancake_sort(arr))
```

####Time complexity:

Complexity | value
--- | ---
*Best* | **O(n)**
*Worst* | **O(n^2)**

Writing a Great Post Title
Think of your post title as a super short (but compelling!) description — like an overview of the actual post in one short sentence.
Use keywords where appropriate to help ensure people can find your post by search.
Save changes