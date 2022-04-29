def main():
    convert(input("What would you like to say? "))


def convert(string):
    string = string.replace(":)", "🙂").replace(":(", "🙁")
    print(string)

main()