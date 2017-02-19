'''
Collatz Conjecture - Start with a number n > 1.
Find the number of steps it takes to reach one using the following process:
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
'''


def Collatz(number, i=1):
    "collatz number calculation"
    if (number <= 1):
        return i
    if ((number % 2) == 0):
        return Collatz(number / 2 , i + 1)
    else:
        return Collatz(number * 3 + 1, i + 1)

print("Collatz Number for {0!s} is {1!s}".format(3, Collatz(3)))
print("Collatz Number for {0!s} is {1!s}".format(4, Collatz(4)))
print("Collatz Number for {0!s} is {1!s}".format(5, Collatz(5)))
print("Collatz Number for {0!s} is {1!s}".format(6, Collatz(6)))