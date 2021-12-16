def naïve_algorithm(string, pattern):
    n = len(string)
    m = len(pattern)
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
