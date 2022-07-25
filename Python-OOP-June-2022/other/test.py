def conv_hours(hours):
    conv = hours % 24
    return conv


def conv_minutes(minutes):
    conv = minutes % 60
    return conv


print(conv_hours(int(input("Enter hours"))))

print(conv_minutes(int(input("Enter minutes"))))
