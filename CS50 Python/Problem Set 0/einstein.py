# Einstein
# Even if you haven’t studied physics (recently or ever!), you might have heard that , wherein  represents energy (measured in Joules),  represents mass (measured in kilograms), and  represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

# In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

# Hints
# Recall that input returns a str, per docs.python.org/3/library/functions.html#input.
# Recall that int can convert a str to an int, per docs.python.org/3/library/functions.html#int.
# Recall that Python comes with several built-in functions, per docs.python.org/3/library/functions.html.


def main():
    mass = int(input("Mass: "))
    convert(mass)

def convert(mass):
    c = pow(300000000, 2)
    energy = mass * c
    print(f"{energy:,} M/s")


main()