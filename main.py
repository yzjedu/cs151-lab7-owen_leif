# CS151
# Programmers: Leif and Owen
# Purpose: This programs purpose is to calculate the cost of renovating a friends house floors.

def room_sizing():
    global house_size
    room_count = 1
    while room_count <= 5:
        room_length = ''
        room_width = ''
        while not room_length.isdigit():
            room_length = input('Please input the length of the room expressed in whole digits: ')
            if not room_length.isdigit():
                print('This is an invalid input. Please input a valid positive whole number\n')
        room_length = int(room_length)
        while not room_width.isdigit():
            room_width = input('Please input the width of the room expressed in whole digits: ')
            if not room_width.isdigit():
                print('This is an invalid input. Please input a valid positive whole number\n')
        room_width = int(room_width)
        room_size = room_length * room_width
        if room_count == 1:
            print(f'The first room is {room_size} square units large\n')
        elif room_count == 2:
            print(f'The second room is {room_size} square units large\n')
        elif room_count == 3:
            print(f'The third room is {room_size} square units large\n')
        elif room_count == 4:
            print(f'The fourth room is {room_size} square units large\n')
        elif room_count == 5:
            print(f'The fifth room is {room_size} square units large')
        house_size = house_size + room_size
        if room_count == 5:
            print(f'In total, the house is {house_size} square units large')
        room_count = room_count + 1

def cost_calculation():
    global house_size
    passthru = False
    minor_passthru1 = False
    minor_passthru2 = False
    while not passthru:
        while not minor_passthru1:
            floor_type = input('\nWould you like to test a hardwood, carpet, or tile floor?\nPlease express your answer in the form of the first letter: ')
            if floor_type.lower() == "h":
                cost_per_square = 1.39
                total_flooring_cost = house_size * cost_per_square
                print(f'Hardwood costs {cost_per_square} per square unit\nThe cost of hardwood flooring for this house is {total_flooring_cost:.2f}$\n')
                minor_passthru1 = True
            elif floor_type.lower() == "c":
                cost_per_square = 3.99
                total_flooring_cost = house_size * cost_per_square
                print(f'Carpet costs {cost_per_square} per square unit\nThe cost of carpet flooring for this house is {total_flooring_cost:.2f}$\n')
                minor_passthru1 = True
            elif floor_type.lower() == "t":
                cost_per_square = 4.99
                total_flooring_cost = house_size * cost_per_square
                print(f'Tile costs {cost_per_square} per square unit\nThe cost of tile flooring for this house is {total_flooring_cost:.2f}$\n')
                minor_passthru1 = True
            else:
                print('This is an invalid input. Please try again\nRemember to express you answer in the form of the first letter (h, c, t)')
        while not minor_passthru2:
            test_new_price_query = input('Would you like to test the price with a different floor type?\nExpress your answer as Y or N: ')
            if test_new_price_query.lower() == 'n':
                print('Thank you for using our calculator!')
                passthru = True
                minor_passthru2 = True
            elif test_new_price_query.lower() == 'y':
                minor_passthru2 = True
            else:
                print('This is an invalid input. Please express your answer as Y or N\n')

house_size = 0
room_sizing()
cost_calculation()



