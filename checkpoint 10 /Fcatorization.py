def divide (a,b):
    if b == 0:
        raise ValueError(" Hey! You cannot divide by zero.")
    return a / b 
print (divide (1,2))
print (divide (2,0))
       