def f(s, m):
    if s >= 50: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 1, m - 1), f(s * 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)
