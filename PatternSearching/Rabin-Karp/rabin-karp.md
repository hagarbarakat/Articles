***Rabin-Karp*** is an algorithm used for pattern matching/searching in a string that uses a hash function unlike the ***naïve algorithms***.
## How it works

![Intro](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gt1gtpsaola8kdmc9tc9.png)

- We will iterate through the string with a window with the same length of the pattern. 

![hashing](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ea4oym13v0hzbc9d45yh.png)

- We will calculate a hash value for the pattern and the window of the string and check if: 

- The hash value of pattern equals the hash value of window of string, check each character of the window with the pattern as two distinct strings may have the same hash value due to **collisions**

- The hash value of pattern isn't equal to the hash value of window of string, then check hash value of the next window with the hash value of the pattern and so on. 

![hashing 2](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/g2j10u17m2fqvk01dd90.png)

![hashing 3](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/unb85uth65hwlso6zug1.png)

## How to calculate the hash function: 
The hash function here is used to map a string to an integer value. 
To get a useful hash function it should: 

- be easily calculated 
- can perform precalculations.
- calculating the hash function of any string takes constant time **O(1)**


## Python code: 
```python
# q is a prime number -modulus-
def rabin_karp(string, pattern, q):
    d = 256
    n = len(string)
    m = len(pattern)
    s = 0
    p = 0
    h = 1
    i = 0
    j = 0
    for _ in range(m - 1):
        h = (h*d) % q
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        s = (d*s + ord(string[i])) % q
    for i in range(n - m + 1):
        if p == s:
            for j in range(m):
                if string[i+j] != pattern[j]:
                    break
            j += 1
            if j == m:
                print("pattern found at index:", i)
        if i < n-m:
            s = (d * (s - ord(string[i])*h) + ord(string[i + m])) % q
        if s < 0:
            s = s + q


string = "ABCDAF"
pattern = "DAF"
q = 113
rabin_karp(string, pattern, q)
```

## Limitations: 
## #Spurious Hit: 
A ***spurious hit*** occurs when two distinct strings have the same hash value. It increases the time complexity of the algorithm. 
To reduce the occurrence of spurious hits, we use modulus. 

## Time Complexity: 
The average case and best case complexity of Rabin-Karp is `O(m + n)`
The worst case complexity is `O(nm)`, which happens when: 
- all characters of pattern and text are same as the hash values of all windows of string will match with hash value of pattern. 
- spurious hit occurs for every window.  

However, if we use a good hashing function, the expected complexity would be `O(n + k . t)`, where t is the number of matches.

As a good hashing function would rarely cause collisions. Thus, we would rarely need to compare two substrings when there is no match. 

>  **If we only want to check the existence of the pattern, the complexity would be `O(n+k)`, as we can break the loop after the first occurrence.**
