hours = 0
minutes = 0

while hours < 24:
    if minutes == 60:
        minutes = 0

    while minutes < 60:
        # if hours < 10:
        #     if minutes < 10:
        #         print(f"0{hours}:0{minutes}")
        #     else:
        #         print(f"0{hours}:{minutes}")
        # else:
        #     if minutes < 10:
        #         print(f"{hours}:0{minutes}")
        #     else:
        #         print(f"{hours}:{minutes}")
        print(f"{hours}:{minutes}")
        minutes += 1
    hours += 1
