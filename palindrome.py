# We will use 123321 as the input for this solution.

x = int(input("Enter a number: "))

# Store value in a temporary variable
# as value of x will change in the while loop.
temp = x

reverse = 0

# Reverse the input to check if reversed value
# equals input value.
while(x > 0):
    remainder = x % 10
    reverse = (reverse * 10) + remainder
    x = x // 10

# x = 123321
# remainder = 1
# reverse = 0 * 10 + 1 = 1
# x = 12332

# x = 12332
# remainder = 2
# reverse = (1 * 10) + 2 = 12
# x = 1233

# Loop continues until x = 0, returning 123321 as the reversed value.

if temp == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")