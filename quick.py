def pivot(listx,first,last):
    pivot=listx[first]
    left=first+1
    right=last
    while True:
        while left<=right and listx[left]<=pivot:
            left+=1
        while left<=right and listx[right]>=pivot:
            right-=1
        if left>right:
            break
        else:
            listx[left],listx[right]=listx[right],listx[left]
    listx[first],listx[right]=listx[right],listx[first]
    return right

def Quick(listx,first,last):
    if first<last:
        P=pivot(listx,first,last)
        Quick(listx,first,P-1)
        Quick(listx,P+1,last)
        
L=[5,7,3,5,89,3,78,3]
Quick(L,0,len(L)-1)
print(L)