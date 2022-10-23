cpu_price_dollars = float(input())
gpu_price_dollars = float(input())
ram_price_dollars = float(input())
ram_units = int(input())
discount_percentage = float(input())

cpu_price_leva = cpu_price_dollars * 1.57
gpu_price_leva = gpu_price_dollars * 1.57
ram_price_leva = ram_price_dollars * 1.57

total_ram_price_leva = ram_price_leva * ram_units
total_cpu_price_leva = cpu_price_leva - (cpu_price_leva * discount_percentage)
total_gpu_price_leva = gpu_price_leva - (gpu_price_leva * discount_percentage)

total_price_leva = total_cpu_price_leva + total_gpu_price_leva + total_ram_price_leva

print(f"Money needed - {total_price_leva:.2f} leva.")
