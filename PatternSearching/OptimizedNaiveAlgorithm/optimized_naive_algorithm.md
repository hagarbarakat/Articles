# Pattern Searching - Optimized Naïve Algorithm
Assume that all characters of pattern are different, in this case we can slide the pattern by more than 1 when a mismatch occurs. 
![string and pattern](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/eeqndcx6ied5zqwwfn23.png)
- All characters of pattern are different.
![slide by j](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/e8hhii7h4k5kh90jow77.png)
- Slide by j.
![search 1](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/r927f649npl2s59b60u9.png)
![pattern found](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ttk7fti24vwlrj3axt7p.png)
```python
def optimized_naïve_search(string, pattern):
    n = len(string)
    m = len(pattern)
    i = 0
    while i <= (n - m):
        for j in range(m):
            if string[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            print("pattern found at index: ", i)
            i = i + m
        elif j == 0:
            i += 1
        else:
            i = i + j


string = "abeabc"
pattern = "abc"
optimized_naïve_search(string, pattern)

```
 