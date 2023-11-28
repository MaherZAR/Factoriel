def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
#hello Team
def main():
    try:
        # Get user o input for the number000000
        num = int(input("Enter a non-negative integer: "))

        # Check if the input test is non-negative
        if num < 0:
            print("Please enter non-negative integer Thank you.")
        else:
            result = factorial(num)
            print("The factoral of {} is: {}".format(num, result))

    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")

if __name__ == "__main__":
    main()
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Rest of your existing code remains unchanged
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    try:
        # Get user input for the number
        num = int(input("Enter a non-negative integer: "))

        # Check if the input test is non-negative
        if num < 0:
            print("Please enter a non-negative integer. Thank you.")
        else:
            result = factorial(num)
            print("The factorial of {} is: {}".format(num, result))
            
            # Call the new function to calculate the sum of digits
            digit_sum = sum_of_digits(result)
            print("The sum of digits in the factorial is:", digit_sum)

    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")

if __name__ == "__main__":
    main()
