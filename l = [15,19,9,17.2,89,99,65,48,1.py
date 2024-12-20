l = [15,19,9,17.2,89,99,65,48,1.0,1,0]
def bubble_sort(l):
    n=len(l) 
    for i in range(n):
        for j in range(0,n-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return(l)

x = bubble_sort(l)
print(x)