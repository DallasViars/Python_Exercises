def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    check_plate = []
    check_plate[:] = plate
    if len(plate) < 2 or len(plate) > 6 or plate.isalnum() == False:
        return False
    if plate[0:].isalpha():
        return True
    i = 2
    first_num = 0
    while i < len(plate):
        if first_num == 0:
            if plate[i].isdigit() and int(plate[i]) == 0:
                return False
            else:
                first_num = 1
        elif plate[i].isdigit() and plate[i:].isdigit() == False:
            return False
        i += 1
    return True




main()