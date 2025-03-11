# Prime Numbers Finder

# Get user input for the range
start_num = int(input("Enter the starting number (minimum 1): "))
end_num = int(input("Enter the ending number: "))

# Ensure start_num is at least 1 and end_num is greater than start_num
if start_num < 1:
    start_num = 1
    print("Starting number adjusted to 1 (minimum value)")

if end_num <= start_num:
    end_num = start_num + 1
    print(f"Ending number adjusted to {end_num} (must be greater than start)")

# Create range based on user input
nums = range(start_num, end_num + 1)  # +1 to include the end number

def is_prime(num):
    # Handle numbers less than 2 separately
    if num < 2:
        return False
    for x in range(2, num):
        if (num % x) == 0:
            return False
    return True

primes = list(filter(is_prime, nums))

print(f"Prime numbers between {start_num} and {end_num}:")
print(primes)