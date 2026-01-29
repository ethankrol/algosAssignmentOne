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
        
        # Make sure file is not empty
        if f.read(1):
            f.seek(0)
        else:
            print('File is empty. Please provide a valid input file.')
            return
        
        # First line in file should be the number of lines.
        n_lines = f.readline().strip()
        if not n_lines.isdigit():
            print("Error: First line in input file is not a number. Must specify n lines first.")
            return
        
        n_lines = int(n_lines)
        total_rows = n_lines * 2 + 1
        
        # Create an empty array for first group of preferences. 
        # Since we are using 1-indexing (preferences can only be permutations of 1...n), we can add an empty row to correct our indexing.
        first_group = [[0] * n_lines]
        for i in range(n_lines):
            row = f.readline()

            if not row:
                print(f'Invalid input file. File terminates at row {i+1} (0-indexed). File must contain a total of {total_rows} rows, including the first row.')
                return

            # Here, we reverse the order of the preferences so that the most preferred pairings are at the end of the list.
            # This is so that we can pop the highest preference in the list in constant time later on.
            # If we pop any element that isn't at the end of the list, the operation is linear, not constant.
            row_stripped = row.strip().split()[::-1]

            # Check if each item in the row is numeric
            for item in row_stripped:
                if not item.isdigit():
                    print(f'Invalid input file. Item {item} in row {i+1} (0-indexed) is not a number.')
                    return

            # Check if the row is length n
            if len(row_stripped) != n_lines:
                print(f'Invalid input file. There are {len(row_stripped)} items in row {i+1} (0-indexed) of input file. This is not the expected row length of n = {n_lines}.')
                return 
            
            row_list = list(map(int, row_stripped))

            # Check if there is exclusively one instance of each number in the group's preference list, or if a number is out of range.
            duplicates = set()
            for item in row_list:
                if item in duplicates:
                    print(f'Invalid input file. Number {item} is repeated in row {i+1} (0-indexed). Each number in each row must be unique.')
                    return
                if item < 0 or item > n_lines:
                    print(f'Invalid input file. Number {item} in row {i+1} is outside of the range 1...{n_lines}.')
                    return
                
                duplicates.add(item)
            
            first_group.append(row_list)
        
        # Create array for second group of preferences.
        second_group = [[0 for _ in range(n_lines + 1)] for _ in range(n_lines + 1)]
        for i in range(n_lines):
            row = f.readline()
            if not row:
                print(f'Invalid input file. File terminates at row {n_lines+i+1} (0-indexed). File must contain a total of {total_rows} rows, including the first row.')
                return

            row_stripped = row.strip().split()[::-1]

            # Check if each item in the row is numeric
            for item in row_stripped:
                if not item.isdigit():
                    print(f'Invalid input file. Item {item} in row {n_lines+i+1} (0-indexed) is not a number.')
                    return
            
            # Check if the length of the parsed list is correct.
            if len(row_stripped) != n_lines:
                print(f'Invalid input file. There are {len(temp)} items in row {n_lines+i+1} (0-indexed) of input file. This is more than expected row items {n_lines}.')
                return 

            # No need to reverse this one as it is just used for comparison lookups.
            temp = list(map(int, row_stripped))

            # Check if there is exclusively one instance of each number in the group's preference list, or if a number is out of range.
            duplicates = set()
            for item in temp:
                if item in duplicates:
                    print(f'Invalid input file. Number {item} is repeated in row {n_lines+i+1} (0-indexed). Each number in each row must be unique.')
                    return
                if item < 0 or item > n_lines:
                    print(f'Invalid input file. Number {item} in row {n_lines+i+1} (0-indexed) is outside of the range 1...{n_lines}.')
                    return
                
                duplicates.add(item)

            # This array will be built as a comparison array.
            # second_group[x][y] will correspond to the rank (preference) that x prefers y.
            # For example, if applicant 1 has a preference list of 2 1 3, second_group[1][2] = 1, as hospital 2 is the applicant's first preference.
            # second_group[1][3] = 3, as hospital 3 is the applicant's 3rd preference.

            for j in range(len(temp)):
                second_group[i+1][temp[j]] = j+1
        
        # Try and read another line to see if the file is empty. If it reads then the input file is invalid and has too many rows.
        if f.readline():
            print(f'Invalid input file. File has more than {total_rows} rows. File should have exactly {total_rows} rows for n = {n_lines}. Make sure there is not an extra newline.')
            return
        
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
    output = read_input(input_file_path)

    # Check if read input file returned something/didn't error out
    if not output:
        return
    
    first_prefs, second_prefs = output
    if output_file_path == '':
        output_file_path = input("Provide a file path to write the output to: ")

    # Create empty matching/pairing lists. 
    first_matchings = [0] * len(first_prefs)
    second_matchings = [0] * len(second_prefs)

    # Initialize a list of all free/unsassigned hospitals
    free = list(range(1,len(first_prefs)))

    # While the list of free hospitals is not empty
    while free:
        # Choose last hospital in free list, ordering doesn't matter here. 
        h = free[-1]

        # Propose the highest preferred applicant of the current hospital
        a = first_prefs[h].pop()

        # Check if the hospital is currently matched (h_cur is not 0).
        h_cur = second_matchings[a]

        if h_cur == 0:
            # Assign hospital to highest available preferred applicant.
            first_matchings[h] = a
            second_matchings[a] = h
            free.pop()

        else:
            # If new applicant preffers current hospital more than its previous assignment, reassign them and free the previous hospital.
            if second_prefs[a][h] < second_prefs[a][h_cur]:
                first_matchings[h] = a
                second_matchings[a] = h
                free.pop()
                free.append(h_cur)

            # Otherwise, reject the pairing.
            else:
                continue
    
    write_output(output_file_path, first_matchings)

#match()