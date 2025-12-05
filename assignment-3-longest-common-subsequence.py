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



# function that prints each step of table(2d array initialized with zeros) filling-------------------------------------
def printLCStable(table, DNAseq1, DNAseq2):
    m = len(DNAseq1)
    n = len(DNAseq2)

    # alignment and formatting
    header = "       "
    for char in DNAseq2:
        header += f"{char:>3}"
    print(header)

    # print by row
    for i in range(m + 1):
        rowChar = DNAseq1[i - 1] if i > 0 else " "

        rowStr = f"{rowChar:^4}"

        for j in range(n + 1):
            val = table[i][j]
            rowStr += f"{val:>3}"

        print(rowStr)
    print()

# function that executes LCS algorithm-------------------------------------
def LCSalgo(DNAseq1, DNAseq2):
    m = len(DNAseq1)
    n = len(DNAseq2)

    # initialize table with zeros
    table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # populate table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if DNAseq1[i - 1] == DNAseq2[j - 1]:
                # base/nucleotide match --> take max of diagonal cell's value and add 1
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                # base/nucleotide doesn't match --> take max value of top and left cells
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

        # print table after completing a row
        print(f"\nTable after filling row {i} (Nucleotide '{DNAseq1[i - 1]}'):")
        printLCStable(table, DNAseq1, DNAseq2)

    return table[m][n], table

# function that backtracks through table to identify matches in both sequences and reconstructs the LCS as a string
def findLCSstring(table, DNAseq1, DNAseq2):
    LCSstr = []
    i = len(DNAseq1)
    j = len(DNAseq2)

    # backtrack
    while i > 0 and j > 0:
        # if nucleotides match, it is part of the LCS
        if DNAseq1[i - 1] == DNAseq2[j - 1]:
            LCSstr.append(DNAseq1[i - 1])
            i -= 1
            j -= 1
        # if nucleotides DON'T match, move in the direction of the larger value
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # The string was built backwards, so reverse it
    return "".join(reversed(LCSstr))

# main method execution--------------------------------------------------------------------------
def main():
    DNAseq1 = generateRandomDNA(SEQUENCE_LENGTH)
    DNAseq2 = generateRandomDNA(SEQUENCE_LENGTH)
    print(f"Example DNA sequences: {DNAseq1} and {DNAseq2}\n")

    # the user is allowed to modify the sequences if they so please
    modify = input("Do you want to modify the DNA sequences? (y/n): ").strip().lower()
    if modify == "y":

        # input validation
        DNAseq1 = input("Enter first DNA sequence of length 6: ").strip().upper()
        while len(DNAseq1) != SEQUENCE_LENGTH:
            print("The DNA sequence must be of length 6. Try again.")
            DNAseq1 = input("Enter first DNA sequence of length 6: ").strip().upper()

        # # input validation
        DNAseq2 = input("\nEnter second DNA sequence of length 6: ").strip().upper()
        while len(DNAseq2) != SEQUENCE_LENGTH:
            print("The DNA sequence must be of length 6. Try again.")
            DNAseq2 = input("Enter second DNA sequence of length 6: ").strip().upper()

        print(f"\nExample DNA sequences: {DNAseq1} and {DNAseq2}\n")

    LCSlength, LCStable = LCSalgo(DNAseq1, DNAseq2)

    LCSstring = findLCSstring(LCStable, DNAseq1, DNAseq2)

    print(f"The longest common subsequence is {LCSstring} of length {LCSlength}.")


if __name__ == '__main__':
    main()