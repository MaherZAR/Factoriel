def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
#hello Team555nnn
def main():
    try:
        # Get user o input for the number youyouy
        num = int(input("Enter a non-negative integer: modifier par youssef"))

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
