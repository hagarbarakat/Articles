# Pattern Searching - Naïve Algorithm
Pattern Searching algorithm is string matching algorithm which is used to find a pattern or a substring in another string.

# 1) Naïve Algorithm: 

![string and pattern](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qy1ywwfzb8bulwj0wbc4.png)
- Slide the pattern over the string and check for the match.
![Search 1](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/j5x3wzdbq6i5qmbmgffk.png)
- Once you find the match, start iterating through the pattern to check for the subsequent matches. 
![Search 2](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/p5bu3zqfb9oy0oiu875q.png)
- Length of pattern has to be less or equal to length of string, if pattern's length is greater than length of string return pattern not found.
```python
def naïve_algorithm(string, pattern):
    n = len(string)
    m = len(pattern)
    if m > n: 
        print("Pattern not found")
        return
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if string[i + j] != pattern[j]:
                break
            j += 1
        if j == map:
            print("Pattern found at index: ", i)

string = "hello"
pattern = "ll"
naïve_algorithm(string, pattern)

```
### Time Complexity: 
Complexity | value
--- | ---
*Best* | **O(n)**
*Worst* | **O(m * n)**

- Where **m** is the length of **pattern** and **n** is the length of **string**.
#### Best Case - O(n): 
Happens when the string doesn't have the pattern. 
#### Worst Case - O(m * n): 
Happens when: 

- All characters in both string and pattern are the same. 
- All characters in both string and pattern are the same except for the last character. 

