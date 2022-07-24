lst1=[]
lst2=[]
for i in range(97,123):
    lst1.append(chr(i))
for j in range (97,123):
    lst2.append(j)
com=dict(zip(lst1,lst2))
print(com)