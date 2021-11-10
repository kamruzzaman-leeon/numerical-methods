#gauss seidal method
n = int(input("number of variables:"))

system = []

for row in range (0,n):
    print("coefficient of equations",(row+1))
    eqn = []
    for col in range (0,n+1):
        eqn.append(float(input()))
    system.append(eqn)
print(system)

old = []
print("Initial values:")
for var in range(0,n):
    old.append(float(input()))
print(old)

true = []
print("true value:")
for var in range(0,n):
    true.append(float(input()))
print(true)

def calculateX(i):
    xi = system[i][n]
    for j in range(0,n):
        if(i != j):
            xi -= system[i][j]*old[j]
    xi /= system[i][i]
    return xi

max_itr = int(input("maximum iteration:"))
new = [None]*n
for itr in range(0,max_itr):
    print("iteration",itr+1)
    for var in range(0,n):
        new[var] = calculateX(var)
        print("x",var+1,":",new[var],end = " ")
        ea = abs((new[var] - old[var]) / new[var]) * 100
        print("ea:",ea,end=" ")
        et = abs((true[var]-new[var])/true[var]) * 100
        print("et:",et,end=" ")
        print()
        old[var] = new[var]
    print()
