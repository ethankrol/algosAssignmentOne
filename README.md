Names: Ethan Krol (UFID: 33541943), Hugo Liu (UFID: 46439406)

## General Tasks

Ethan: matching engine, example I/O for matching engine, README
Hugo: verifier, example I/O for verifier, scalability

## Matching Engine

-- TODO

## Verifier

Located at: verify.py
Dependencies: none

### How to Run:

The verifier takes in the original matching input as input, with the matching output concatenated after it.

### Example Input

```
3
1 2 3
2 3 1
2 1 3
2 1 3
1 2 3
1 2 3
1 2
2 3
3 1
```

- The first line represents the number of students/hospitals (n)
- The next n\*2 lines represents the hospital and student preferences
- The next n lines represents a hypothetical matching

Make sure to create a file like this, or note the file locations of one of the verify_exampleX.in files.

To create one on your own easily, you can run the matching function and concatenate the result .out file to the original input file.

### To Run

Either run verify.py, or import the _verify_ function from verify.py and run in a separate file.

Example command: c:/.../algosAssignmentOne/verify.py

### Function Instructions

The verify function takes in 2 optional arguments: the input file path and output file path.

- The input file path indicates what file to read from. Omitting this will prompt the user to input a file path on the command line.
- The output file path indicates what file to print the result to. Omitting this will cause no output file to be written to. However, the result will still print in the command line.

The output file, should an output file path be provided, will contain one line explaining the result.

## Scalability Test

Located at: scalabilitytest.py
Dependencies: matplotlib

To import:

```
pip install matplotlib
or
pip3 install matplotlib
```

### How to Run:

The scalability test function works by taking in several test cases in the form of pair_counts.

Example Function Call: scalability_test([100, 200, 300, 400])

- This tests cases with 100, 200, 300, and 400 student-hospital pairs

It works by searching the inputs and outputs folders for files with the names

- input/scalability*verify_input*[pair_count].txt
- input/scalability*verify_input*[pair_count].txt

**If these files do not exist, the function will generate new ones automatically**

Therefore, you can run scalability_test([100, 200, 300, 400]) with no existing files, and the function will randomly generate example test files corresponding to the pair counts automatically.

**Note**:

these generated files always result in valid matchings/inputs, so there should be no errors or unstable results from the verifier. Therefore the verification scalability test will test verifying stable matchings

### To Run

Either run scalabilitytest.py after editing the _test_cases_ variable, or import scalability_test from scalabilitytest.py and run in a separate file.

Example command: c:/.../algosAssignmentOne/scalabilitytest.py

### Function Instructions

As explained earlier, the function takes in 1 required test_cases variable in the form of a python list of integers.

The function will output two matplotlib graphs. These graphs will also be saved under /graphs directory.

## Scalability Test Outputs

![Matching Algorithm Graph](graphs/Matching%20Algorithm.png)
![Verification Algorithm Graph](graphs/Verification%20Algorithm.png)

From analyzing these graphs, we can see both graphs exhibit a curve upward. The curve can be described as polynomial.

This makes sense because the implemented matching and verifying algorithms run in worst case polynomial time (big O of n^2).
