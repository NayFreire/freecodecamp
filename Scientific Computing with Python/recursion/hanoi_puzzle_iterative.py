NUMBER_OF_DISKS = 5
number_of_moves = 2**NUMBER_OF_DISKS - 1

rods = {
    'A': [],
    'B': [],
    'C': []
}

rods['A'] = list(range(NUMBER_OF_DISKS, 0, -1)) #list of range from 3 to 1 with -1 step -> 3, 2, 1 (0 is non-inclusive)

"""
Parameters of the move function:
- n: number of disks
- Source rod: The first rod, where all the disks are stacked on top of each other at the beginning of the game.
- Auxiliary rod (second): helps in moving the disks to the target rod.
-Target rod (third): where all the disks should be placed in order at the end of the game.
"""

def move(n, source, auxiliary, target):
    #display starting configuration
    print(rods)
    for number in range(number_of_moves):
        remainder = (number + 1) % 3
        if remainder == 1:
            if n % 2 != 0: #verifying if the number of disks is odd
                print(f'Move {number + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
            else:
                print(f'Move {number + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
        elif remainder == 2:
            if n % 2 != 0:
                print(f'Move {number + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
            else:
                print(f'Move {number + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
        elif remainder == 0:
            print(f'Move {number + 1} allowed between {auxiliary} and {target}')
            make_allowed_move(auxiliary, target)

def make_allowed_move(rod1, rod2):
    forward = False
    if not rods[rod2]: #If the rod2 rod is empty...
        forward = True #...move the disk foward
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]: #if the rod1 is not empty and the last disk on rod1 is lower than the last disk in rod2...
        forward = True #...move forward
    if forward: #if it's possible to move foward...
        print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')

        rods[rod2].append(rods[rod1].pop()) #... move last disk from rod1 and add it to rod2

    else: #if it's not possible to move foward...
        print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
        rods[rod1].append(rods[rod2].pop())#... move last disk from target and add it to rod1
    
    #display our progress
    print(rods, '\n\n')
#initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')