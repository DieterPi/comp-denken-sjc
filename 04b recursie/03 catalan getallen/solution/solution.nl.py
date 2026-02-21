def catalan(n):
    if n == 0:
        return 1
    else:
        return (4 * n - 2) * catalan(n - 1) // (n + 1)
