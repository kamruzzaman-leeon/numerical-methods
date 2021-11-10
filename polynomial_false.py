print("initial lower bound :")
xl = float(input())
print("initial upper bound :")
xu = float(input())
print("error tolerance :")
es = float(input())
print("true value of root :")
xt = float(input())
print("maximum number of iterations allowed :")
max_itr = int(input())

d = int(input("highest degree of function : "))
coeff = []
for i in range(d + 1):
    print("coefficient no_", i+1,": ")
    coeff.append(float(input()))

def f(x):
    v = 0.0
    p = d
    for m in coeff:
        v+=int(m)*pow(x,p)
        p-=1
    return v


xr = 0.0
itr = 0
xrold =0.0
ea=None

while (itr<max_itr):
    xr = xu - (f(xu) * (xl - xu)) / (f(xl) - f(xu))
    if(itr!=0):
        ea = abs((xr - xrold) / xr) * 100
    xrold = xr
    et = abs((xt - xr) / xt) * 100
    print("Iteration ", itr+1, "xl = ", xl, "xu = ", xu, "xr = ", xr, "Ea = ", ea, "Et = ", et)
    if f(xl)*f(xr)<0 :
        xu = xr
    elif f(xl)*f(xr)>0 :
        xl = xr
    elif f(xl)*f(xr)==0 :
        break
    itr += 1
    if(ea!= None and ea<es):
        break
print("\nEstimated root is : ",xr)
