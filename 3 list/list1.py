






a=[3, "1", 4, 2]
for i in a:
    print(i,end=" ")
print()

print(a[-1])

a.append(5)
print(a)

a[1]=1
print(a)

b=a[2:4]
print(b)

c=a[2:]
print(c)

d=a[1:-1]
print(d)
#內容為 a 的第 1 到倒數第 2 個元素

e=a[2:-1]
print(e)
#內容為 a 的第 2 到倒數第 2 個元素

f=[]
for el in a:
    f.append(el)
f[0]=99
print(a,f,sep="\n")

g=a+[10,20]
print(g)

a[2:3]=[7,8,9]
print(a)

