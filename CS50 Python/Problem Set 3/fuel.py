# Fuel Gauge
# fuel gauge
# Source: amazon.com/dp/B09C4FL56G
# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, less than 1% remains, output E instead to indicate that the tank is empty. And if more than 99% remains, output F instead to indicate that the tank is full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

# Hints
# Note that you can handle two exceptions separately with code like:

# try:
#     ...
# except ValueError:
#     ...
# except ZeroDivisionError:
#     ...
# Or you can handle two exceptions together with code like:

# try:
#     ...
# except (ValueError, ZeroDivisionError):
#     ...


def main():
    guage()


def guage():
    userinput = input("Fraction: ")

    #This checks for expected format of ##/##
    if userinput.find("/") == False:
        return guage()

    #This makes sure user isn't inputting multiple forward slashes
    if userinput.find("/") != userinput.rfind("/"):
        return guage()

    #This tries to assign the value before the split to numerator and the value after the split to the denominator
    try:
        numerator, denominator = userinput.split("/")
    except ValueError:
        guage()
    
    #This ensures the numerator and denominator are numbers
    if numerator.isdigit() == False or denominator.isdigit() == False:
        return guage()

    #This ensures the numerator is always larger than the denominator and that the denominator isn't 0 or less
    elif int(numerator) > int(denominator) or int(denominator) <= 0:
            return guage()

    #The below section just gets the percentage and sets the output formatting
    percent = int(numerator) / int(denominator) * 100
    percent = round(percent)
    if int(percent) <= 1:
        print("E")
    elif int(percent) >= 99:
        print("F")
    else:
        print(f"{percent}%")



main()