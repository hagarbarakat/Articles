#Bucket Sort

#Scatter  Sort  Gather 
**Bucket sort**, also known as **bin sort** is a sorting algorithm where elements of an array are distributed into a number of buckets. 
##How it works 
The array is divided into buckets, each bucket is sorted either by any sorting technique or by recursively applying bucket sort itself and at the end the buckets are combined to have the desired sorted array.
##When to use bucket sort
* Input is floating point numbers
* Input is uniformly distributed over a range 

##Bucket Sort Example
Assume we have an unsorted array of size 7 that contains floating point numbers.
![Input Array](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4fsjt8m0hsrw3trtqjyh.png)
Then we will create another array ***B***, as we have floating point numbers that range from [0,1], thus the best size for the array is 10 where each value will be in its right bucket using this formula: 
**bucket = Int(value * size of array B)**
![Bucket Sort](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/g6selfwhgm33r486364c.png)
Then I used the built-in **list.sort()** method which is tim sorting technique that modifies the list in-place to sort each bucket. 
![Sorted array](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/y82mx831gb3yrj6ebqsz.png)
##Python code
```python
 def bucket_sort(arr): 
    buckets_arr = []
    output = []
    # create buckets 
    for i in range(10): 
        buckets_arr.append([])
    
    #Insert elements in buckets - Scatter
    for value in arr: 
        index = int(len(buckets_arr) * value)
        buckets_arr[index].append(value)

    print("buckets before sorting",  buckets_arr, sep='\n')

    #Sorting in each bucket - Sort
    for i in range(len(arr)):
        buckets_arr[i].sort()

    print("buckets after sorting",  buckets_arr, sep='\n')

    #Gather 
    for i in range(len(buckets_arr)):
        for j in range(len(buckets_arr[i])):
            output.append(buckets_arr[i][j])
    
    return output 

arr = [0.13, 0.8, 0.77, 0.2, 0.11, 0.97, 0.78]
result = bucket_sort(arr)
print("Sorted array", result, sep='\n')
```
##Detect Number of Buckets 
* If the data is floating point numbers that ranges from [0,1], use 10 buckets so that first bucket contains values from [0,1[ and so on. To know the right index: 

**bucket_index = Int(value * size of array B)**
* If the data is numbers between 0 and 1000 for example we can use also 10 buckets or maybe 5 buckets and to know the right index you can use: 

**bucket_index = Int(value/size of array B)**
* If data is string, we can have 26 buckets, each bucket represents a character from a to z. To know the right bucket use first characters to know which bucket it matches with. 

##Time Complexity  

It actually depends on the number of elements in each bucket. 

Complexity | value
--- | ---
*Best* | **O(n+k)**
*Average* | **O(n)**
*Worst* | **O(n^2)**

###Best case - O(n+k) 

Happens when elements are uniformly distributed and number of elements in buckets are nearly equal. 
**O(n)** is the complexity of creating buckets and **O(k)** is the complexity of sorting with a technique that gives linear time complexity at its best. 
 
###Worst case - O(n^2) 

Happens when elements are close in range where elements are likely placed in the same bucket giving buckets with larger number of elements than the others, so, the complexity here depends on the sorting technique used to sort the buckets.

##Space complexity
It depends on size of input array and number of buckets, thus the space complexity of bucket sort if **O(nb)** where ***n*** is number of elements in input array and ***b*** is number of buckets. 

