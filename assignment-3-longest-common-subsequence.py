import sys
import random

"""
>>>assignment checklist<<<
1. run your algorithm on two example DNA sequences of length 6
2. allow the user to modify the two sequences to test other examples
3. illustrate the process of filling up the table
4. print out the program state at each loop iteration (in this case, the table after each step of your algorithm)
"""


SEQUENCE_LENGTH = 6

# function that randomly generates 2 DNA sequences of length 6-------------------------------------
def generateRandomDNA(length):
  return ''.join(random.choice('ACGT') for _ in range(length))

DNAseq1 = generateRandomDNA(SEQUENCE_LENGTH)
DNAseq2 = generateRandomDNA(SEQUENCE_LENGTH)
print(f"Example DNA sequences: {DNAseq1} and {DNAseq2}\n")

# the user is allowed to modify the sequences if they so please
modify = input("Do you want to modify the DNA sequences? (y/n): ").strip().lower()
if modify == "y":

    # input validation
    DNAseq1 = input("\nEnter first DNA sequence of length 6: ").strip().upper()
    while len(DNAseq1) != SEQUENCE_LENGTH:
        print("The DNA sequence must be of length 6. Try again.")
        DNAseq1 = input("Enter first DNA sequence of length 6: ").strip().upper()

    # # input validation
    DNAseq2 = input("\nEnter second DNA sequence of length 6: ").strip().upper()
    while len(DNAseq2) != SEQUENCE_LENGTH:
        print("The DNA sequence must be of length 6. Try again.")
        DNAseq2 = input("Enter second DNA sequence of length 6: ").strip().upper()

    print(f"\nExample DNA sequences: {DNAseq1} and {DNAseq2}\n")


# algorithm

# print each step of table(2d array initialized with zeros) filling