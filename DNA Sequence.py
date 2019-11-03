# DNA - SEQUENCES

# -- Perform basic operations with DNA data represented as lists and strings.
# -- Creating our own libraries.
# -- Introduction to BioPython. (Optional)

import random
import numpy as np

# This is a lambda function that generates a random string of length n containing characters from the choices A,C,G,T
# It uses a list comprehension to generate a sequence of random characters, which are then joined together with .join()
# The resulting string is a typical file/input format for working with gene data.
generate_genome = lambda n: ''.join([random.choice('ACGT') for i in range(n)])

# generate genome string and convert to a list of 100 characters for Task 1 + 2
genome_task1_str = generate_genome(100)
genome_task1_list = list(genome_task1_str)

# Similar list to use in Task 2
genome_task2_list = list(generate_genome(100))

# Lists to use in Task 3
genome_task3_list_a = list(generate_genome(100))
genome_task3_list_b = list(generate_genome(100))

# the search criterion
search_char = 'C'

#####################################################

# 1. Replace all occurrences of search_char in genome_task1_list by the number 0.
for n, i in enumerate(genome_task1_list):
    if i == search_char:
        genome_task1_list[n] = 0

# 2. Find and remove all occurrences of search_char from genome_task2_list.
for n, i in enumerate(genome_task2_list):
    if i == search_char:
        del genome_task2_list[n]

# 3. We now look at genome_task3_list_a and genome_task3_list_b, both length 100 but with (probably) different sequences.
# Count the number of matching DNA base pairs: A with T (or T with A), C with G (or G with C).
# For example, if genome_task3_list_a[0] is an 'A' and genome_task3_list_b[0] is a 'T' we have a matching base pair.
count = 0
count_1 = 0
count_2 = 0
count_3 = 0
for i in range(len(genome_task3_list_a)) :
    left = genome_task3_list_a[i]
    right = genome_task3_list_b [i]
    if left == 'A' and right == 'T':
        count = count + 1
    if left == 'T' and right == 'A':
        count_1 = count_1 + 1
    if left == 'C' and right == 'G':
        count_2 = count_2 + 1
    if left == 'G' and right == 'C':
        count_3 = count_3 +1

print (count)
print (count_1)
print (count_2)
print (count_3)

tup_1 =[]
tup_2 = []
tup_3 = []
tup_4 = []
# 4. Create a list of tuples of just the matching base pairs in genome_task3_list_a and genome_task3_list_b.
# For example, from 'A','T','T','C' and 'T','A','A','T' you would get [('A','T'),('T','A'),('T','A')]
# which is a list of 3 tuples.
for i in range(len(genome_task3_list_a)) :
    left = genome_task3_list_a[i]
    right = genome_task3_list_b [i]
    if left == 'A' and right == 'T':
        tup_1.append((left, right))
    if left == 'T' and right == 'A':
        tup_2.append((left, right))
    if left == 'C' and right == 'G':
        tup_3.append((left, right))
    if left == 'G' and right == 'C':
        tup_4.append((left, right))
tup_5 = []
count_5 = 0
count_reset = [0]
# 5. Repeat Task 3, but this time find the length of the longest consecutive sequence of matching base pairs.
# For example, if genome_task3_list_a contains the sequence 'A','T','T','C' and genome_task3_list_b contains 'T','A','A','T' then we have a consecutive sequence of 3 matching base pairs.
for i in range(len(genome_task3_list_a)) :
    up = genome_task3_list_a[i]
    down = genome_task3_list_b [i]
    if (up == 'A' and down == 'T') or (up == 'T' and down == 'A') or (up == 'C' and down == 'G') or (up == 'G' and down == 'C'):
        count_5 = count_5 + 1
    else:
        if count_5 > 0:
            count_reset.append(count_5)
            count_5=0
if count_5 > 0:
    count_reset.append(count_5)
    count_5=0
print(f'the max count_reset is {max(count_reset)}')
