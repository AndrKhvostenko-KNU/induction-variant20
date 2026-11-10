def f(n):
    return 6**n + 20*n + 24

m = 25
bad = [n for n in range(1, 101) if f(n) % m != 0]
print("Контрприкладів не знайдено" if not bad else bad)