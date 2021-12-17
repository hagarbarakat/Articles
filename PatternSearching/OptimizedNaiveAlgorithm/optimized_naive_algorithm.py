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
