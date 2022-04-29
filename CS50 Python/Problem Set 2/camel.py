def main():
    camel()


def camel():
    variableName = input("What is your variable name? ")
    snake_case = ""
    for i in variableName:
        if i.isupper():
            snake_case = snake_case + "_" + i.lower()
        else:
            snake_case = snake_case + i
    print(snake_case)


main()