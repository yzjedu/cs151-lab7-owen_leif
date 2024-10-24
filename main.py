# CS151
# Programmers: Leif and Owen
# Purpose: This programs purpose is to calculate the cost of renovating a friends house floors.


def sqr_ft():  # Calculates for Square Feet of each room entered
    while True:
        width = float(input("Enter the width in feet: "))
        length = float(input("Enter the length in feet: "))
        dimension = width * length
        if width <= 0 or length <= 0:
            print("Please enter a positive integer")
        else:
            print(f"The room is {dimension} square ft")
            break
def floor_material(dimension):
    hardwood = 1.39
    tile = 4.99
    carpet = 3.99
    floor_type = input("Enter the type of floor:\n\t- Hardwood\n\t- Carpet\n\t- Tile").strip().lower()
    if floor_type == "hardwood":
        cost = hardwood * dimension
    elif floor_type == "carpet":
        cost = carpet * dimension
    elif floor_type == "tile":
        cost = tile * dimension
    else:
        print("Please enter a valid floor type")
    print(f"The floor costs ${cost}")
def room_one(cost):
    while True:
        floor_material()




