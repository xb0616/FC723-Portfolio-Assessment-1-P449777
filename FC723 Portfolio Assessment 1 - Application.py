a=int(input("Please enter the first number A"))
b=int(input("Please enter the second number B"))

def Euclidean(a,b):
    while a*b!=0:
        if a>b :
            r=a%b
            a,b=b,r
        else:
            a,b=b,a
    return a

a = Euclidean(a,b)
        
print(f"The GCD of A and B is {a}")
