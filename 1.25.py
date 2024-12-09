def count_digits(n):
    """Count the number of digits in an integer."""
    # Convert the number to a string and count the characters
    return len(str(abs(n)))  # Use abs() to handle negative numbers

"""def main():
    number = int(input("Enter an integer: "))
    digit_count = count_digits(number)
    print("The number of digits in", number, "is:", digit_count)

if __name__ == "__main__":
    main()"""

number=int(input("Enter number:"))
str1=str(number)
length=len(str1)
print("The length of the ",number," is :",length)