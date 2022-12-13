
if __name__ == '__main__':

    with open("input.txt", "r") as infile:
        total_one = 0
        for line in infile:
            pair_a, pair_b = line.split(",")
            pair_a_min, pair_a_max = pair_a.split("-")
            pair_b_min, pair_b_max = pair_b.split("-")
            pair_a_min = int(pair_a_min)
            pair_a_max = int(pair_a_max)
            pair_b_min = int(pair_b_min)
            pair_b_max = int(pair_b_max)

            #print(pair_a, pair_b)
            #print(pair_a_min, pair_a_max, pair_b_min, pair_b_max)

            # check B contained in A
            if (pair_b_min >= pair_a_min) and (pair_b_max <= pair_a_max):
                total_one += 1
                print(line, total_one)
            elif (pair_a_min >= pair_b_min) and (pair_a_max <= pair_b_max):
                total_one += 1
                print(line, total_one)

        print("Answer to part one: ", total_one)