from sympy import *
x,y,z=symbols('x y z')
count=0
equation=input("enter the equation for which you want find the roots :")
diff_equation=str(diff(equation))
print("newtons method formula: Xn=x-(f(x)/f'(x))")
x=1.5
equation_value=eval(equation)
diff_equation_value=eval(diff_equation)
Xn=x-(equation_value/diff_equation_value)
Xn="{0:.4f}".format(Xn)
Xn=float(Xn)
while True:
    if Xn==x:
        print(f"the solution to equation  is {Xn} ")
        break
    else:
        x=Xn
        equation_value=eval(equation)
        diff_equation_value=eval(diff_equation)
        ans=x-(equation_value/diff_equation_value)
        Xn=ans
        count=count+1
        Xn="{0:.4f}".format(Xn)
        Xn=float(Xn)
        print(f"X{count}={Xn}")
