def main():
    convert()



def convert(time = input("What time is it? ")):
    if time.find("a.m.") < 0 and time.find("p.m.") < 0:
        hour, minutes = time.split(":")
    else:
        hour, minutes = time.split(":")
        minutes = minutes.split(" ")
        if minutes[1] == "p.m." and int(hour) < 12:
            hour = int(hour) + 12
        minutes = minutes[0]
    if int(minutes) >= 60:
        return
    time = int(hour) + float(int(minutes)/60)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

if __name__ == "__main__":
    main()