from stack import Stack

print("\nLet's play Towers of Hanoi!")


# Creating the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# Setting up the game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
    num_disks = int(input("\nEnter a number greater than or equal to 3\n"))

for i in range(num_disks, 0, -1):
    left_stack.push(i)
    
num_optimal_moves = (2**num_disks) - 1
print("\nThe fastest you can solve this game is in {x} moves!\n".format(x=num_optimal_moves))
