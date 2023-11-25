import random
import math

def determine_prime(a, b): # Determine if a and b are rel. prime; GCD = 1
    return math.gcd(a, b) == 1

def solution(a, b): # Find a solution to the equation where int are rel. prime
    if determine_prime(a, b): # See if prime 
        for x in range(1, b): # Iterate through possible x values
            if (a * x) % b == 1:
                y = (1 - a * x) // b  # Calculate 'y' based on the equation ax + by = 1
                print(f"{a}x + {b}y = 1, with x = {x} and y = {y}\n")
                return
    else:
        gcd = math.gcd(a, b) # Calculate the GCD
        print(f"{a} and {b} are not relatively prime. GCD({a}, {b}) = {gcd}\n")

for _ in range(20): # Generate 20 random pairs of 'a' and 'b' and find solutions.
    a = random.randint(1, 9999)
    b = random.randint(1, 9999)
    solution(a, b)