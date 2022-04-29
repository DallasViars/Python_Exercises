def main():
    strip()


vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def strip():
    tweet = []
    result = []
    tweet[:] = input("Input: ")
    for i in tweet:
        if i not in vowels:
            result.append(i)
    result = "".join(result)
    print(result)


main()