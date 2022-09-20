length_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
percentage_of_occupancy = float(input())/100

volume_in_cm = length_in_cm * width_in_cm * height_in_cm
volume_in_liters = volume_in_cm * 0.001
volume_total = volume_in_liters * (1 - percentage_of_occupancy)

print(volume_total)
