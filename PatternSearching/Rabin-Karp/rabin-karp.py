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
        print(ord(pattern[i]))
        print(p)
        s = (d*s + ord(string[i])) % q
    print(p)
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
