from lib import *

def execute_instruction(stacks, move_num, from_idx, to_idx):

    # split off from origin stack
    #print("from before: %s" % stacks[from_idx])
    stacks[from_idx], popped = stacks[from_idx][:-move_num], stacks[from_idx][-move_num:]
    #print("popped: %s" % popped)
    #print("from after: %s" % stacks[from_idx])

    # join into destination stack
    #print("to before: %s" % stacks[to_idx])
    stacks[to_idx].extend(popped)
    #print("to after: %s" % stacks[to_idx])
    #print()

    return stacks


if __name__ == '__main__':
    total_one = 0
    total_two = 0

    with open("input.txt", "r") as infile:
        # input stacks
        input_stacks = []
        for i in range(9):
            input_stacks.append(infile.readline())
        stacks = read_start_stack(input_stacks)
        #print(stacks)

        # blank line
        infile.readline()

        # instructions
        for i, line in enumerate(infile):
            line = line.strip()
            move_num, from_idx, to_idx = read_instruction(line)
            print(line)
            stacks = execute_instruction(stacks, move_num, from_idx, to_idx)
            print(stacks)

        # read result
        result = []
        for i in range(1, 10):
            result.append(stacks[i][-1])
        result = "".join(result)

    print("Answer to part two:", result)
