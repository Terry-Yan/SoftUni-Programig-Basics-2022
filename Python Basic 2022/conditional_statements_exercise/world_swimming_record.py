from math import floor

current_record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_per_meter = float(input())

water_resistance = 12.5

total_time_for_swimming = distance_in_meters * seconds_per_meter
time_for_water_resistance = floor((distance_in_meters / 15)) * 12.5
personal_time = total_time_for_swimming + time_for_water_resistance

if current_record_in_seconds <= personal_time:
    time_to_spare = abs(current_record_in_seconds - personal_time)
    print(f'No, he failed! He was {time_to_spare:.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {personal_time:.2f} seconds.')
