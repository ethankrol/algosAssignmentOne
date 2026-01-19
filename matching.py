def read_input(file_path = ''): 
    # Example file_path is inputs/example1.in
    if file_path == '':
        file_path = input("Enter your file path: ")
    print(f'Reading in input from {file_path}')

    # Try and except block to catch I/O error
    try:
        with open(file_path, 'r') as f:
            print('File opened successfully')
    except:
        print('Error opening file. Make sure this file exists and the file path is correct.')
        return
    
    with open(file_path, 'r') as f:
        n_lines = f.readline().strip()
        if not n_lines.isdigit():
            print("Error: First line in input file is not a number. Must specify n lines first.")

        n_lines = int(n_lines)
        
        # Create array for first group. Since we are using 1-indexing, we can add an empty row to correct our indexing.
        first_group = [[0] * n_lines]
        for _ in range(n_lines):
            row = f.readline()

            # Here, we reverse the order of the preferences
            # This is so that we can pop the highest preference in the list in constant time later on.
            # If we pop any element that isn't at the end of the list, the operation is linear, not constant.
            first_group.append(list(map(int, row.strip().split(' ')[::-1])))
        
        # Create array for second group
        second_group = [[0 for _ in range(n_lines + 1)] for _ in range(n_lines + 1)]
        for i in range(n_lines):
            row = f.readline()

            # No need to reverse this one as it is just used for comparisons
            temp = list(map(int, row.strip().split(' ')))
            # This array will be built as a comparison array.
            for j in range(len(temp)):
                second_group[i+1][j+1] = temp[j]
        
        return first_group, second_group

def write_output(file_path, pairings):
    if file_path == '':
        return
    with open(file_path, 'w') as f:
        for i in range(1, len(pairings)):
            row = f'{i} {pairings[i]}'
            if i != len(pairings) - 1:
                row += '\n'
            f.write(row)
            

def match(input_file_path = '', output_file_path = ''):
    first_prefs, second_prefs = read_input(input_file_path)   
    if output_file_path == '':
        output_file_path = input("Provide a file path to write the output to: ")
    # Create empty matchings
    first_matchings = [0] * len(first_prefs)
    second_matchings = [0] * len(second_prefs)
    (first_matchings, second_matchings)

    free = list(range(1,len(first_prefs)))
    while free:
        # Choose last student, ordering doesn't matter
        h = free[-1]
        a = first_prefs[h].pop()
        h_cur = second_matchings[a]
        if h_cur == 0:
            first_matchings[h] = a
            second_matchings[a] = h
            free.pop()
        else:
            if second_prefs[a][h] < second_prefs[a][h_cur]:
                first_matchings[h] = a
                second_matchings[a] = h
                free.pop()
                free.append(h_cur)

            else:
                continue
    
    write_output(output_file_path, first_matchings)


match("inputs/example1.in", "outputs/example2.out")