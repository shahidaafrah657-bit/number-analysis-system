# Number Analysis System

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Input numbers
nums = list(map(int, input("Enter numbers separated by space: ").split()))

even = []
odd = []
prime = []

for num in nums:
    # Even or Odd
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

    # Prime check
    if is_prime(num):
        prime.append(num)

# Calculations
total = sum(nums)
average = total / len(nums)

# Output
print("\n--- Number Analysis System ---")
print("Numbers:", nums)
print("Even Numbers:", even)
print("Odd Numbers:", odd)
print("Prime Numbers:", prime)
print("Sum:", total)
print("Average:", average)