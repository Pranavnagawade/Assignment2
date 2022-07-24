'''Q.1 Write a Python program to get a list, sorted in 
 increasing order by the last element in each tuple 
 from a given list of non-empty tuples

 Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

 Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]'''

lst=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
lst1=[]
for i in lst:
    lst1.append(i[1])
for j in range(len(lst1)):
    for k in range(j,len(lst1)):
        if lst1[j]>lst1[k]:
            lst1[j],lst1[k]=lst1[k],lst1[j]  
lst2=[]
for f in lst1:
    for r in lst:
        if f ==(r[1]):
          lst2.append(r)
print(lst2)
