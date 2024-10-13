def hoar_sort(a: list):
    if len(a) <= 1:
        return
    barer = a[-1]
    L= [] ;M= [];R= []
    for i in a:
       if i < barer:
           L.append(i)
       elif i > barer:
           R.append(i)
       else:
           M.append(i)
    hoar_sort(L)
    hoar_sort(R)
    k=0
    for i in L+M+R:
        a[k]=i; k+=1
