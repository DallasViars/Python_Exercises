def main():
    interpret()



def interpret():
    x, y, z = input("What is your math expression? ").split(" ")
    if y == "*":
        answer = round(float(x) * float(z), 1)
    elif y == "/":
        answer = round(float(x) / float(z), 1)
    elif y == "+":
        answer = round(float(x) + float(z), 1)
    elif y == "-":
        answer = round(float(x) - float(z), 1)
    print(answer)


main()