def main():
    mass = int(input("Mass: "))
    convert(mass)

def convert(mass):
    c = pow(300000000, 2)
    energy = mass * c
    print(f"{energy:,} M/s")


main()