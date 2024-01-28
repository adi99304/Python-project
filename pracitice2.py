#update the middle element of the list with a value and delete a middle element
l=list()
n=int(input("no. of elements in the list: "))
for i in range(0,n):
    j=int(input("Enter the element: "))
    l.append(j)
print(l)
if len(l)%2==0:
    midindex1=len(l)//2-1
    midindex2=len(l)//2
    l[midindex1]=34
    l[midindex2]=45
    print(l)
else :
    midindex3=len(l)//2
    print(midindex3)
        