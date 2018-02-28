def print_move(origin, destination):
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    assert 1 <= start <= 3 and 1 <= end <= 3, "Bad starting/destination rod"
    assert start != end, "Destination rod must be different from starting rod."
    assert n > 0, 'Number of disks must be positive'
    intermediate = 1 + 2 + 3 - start - end
    if n == 1:
        print_move(start, end)
    else:
        move_stack(n-1, start, intermediate)
        print_move(start, end)
        move_stack(n-1, intermediate, end)

disks = int(input('How many disks to transfer?: '))
starting_rod = int(input('Starting rod (1/2/3): '))
destination_rod = int(input('Destination rod (1/2/3): '))
move_stack(disks, starting_rod, destination_rod)
