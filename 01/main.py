if __name__ == '__main__':
    with open("input.txt") as infile:
        cals_per_elf = []
        curr_cals = 0
        idx = 0
        for line in infile:
            if line == '\n':
                cals_per_elf.append(curr_cals)
                curr_cals = 0
                idx += 1
            else:
                cals = int(line)
                curr_cals += cals
    cals_idx = [(i, val) for (i, val) in enumerate(cals_per_elf)]

    cals_idx_sorted = sorted(cals_idx, key=lambda t:t[1])
    max_one_idx, max_one_val = cals_idx_sorted[-1]
    max_two_idx, max_two_val = cals_idx_sorted[-2]
    max_three_idx, max_three_val = cals_idx_sorted[-3]
    max_three_total = max_one_val + max_two_val + max_three_val
    print("Top elf in terms of calories is individual %d, with %d calories"
             % (max_one_idx, max_one_val))
    max_three = cals_idx_sorted[-1][1] + cals_idx_sorted[-2][1] + cals_idx_sorted[-3][1]
    print("Top three in terms of calories are individuals %d, %d, %d, with %d calories total" % (max_one_idx, max_two_idx, max_three_idx, max_three_total))
