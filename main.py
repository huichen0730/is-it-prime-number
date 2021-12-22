# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.

def prime_checker(number):
    is_prime = True
    if number == 0 or number == 1:
        is_prime = False
    for n in range (2, number):
        if number % n == 0:
            is_prime = False

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")            

n = int(input("Check this number: "))
prime_checker(number=n)
