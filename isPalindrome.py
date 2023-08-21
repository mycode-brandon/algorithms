def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    number = x                                              # constant copy of x
    reversed_number = 0                                     # start at zero for reverse
    while x > 0:                                            # until x is below 10 b/c x//10=0 for x < 10
        remainder = x % 10                                  # grab the last digit of x
        x = x // 10                                         # grab the other digits
        reversed_number = reversed_number * 10 + remainder  # first round, reversed_number=0
        # First round:  remainder=2, x=244, reversed_number=2
        # Second round: remainder=4, x=24, reversed_number=24
        # Third round:  remainder=4, x=2, reversed_number=244
        # Fourth round: remainder=2, x=0, reversed_number=2442
    return reversed_number == number

# Pythonic Method
# def isPalindrome(x: int) -> bool:
#     if str(x) == str(x)[::-1]:
#         return True
#     else:
#         return False

assert isPalindrome(121) == True
assert isPalindrome(112) == False
assert isPalindrome(21112) == True
assert isPalindrome(2442) == True
assert isPalindrome(0) == True
assert isPalindrome(100) == False
assert isPalindrome(-777) == False
