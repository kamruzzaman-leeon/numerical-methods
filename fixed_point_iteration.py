import math
def f(x):
    return round(math.exp(-x),5)

itr_max = int(input("maximum iteration value: "))
es = float(input("approximate error: "))
xt = float(input("true value : "))
itr = 0
xr = 0
ea = None
while(itr<itr_max):
    if (xr != 0 ):
        ea = round(abs((xr - xrold) / xr) * 100.0,3)
    xrold = xr
    et = round(abs((xt-xrold)/xt)*100.0,3)
    if (ea != None and ea < es):
        break
    print("iteration: ", itr, "xi :", xr, "ea(%) : ",ea,"et(%)",et)
    itr += 1

    xr = f(xrold)


print("estimated root is",xrold)