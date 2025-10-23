# set the table size to 16
# set the first hash function as: h1 = key modulo 16
# set the second hash function as: h2 = 2(key modulo 4) + 1
# run your algorithm on example keys that you insert into the hash table.
# display any collisions or skips to new slots.
# print out the program state at each loop iteration
#   [key inserted (indicate success or collision); array; probe number i]

#if there is a collision we set i to 1; then if there is still a collision we set i to 2; and so on