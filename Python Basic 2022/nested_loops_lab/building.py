floors = int(input())
rooms = int(input())

for f in range(floors, 0, -1):
    for r in range(rooms):
        if f == floors:
            print(f"L{f}{r}", end=' ')
        elif f % 2 == 0 and f != floors:
            print(f"O{f}{r}", end=' ')
        elif f % 2 != 0 and f != floors:
            print(f"A{f}{r}", end=' ')
    print()
