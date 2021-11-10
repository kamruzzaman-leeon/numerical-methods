X0=float(input())
Xt=float(input())
Es=float(input())
max_itr=int(input())

def f(x):
	return 2*x*x*x - 11.7*x*x + 17.7*x - 5

def df(x):
	return 6*x*x - 23.4*x + 17.7

Xa=X0

itr=0
while (itr<max_itr):
	Xr=Xa-(f(Xa)/df(Xa))
	itr+=1
	Et= float(abs((Xt-Xr)/Xt)*100 )

	Ea= float(abs((Xr-Xa)/Xr)*100 )
	Xa=Xr
	print ("Iteration:", itr,", X",itr,"= ",Xr,", Ea= ",Ea,"%, Et= ",Et,"%")

	if Ea<Es:
		break

print ("Estimated root is:",Xr)
