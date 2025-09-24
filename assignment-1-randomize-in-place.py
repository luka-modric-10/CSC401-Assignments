import random

# example array prints at the beginning of program
numArray = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"Original array: {numArray}\n")

# n = A.length
# for i = 1 to n
#     swap A[i] with A[Random(i,n)]

# swap method takes the index of the current element being iterated over
# and the randomly generated index (in range of array's length) and swaps the elements
def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]

# array length
numslength = len(numArray)

#iterate backwards over the array
for i in range(numslength - 1, 0, -1):
    #generate an index within the range of the array to find an element to swap with
    randomIndex = random.randint(0, i)
    #call previously defined swap method using current index and randomly generated index
    swap(numArray, i, randomIndex)
    #if randomly generated index happens to be the same as the current index, no change occurs. in any case, print array and iterator
    if (numArray[i] == numArray[randomIndex]):
        print(f"No swap occurred.       Current Array -> {numArray}   iterating backwards from: {i}")
    else: print(f"Swapped {numArray[i]} with {numArray[randomIndex]}.     Current Array -> {numArray}   iterating backwards from: {i}  ")

#final array after all swaps
print(f"\nRandomized array: {numArray}")
