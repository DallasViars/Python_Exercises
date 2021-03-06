# Just setting up my twttr

# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

# Hints
# Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
# Much like a list, a str is “iterable,” which means you can iterate over each of its characters in a loop. For instance, if s is a str, you could print each of its characters, one at a time, with code like:
# for c in s:
#     print(c, end="")


def main():
    strip()


vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def strip():
    tweet = []
    result = []
    tweet[:] = input("Input: ")

    #Loops through each letter in the Tweet
    for i in tweet:

        #If the letter is not in the vowels list it is added to the end of the result list
        if i not in vowels:
            result.append(i)

    #When the loop is done result is converted from a list to a string
    result = "".join(result)
    print(result)


main()