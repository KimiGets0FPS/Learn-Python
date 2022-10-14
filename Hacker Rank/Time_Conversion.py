def time_conversion(s):
    time = s.split(":")
    hour,  time_period = int(time[0]), time[2][2:]

    if time_period == "PM" and hour != 12:
        hour += 12
    if hour < 10:
        hour = "0" + str(hour)
    if time_period == "AM" and hour == 12:
        hour = "00"

    return f"{hour}:{time[1]}:{time[2][:2]}"


print(time_conversion(input()))
