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

