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
    
def validate_input(value):   #def the function to check input
    try:                     #try-except and ValueError to check if its type
        num=int(value)
        if num <= 0:         #check if it is positive
            print("Please enter a positive integer.")
            return 0
        else:
            return num
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return 0

#main function
while True:
    a=input("Please enter the first positive integer for A")    #input and check a
    a = validate_input(a)
    if a:
        break
while True:
    b=input("Please enter the second positive integer for B")   #input and check b
    b = validate_input(b)
    if b:
        break        

if is_coprime(a, b):                             #output
    print("A and B are coprime")
else:
    print("A and B are not coprime")


        

