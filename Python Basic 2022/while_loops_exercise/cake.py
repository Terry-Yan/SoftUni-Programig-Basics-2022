cake_length = int(input())
cake_width = int(input())
cake_pieces_total = cake_width * cake_length
cake_pieces_left = cake_pieces_total

while cake_pieces_left > 0:
    cake_pieces_taken = input()

    if cake_pieces_taken != 'STOP':
        cake_pieces_left -= int(cake_pieces_taken)
    elif cake_pieces_taken == 'STOP':
        break

if cake_pieces_left < 0:
    print(f"No more cake left! You need {abs(cake_pieces_left)} pieces more.")
else:
    print(f"{cake_pieces_left} pieces are left.")


