def find_ball(swaps,position):
    for i in swaps:
        if i[0] == position:
            position = i[1]
        elif i[1] == position:
            position = i[0]
    return position


def get_pos(swaps, curr_pos):
    for i in swaps:
        if curr_pos in i:
            curr_pos = i.replace(curr_pos,'')
    return curr_pos

swaps = ['AB','CA','CA']
curr_pos = 'B'

print(get_pos(swaps, curr_pos))

# no_of_swaps = int(input("Enter no of swaps: "))
# for i in range(no_of_swaps):
#     swap = input(f"Enter swap {i+1}: ")
#     swaps.append(swap)
# initial_pos_of_ball = input("Enter initial position: ")
# print(find_ball(swaps,initial_pos_of_ball))