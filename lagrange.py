#lagrange
d=int(input("number of point:"))
n=int(input("polynomial order:"))
X=float(input("X:"))

x=[]

for i in range(d+1):
	print("cofficient of x_",i+1,":")
	x.append(float(input()))


y=[]
for i in range(d+1):
	print("coefficent of f(x)",i+1,":")
	y.append(float(input()))

I=[]
uper = 1
down = 1

for j in range(n):
	uper=1
	down=1
	for k in range(n):
		if(j!=k):
			uper *=(X-x[k])
			down *=(x[j]-x[k])

	I.append(float(uper/down))
print(I)

p=0.0
for h in range(0,n,1):
	p +=(y[h]*I[h])
print("result: ",p)