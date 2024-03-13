NUMBER_OF_DISKS = 3
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
            print(f'Move {number + 1} allowed between {source} and {target}')
            forward = False
            if not rods[target]: #If the target rod is empty...
                forward = True #...move the disk foward
            elif rods[source] and rods[source][-1] < rods[target][-1]: #if the source is not empty and the last disk on source is lower than the last disk in target...
                forward = True #...move forward
            if forward: #if it's possible to move foward...
                print(f'Moving disk {rods[source][-1]} from {source} to {target}')

                rods[target].append(rods[source].pop()) #... move last disk from source and add it to target

            else: #if it's not possible to move foward...
                print(f'Moving disk {rods[target][-1]} from {target} to {source}')
                rods[source].append(rods[target].pop())#... move last disk from target and add it to source
            
            #display our progress
            print(rods)
        elif remainder == 2:
            print(f'Move {number + 1} allowed between {source} and {auxiliary}')
        elif remainder == 0:
            print(f'Move {number + 1} allowed between {auxiliary} and {target}')

#initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')