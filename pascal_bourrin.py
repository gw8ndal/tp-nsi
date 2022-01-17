def pascal_bourrin(n, p):
    if p == 0 or n == p:
        return 1
    else:
        p1 = pascal_bourrin(n-1, p-1)
        p2 = pascal_bourrin(n-1, p)
        return p1 + p2
print(pascal_bourrin(50,30))
