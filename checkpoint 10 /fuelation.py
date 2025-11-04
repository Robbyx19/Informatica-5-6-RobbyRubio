def main ():
    Fuel = input("Enter your fuel as fraction:").split ("/")
    num =int (Fuel [0])
    den =int (Fuel [1])
    percentage = round ( (num / den) * 100)
    if percentage <= 1:
        percentage = "E"
    elif percentage >= 99:
        percentage = "F"
    print (percentage)

    print (Fuel)
    
    
main ()