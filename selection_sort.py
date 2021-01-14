def selection_sort(mylist):
    for i in range(len(mylist)-1):
        k=i
        for j in range(i+1,len(mylist)):
            if(mylist[j]<mylist[k]):
                k=j
        if(k!=i):
            temp=mylist[i]
            mylist[i]=mylist[k]
            mylist[k]=temp

mylist = [12,34,2,7,45,90,89,9,1]
print('element before sorting')
print(mylist)
selection_sort(mylist)
print('element after sorting')
print(mylist)
