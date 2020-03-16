# Grace Keane
# BSc in Computing in Software Development
# Implementing the square root of a number using Python

def sqrt(x):

    # Calculating the square root of argument x
    # Check that x is positive

    if x < 0:
        print("Error - negative value supplied")
        return -1
    else:
        print("Working...")

    # Initial guess for the square root
    z = x / 2.0

    # Continuously improve the guess
    # Adapted from https://tour.golang.org/flowcontrol/8
    while abs(x - (z*z)) > 0.000001:
        z = z - (((z * z) - x) / (2 * z))

    return z

myVal = 63.0
print("The square root of", myVal,"is", sqrt(myVal))


