print("Hello world")
#To write a program to seperate even and odd no.s from a list
l=list()
n=int(input("no. of elements in the list: "))
for i in range(0,n):
    j=int(input("Enter the element: "))
    l.append(j)
print(l)
for i in range(n):
    if l[i]%2==0:
        print("evenno.: "+str(l[i]))
    else:
        print("odd no.: "+str(l[i]))    