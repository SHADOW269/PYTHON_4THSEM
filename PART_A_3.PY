t1=(1,2,5,7,9,2,4,6,8,10)
for i in t1:
    print(i,end=" ")
print("\n First Half")
tp1=t1[:5]
tp2=t1[5:]
print(tp1)
print("\n Second Half")
print(tp2)
li=[]
print("\n Even numbers")
for i in t1:
    if i%2==0:
        li.append(i)
t3=tuple(li)
print(t3)
print("\n Concatenation numbers")
t2=(11,13,15)
t=()
t=t1+t2
print(t)
print("\n The maxiumum value is")
print(max(t))
print("\n The miniumum value is")
print(min(t))