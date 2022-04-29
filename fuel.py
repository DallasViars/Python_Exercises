def main():
    guage()


def guage():
    print("Stuff")
    userinput = input("Fraction: ")
    if userinput.find("/") == False:
        return guage()
    if userinput.find("/") != userinput.rfind("/"):
        return guage()
    try:
        numerator, denominator = userinput.split("/")
    except ValueError:
        guage()
    if numerator.isdigit() == False or denominator.isdigit() == False:
        return guage()
    elif int(numerator) > int(denominator) or int(denominator) <= 0:
            return guage()
    percent = int(numerator) / int(denominator) * 100
    percent = round(percent)
    if int(percent) <= 1:
        print("E")
    elif int(percent) >= 99:
        print("F")
    else:
        print(f"{percent}%")



main()