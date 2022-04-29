def main():
    deep()


def deep():
    guess = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
    if guess == "42" or guess == "forty-two" or guess == "forty two":
        print("Yes")
    else:
        print("No")


main()