def main():
    length = int(input("Enter the length of the list: "))
    numbers = []
    for i in range(length):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)
    
  
    with open("largest.txt", "w") as f:
        for num in numbers:
            f.write(f"{num}\n")
    

    largest = max(numbers)
    print(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
