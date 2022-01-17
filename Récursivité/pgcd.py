def pgcd(a, b):
        if a < b:
            a, b = b, a
        reste = a%b
        if reste == 0:
            return b
        else:
            return pgcd(b, reste)

print(pgcd(1540, 4950))
