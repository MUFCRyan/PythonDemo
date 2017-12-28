#coding=utf-8
I=input('Enter the profit:') #输入的是 str
I=int(I) #转换成 int
m=[100000, 600000, 400000, 200000, 100000, 0]
r=[0.01, 0.015, 0.03, 0.05, 0.075, 0.1]

sum=0

for x in range(0,6):
    if I>m[x]:
        sum+=(I-m[x]*r[x])
        I=m[x]
print(sum)

