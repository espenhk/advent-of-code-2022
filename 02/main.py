def determine_game(str_a, str_b):
    choice_a = None
    choice_b = None
    result = None

    if str_b == "X":
        str_b = "A"
    elif str_b == "Y":
        str_b = "B"
    elif str_b == "Z":
        str_b = "C"


    if str_a == "A":
        choice_a = 'rock'
    elif str_a == "B":
        choice_a = 'paper'
    elif str_a == "C":
        choice_a = 'scissors'

    if str_b == "A":
        choice_b = 'rock'
    elif str_b == "B":
        choice_b = 'paper'
    elif str_b == "C":
        choice_b = 'scissors'
    
    # tie
    if choice_a == choice_b:
        result = "draw"
    # A chooses rock
    if choice_a == 'rock':
        if choice_b == 'paper':
            result = "B"
        if choice_b == 'scissors':
            result = "A"
    # A chooses paper
    elif choice_a == 'paper':
        if choice_b == 'rock':
            result = "A"
        if choice_b == 'scissors':
            result = 'B'
    # A chooses scissors
    elif choice_a == 'scissors':
        if choice_b == 'rock':
            result = "B"
        if choice_b == 'paper':
            result = "A"

    return result, choice_a, choice_b

def calculate_score(my_choice, result):
    scores_result = {'B': 6, 'draw': 3, 'A': 0}
    scores_choice = {'rock': 1, 'paper': 2, 'scissors': 3}

    result_score = scores_result[result]
    choice_score = scores_choice[my_choice]

    final_score = choice_score + result_score
    return final_score


if __name__ == "__main__":
    draw_score = 0
    total_score_one = 0

    with open("input.txt") as infile:
        for line in infile:
            # == PART ONE SECTION == 
            your_choice, my_choice = line.strip().split(" ")

            res, your_choice, my_choice = determine_game(your_choice, my_choice)
            score = calculate_score(my_choice, res)
            total_score_one += score

            # == PART TWO SECTION ==
            your_choice_two, desired_res = line.strip().split(" ")

    print("Final score, part 1 method: ", total_score_one)
