x=[5,8,4,6,6,2,15,23]
Smax=0
for i in range(len(x)):
    a=x[i]
    for j in range(i+1,len(x)):
        b=x[j]
        for k in range(j+1,len(x)):
            c=x[k]
            if a+b>c and a+c>b and c+b>a:
                p=(a+b+c)/2
                S= (p*(p-a)*(p-b)*(p-c))**0.5
                if S>Smax:
                    Smax=S
print(Smax)
