from multiprocessing.managers import ListProxy
# Сортировка слиянием

def merg(a: list,b: list):
    c=[0]*(len(a)+len(b))
    i=m=k=0
    while m<len(a) and k<len(b):
        if a[m]<=b[k]:
            c[i]=a[m]
            i+=1
            m+=1
        else:
            c[i]=b[k]
            i += 1
            k += 1
    c=c[:i:]+a[m::]+b[k::]
    return c
#print(merg([1,6,8,9], [6,9,71]))
def merge_sort(a: list):
    if len (a) <=1:
        return
    midl=len(a)//2
    L =a[:midl]
    R=a[midl:]
    merge_sort(L)
    merge_sort(R)
    c=merg(L,R)
    for i in range(len(c)):
        a[i] = c[i]
    print(a)
merge_sort([7 ,2,5,3,4])
