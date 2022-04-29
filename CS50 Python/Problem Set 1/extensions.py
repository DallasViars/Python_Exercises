def main():
    check_extension()

fileTypes = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

def check_extension():
    userInput = input("What is your file name? ").lower().strip()
    if userInput.find(".") < 0:
        print("application/octet-stream")
    else:
        try:
            print(fileTypes[userInput[userInput.rfind("."):]])
        except KeyError:
            print("application/octet-stream")



main()