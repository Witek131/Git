# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print('YELLLO')
    print('sfdsdgf')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


def merg(a: list, b: list):
    c = [0] * (len(a) + len(b))
    i = m = k = 0
    while m < len(a) and k < len(b):
        if a[m] <= b[k]:
            c[i] = a[m]
            i += 1
            m += 1
        else:
            c[i] = b[k]
            i += 1
            k += 1
    c = c[:i:] + a[m::] + b[k::]
    return c


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def merge_sort(a: list):
    if len(a) <= 1:
        return a
    midl = len(a) // 2
    L = a[:midl]
    R = a[midl:]
    merge_sort(L)
    merge_sort(R)
    c = merg(L, R)
    for i in range(len(c)):
        a[i] = c[i]
    return a


a = input()
s = list(map(int, input().split()))
s  = merge_sort(s)
print(*s)
