def findIn(n, pr):  # ищет n в pr
    for x in pr:
        if x == n:
            return True
    return False


def generate_pemutations(n: int, m=-1, pref=None):  # генерация n чисел в m позициях
    m = n if m == -1 else m
    pref = pref or []
    if m == 0:
        print(pref)
        return
    for i in range(1, n + 1):
        if findIn(i, pref):
            continue
        pref.append(i)
        generate_pemutations(n, m - 1, pref)
        pref.pop()


def generate(n: int, m: int, prefix=None):  # генерация n чисел m длинной
    if m == 0:
        print(prefix)
        return
    prefix = prefix or []
    for i in range(n):
        prefix.append(i)
        generate(n, m - 1, prefix)
        prefix.pop()


# generate(2, 3)
print(11111)
generate_pemutations(6, 6)
