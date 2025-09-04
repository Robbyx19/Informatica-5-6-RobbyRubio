def vending_machine(price, total_paid):
    while price > 0:
        print(f"Amount due: {price}")
        try:
            pay = int(input("Insert coin: "))
            if pay == 25 or pay == 10 or pay == 5:
                price -= pay
                total_paid += pay
            else:
                print("Not a valid coin.")
        except ValueError:
            print("Please insert a valid number.")
    
    print("Thanks! Here's your coke.")
    if total_paid > 50:
        print(f"Here is your change: {total_paid - 50}")

def main():
    price = 50
    total_paid = 0
    vending_machine(price, total_paid)

main()
