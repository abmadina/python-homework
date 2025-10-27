#1
def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Example usage:
y = int(input("Enter a year: "))
print(is_leap(y))

#2
n = int(input("Enter a number: "))

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")


#3
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Ensure correct order using min() and max()
evens = list(range(min(a, b) + (min(a, b) % 2), max(a, b) + 1, 2))
print("Even numbers:", evens)
