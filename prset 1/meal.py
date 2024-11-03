def main():
    in_time = input('What time is it? ').strip()
    time = convert(in_time)
    if 7 <= time and time <= 8:
        print('breakfast time')
    elif 12 <= time and time <= 13:
        print('lunch time')
    elif 18 <= time and time <= 19:
        print('dinner time')



def convert(time):
    hours, minutes = time.split(':')
    hours = float(hours) + (float(minutes)/60)
    return hours


if __name__ == "__main__":
    main()
