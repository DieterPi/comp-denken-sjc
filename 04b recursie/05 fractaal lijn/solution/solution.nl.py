def lijn(n):
    if n == 1:
        print("-")
    else:
        lijn(n - 1)
        print("-" * n)
        lijn(n - 1)
