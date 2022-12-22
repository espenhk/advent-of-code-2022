def find_start(input_str, len_candidate):

    result_idx = 0
    start_offset = len_candidate-1
    for i, char in enumerate(input_str):
        if i < start_offset:
            continue

        candidate = input_str[i-start_offset:i+1]
        cand_set = set(candidate)

        if len(candidate) == len(cand_set):
            print(candidate, len(cand_set))
            result_idx = i+1
            break

    return result_idx

if __name__ == '__main__':
    with open("input.txt", "r") as infile:
        input_str = infile.readline().strip()
    #print(input_str)

    result_one = find_start(input_str, 4)
    result_two = find_start(input_str, 14)

    print("Answer to part one:", result_one)
    print("Answer to part two:", result_two)
