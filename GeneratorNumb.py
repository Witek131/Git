def generate(n: int, m: int, prefix=None):  # n чмслa m длинна
    if m == 0:
        print(prefix)
        return
    prefix = prefix or []
    for i in range(n):
        prefix.append(i)
        generate(n, m - 1, prefix)
        prefix.pop()
generate(3, 5)