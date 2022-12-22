def read_start_stack(stack_lines):
    # print(stack_lines)
    stacks = {i: [] for i in range(1, 10)}

    # read from bottom up
    stack_lines.reverse()

    for line in stack_lines[1:]:
        # print(line)
        idx = 0
        for j, char in enumerate(line):
            # print(j, char, idx)
            # new stack
            if j % 4 == 0:
                idx += 1
            # element in stack
            elif j % 4 == 1:
                if char != ' ':
                    stacks[idx].append(char)

    return stacks


def read_instruction(instruction):
    instruction = instruction.split()
    move_num = int(instruction[1])
    from_idx = int(instruction[3])
    to_idx = int(instruction[5])
    # print(move_num, from_idx, to_idx)
    return move_num, from_idx, to_idx


def execute_instruction(stacks, move_num, from_idx, to_idx):
    remaining = move_num
    for i in range(remaining):
        # split off from origin stack
        # print("from before: %s" % stacks[from_idx])
        stacks[from_idx], popped = stacks[from_idx][:-1], stacks[from_idx][-1]
        # print("popped: %s" % popped)
        # print("from after: %s" % stacks[from_idx])

        # join into destination stack
        # print("to before: %s" % stacks[to_idx])
        stacks[to_idx].append(popped)
        # print("to after: %s" % stacks[to_idx])
        # print()
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
            # print(line)
            stacks = execute_instruction(stacks, move_num, from_idx, to_idx)
            # print(stacks)

        # read result
        result_one = []
        for i in range(1, 10):
            result_one.append(stacks[i][-1])
        result_one = "".join(result_one)

    print("Answer to part one:", result_one)
