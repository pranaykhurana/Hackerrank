import calendar

if __name__ == '__main__':
    date = input().split(" ")
    day = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))
    day_name_list = list(calendar.day_name)
    print(day_name_list[day].upper())