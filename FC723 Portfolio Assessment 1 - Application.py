def Euclidean(a,b):     #get GCD of two number
    while a*b!=0:       #a!=0 and b!=0
        if a>b :        #ensure a is always bigger
            r=a%b       #mimic Euclidean
            a,b=b,r
        else:
            a,b=b,a     #swap a,b
    return a


#extend the Euclidean to check if two numbers are coprime

def is_coprime(a,b):    #def the function
    if Euclidean(a,b)==1:  #if gcd == 1 then yes
        return 1
    else:
        return 0

#main function

a=int(input("Please enter the first number A"))   #input
b=int(input("Please enter the second number B"))

if is_coprime(a, b):                             #output
    print("A and B are coprime")
else:
    print("A and B are not coprime")


        

