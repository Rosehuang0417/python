x=[1.3,5]
for i in x:
    print(i, end=" ")
print()

for i in range(len(x)):
    print(x[i],end=" ")
print()

for ix, i in enumerate(x):
    print(ix+1,i,sep=" : ")
print()

x.append(7)
print(x)

y=[2,4]
z=x+y
print(x,y,z,sep="\n")

z=x
z[0]=99
print(x,z,sep='\n')
#只記起始位置

x.append(y)
print(x)

print(len(x))
print(x[-2])#倒數

print(x)
x[2:3]=[90,91]
print(x)


