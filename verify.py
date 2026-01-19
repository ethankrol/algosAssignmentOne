def read_input():
    # read file name from stdin
    print("Enter input file name:")
    file_name = input().strip()
    input_data = []
    with open(file_name, 'r') as f:
        for line in f:
            input_data.append(line.strip().split())
    return input_data

def verify():
    # take in user input
    input_data = read_input()

    if not input_data:
        print("INVALID. Empty file.")
        return

    pair_count = int(input_data[0][0])
    preferences_matrix_a = [[-1]*pair_count for _ in range(pair_count)]
    preferences_a = input_data[1:pair_count+1]
    for i in range(pair_count):
        for j in range(pair_count):
            # i represents the person from group A
            preferences_matrix_a[i][int(preferences_a[i][j])-1] = j
    preferences_matrix_b = [[-1]*pair_count for _ in range(pair_count)]
    preferences_b = input_data[pair_count+1:2*pair_count+1]
    for i in range(pair_count):
        for j in range(pair_count):
            # i represents the person from group B
            preferences_matrix_b[i][int(preferences_b[i][j])-1] = j

    # read matching data, while verifying
    matching_data = input_data[2*pair_count+1:]
    matches_a = {}
    matches_b = {}
    for match in matching_data:
        if int(match[0]) in matches_a:
            print(f"INVALID. Person {match[0]} from group A is matched more than once. (to person {match[1]} from group B, and to person {matches_a[int(match[0])]} from group B)")
            return
        matches_a[int(match[0])] = int(match[1])
        if int(match[1]) in matches_b:
            print(f"INVALID. Person {match[1]} from group B is matched more than once. (to person {match[0]} from group A, and to person {matches_b[int(match[1])]} from group A)")
            return
        matches_b[int(match[1])] = int(match[0])
    if len(matches_a) != pair_count:
        print("INVALID. Not all people from group A are matched.")
        return
    if len(matches_b) != pair_count:
        print("INVALID. Not all people from group B are matched.")
        return
    # check for stability

    for a in range(1, pair_count+1):
        for b in range(1, pair_count+1):
            # a is the person from group a
            # b is the person from group b

            # we want to check the "happiness values" of a to b,
            # and compare it to the current matches of a and b
            
            # if the happiness value of a to b is higher than the current matches
            # then, we have an instability

            a_to_b_happiness = preferences_matrix_a[a-1][b-1]
            b_to_a_happiness = preferences_matrix_b[b-1][a-1]

            a_current_match = matches_a[a]
            b_current_match = matches_b[b]

            a_to_current_match_happiness = preferences_matrix_a[a-1][a_current_match-1]
            b_to_current_match_happiness = preferences_matrix_b[b-1][b_current_match-1]

            if a_to_b_happiness < a_to_current_match_happiness and b_to_a_happiness < b_to_current_match_happiness:
                print(f"UNSTABLE. Matching is unstable because person {a} from group A and person {b} from group B prefer each other over their current matches (person {a_current_match} from group B and person {b_current_match} from group A respectively).")
                return
    
    print("VALID STABLE MATCHING.")

verify()