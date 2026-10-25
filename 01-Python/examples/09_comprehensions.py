squares = [n*n for n in range(1, 6)]
evens = {n for n in range(10) if n % 2 == 0}
lookup = {n: n*n for n in range(1, 4)}
print(squares, sorted(evens), lookup)
