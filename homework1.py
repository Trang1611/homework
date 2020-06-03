def ex1():
    numbers = input("Enter numbers: ")
    n = numbers.split()
    return (len(n), "numbers")
#print (ex1())

def ex2(a,b):
    import math
    return ("GCD is", math.gcd(a, b))
#print (ex2(a,b))
