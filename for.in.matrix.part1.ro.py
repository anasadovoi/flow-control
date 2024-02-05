print("\n")

for y in range(1, 11):
    for x in range(1, 11):
        if x in(1,10) or y in (1,10):
            print("#", end=" ")
        else:
            print(".", end=" ")
    print()

print("\n")