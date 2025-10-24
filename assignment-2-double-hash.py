import random
from turtledemo.penrose import start

# set the table size to 16 and initialize an empty hash table
tableSize = 16
table = [None] * tableSize

# set the first hash function as: h1 = key modulo 16
def hashFunc1(key):
    return key % 16

# set the second hash function as: h2 = 2(key modulo 4) + 1
def hashFunc2(key):
    return 2 * (key % 4) + 1

# example keys
keys = random.sample(range(1, 99), tableSize)
print(f"Example keys: {keys}\n")


# insertion status helper function AKA print program state at each loop iteration (pt 2)
def insertionStatus(inserted, key, slot, table, i, occupiedBy = None):
    message = ""

    # if boolean flag signals that the key was successfully inserted, print success message
    if inserted == True:
        # slot found on first try
        if i == 0:
            message = f"{key} inserted successfully in slot {slot}!"
        # if probe isn't zero, the slot wasn't found on the first try
        elif i == 1:
            # a skip has occurred signaled by the i having been incremented past its intialized zero
            message = f"{key} inserted successfully in slot {slot} after {i} probe!"
        else:
            message = f"{key} inserted successfully in slot {slot} after {i} probes!"

    #if boolean flags indicates insertion failed, attempt to resolve collision/skip with second hash function until
    # a slot is found. if probe is not 0, collision/skip was not resolved on the first try.
    else:
        if i == 0:
            message = f"Collision at slot {slot} (occupied by {occupiedBy}.)"
        else:
            message = f"Probe has landed on another occupied slot: {slot}."

    # output program state
    print(f"{message} Array: {table}; Probe i = {i}]\n")


# insertion function
def insert(key, table, tableSize):
    h1 = hashFunc1(key)
    h2 = hashFunc2(key)

    # boolean flag where True means the insertion was successful
    # and False means a collision or skip has occurred
    inserted = False

    # probe, i, initialized at zero
    i = 0

    # print program state at each loop iteration (pt 1)
    print(f"Inserting key {key}...")

    # insertion loop algorithm accounting for collisions and skips
    while i < tableSize:
        # determine slot key will be inserted into using hash function
        slot = (h1 + i * h2) % tableSize

        # probe/examine slot to check if empty
        if table[slot] is None:
            # if empty, insert key
            table[slot] = key
            insertionStatus(True, key, slot, table, i)
            return

        # collision: slot is occupied
        else:
            occupiedBy = table[slot]
            insertionStatus(False, key, slot, table, i, occupiedBy)

            # increment probe in the case of a collision
            i += 1

    # worst case, there aren't enough slots (which won't happen in this specific program because
    # the randomly generated keys are the exact quantity of the hash table slots
    print(f"Failed to insert {key} after {tableSize} probes (table full and/or empty slot not found); Array: {table}; Probe i = {i}]")


# run your algorithm on example keys that you insert into the hash table
for key in keys:
    insert(key, table, tableSize)

# print final hash table after insertion loop has terminated
print(f"\nFinal hash table: {table}")
