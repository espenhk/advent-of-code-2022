from math import ceil

def priority(char):
    ord_char = ord(char)
    if ord_char >= 97: # lowercase
        res = ord_char - 96
    else:
        res = ord_char - 65 + 27
    return res


if __name__ == '__main__':

    with open("input.txt", "r") as infile:
        total_one = 0
        total_two = 0
        group = []
        for i, line in enumerate(infile):
            # PART ONE
            #print(line)
            line = line.strip()
            half_len = ceil(len(line) / 2)
            comp_one = line[:half_len]
            comp_two = line[half_len:]
            #print(comp_one, comp_two, len(comp_one), len(comp_two))

            set_one = set(comp_one)
            set_two = set(comp_two)
            #print(set_one, set_two)

            diff_set = set_one.intersection(set_two)
            #print(diff_set)

            diff_char = list(diff_set)[0]

            result = priority(diff_char)

            #print(diff_char, ord_char)

            total_one += result

            # PART TWO
            if len(group) < 3:
                group.append(line)
            else:
                # do analysis
                group_sets = [set(l) for l in group]
                print(sorted(group_sets[0]))
                print(sorted(group_sets[1]))
                print(sorted(group_sets[2]))
                group_intersect = set.intersection(group_sets[0], group_sets[1], group_sets[2])
                print(group_intersect)
                group_badge = list(group_intersect)[0]
                group_priority = priority(group_badge)
                print(group_badge, group_priority)
                total_two += group_priority

                # reset group
                group = []


        print("Answer to part one:", total_one)
        print("Answer to part two:", total_two)
