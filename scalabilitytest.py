from matching import match
from verify import verify
import matplotlib.pyplot as plt
import time
import random
import os

def generate_match_test_input(pair_count):
    input_filename = f"inputs/scalability_input_{pair_count}.txt"
    with open(input_filename, 'w') as f:
        f.write(f"{pair_count}\n")
        for _ in range(pair_count):
            # Generate a random permutation of preferences
            preferences = list(range(1, pair_count + 1))
            random.shuffle(preferences)
            f.write(' '.join(map(str, preferences)) + '\n')
        for _ in range(pair_count):
            preferences = list(range(1, pair_count + 1))
            random.shuffle(preferences)
            f.write(' '.join(map(str, preferences)) + '\n')

def generate_verify_test_input(pair_count):
    input_filename = f"inputs/scalability_input_{pair_count}.txt"
    output_filename = f"outputs/scalability_output_{pair_count}.txt"
    verify_filename = f"inputs/scalability_verify_input_{pair_count}.txt"

    with open(input_filename, 'r') as f_in:
        input_data = f_in.read()

    with open(output_filename, 'r') as f_out:
        output_data = f_out.read()

    # combine
    with open(verify_filename, 'w') as f_verify:
        f_verify.write(input_data)
        f_verify.write(output_data)
    

def measure_match_runtimes(test_cases):
    resulting_times = [-1]*len(test_cases)

    for pair_count in test_cases:
        print(f"Testing pair count: {pair_count}")
        input_filename = f"inputs/scalability_input_{pair_count}.txt"
        if not os.path.exists(input_filename):
            generate_match_test_input(pair_count)
        output_filename = f"outputs/scalability_output_{pair_count}.txt"
        start_time = time.time()
        match(input_filename, output_filename)
        end_time = time.time()
        resulting_times[test_cases.index(pair_count)] = end_time - start_time

    return resulting_times

def measure_verify_runtimes(test_cases):
    resulting_times = [-1]*len(test_cases)

    for pair_count in test_cases:
        print(f"Testing pair count: {pair_count}")
        input_filename = f"inputs/scalability_verify_input_{pair_count}.txt"
        if not os.path.exists(input_filename):
            generate_verify_test_input(pair_count)
        output_filename = f"outputs/scalability_verify_output_{pair_count}.txt"
        start_time = time.time()
        verify(input_filename, output_filename)
        end_time = time.time()
        resulting_times[test_cases.index(pair_count)] = end_time - start_time

    return resulting_times
    
def graph_times(test_cases, times, title):
    plt.figure(figsize=(8, 6))
    plt.plot(test_cases, times, marker='o')
    plt.title(f"{title}: Pair Count vs Time Taken")
    plt.xlabel('Number of Pairs')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.xticks(test_cases)
    plt.show()

def scalability_test():
    test_cases = [100*n for n in range(1, 20)]
    match_times = measure_match_runtimes(test_cases)
    verify_times = measure_verify_runtimes(test_cases)
    graph_times(test_cases, match_times, "Matching Algorithm")
    graph_times(test_cases, verify_times, "Verification Algorithm")


scalability_test()
