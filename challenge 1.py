def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    while True:
        num = input("Enter a positive integer (or 'q' to quit): ")
        if num == 'q':
            break

        try:
            num = int(num)
            if num >= 0:
                print(f"The factorial of {num} is {factorial(num)}")
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()