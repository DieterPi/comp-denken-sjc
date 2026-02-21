def faculteit(n):
    if n == 0:
        return 1
    else:
        return n * faculteit(n - 1)
