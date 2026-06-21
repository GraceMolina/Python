"""
manipulating lists
"""

import random

# exercise 1
example_list1 = [i for i in range(6)]
print(example_list1)
# replace the third element of the list with 0
example_list1[2] = 0
print(example_list1)
print("")

# exercise 2
example_list2 = [i for i in range(0, 11, 2)]
print(example_list2)
# replace the second and third element of
# example_list2 with 0, 0, 0 such that example_lsit2 
# changes from [first_item, sencond_item, third_item, fourth_item,...]
# to [first_item, 0, 0, 0, fourth_item,...]
example_list2[1:3] = [0 for i in range(3)]
print(example_list2)
print("")

# exercise 3
example_list3 = [i for i in range(0, 21, 5)]
print(example_list3)
# append the number 0 at the end of example_list3
example_list3.append(0)
print(example_list3)
print("")

# exercise 4
example_list4 = [8]*4
print(example_list4)
# add the numbers in the list [0, 0, 0] to the end of example_list4
example_list4.extend([0,0,0])
print(example_list4)
print("")

# exercise 5
example_list5 = [5]*7
example_list6 = list(example_list5)
print(example_list5)
print(example_list6)
# add the numbers in the list [0, 0, 0] to the end of example_list4
# without mutating example_list5
example_list6.extend([0,0,0])
print(example_list5)
print(example_list6)

# exercise 6
example_list7 = [2, 1]
list_to_append = [0,0,0]
# loop that appends the numbers in the list
# [0,0,0] to the end of example_list6
for i in range(len(list_to_append)):
    example_list7.append(list_to_append[i])
print(example_list7)
print("")
# another way:
#for num in list_to_append:
    #example_list7.append(num)

# exercise 7
example_list8 = ['I', 'v', 'o', 'r', 'y', 'C', 'o', 'a', 's', 't']
example_tuple = tuple(example_list8)
print(example_tuple)

# exercise 8
example_list9 = ['G', 'e', 'r', 'm', 'a', 'n', 'y']
random.shuffle(example_list9)
print(example_list9)
print("")

# exercise 9
def flatten(nested_list):
    """
    Inputs:
        nested_list - list of lists
    Output:
        Returns a list of the items in each list in nested_list.
    """
    flat_list = []
    for row in nested_list:
        flat_list.extend(row)
    return flat_list

nested_list = [['G', 'e', 'r', 'm', 'a', 'n', 'y'], 
               ['I', 'v', 'o', 'r', 'y', 'C', 'o', 'a', 's', 't'], 
               ['2', '0', '2', '6']]
print(flatten(nested_list))
print("")

# exercise 10
def remove_duplicates(items):
    """
    Input:
        items - list
    Output:
        Removes the duplicates in items. The order of the resulting list matches the order in items.
    """
    indices = []
    for i in range(0, len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                indices.append(j)
    unique_list = []
    for i in range(0, len(items)):
        if i in indices:
            pass
        else:
            unique_list.append(items[i])
    # another way:
    # for item in items:
    #   if item is not in unique_list:
    #       unique_list.append(item)
    return unique_list

print(remove_duplicates(['G', 'e', 'r', 'm', 'a', 'n', 'y']))
print(remove_duplicates(['A', 'u', 's', 't', 'r', 'a', 'l', 'i', 'a']))
print(remove_duplicates([]))
print(remove_duplicates([1, 2, 2, 3, 3, 3, 4, 5, 6, 6]))
print(remove_duplicates(["cat", "dog", "cat", "pig", "cow", "cat", "pig", "pug"]))

# exercise 11
fib = [0, 1]
for i in range(0, 20):
    sum = fib[-2] + fib[-1]
    fib.append(sum)
print(fib)
print("")

# exercise 12
def compute_primes(bound):
    """
    Input:
        bound - integer greater than 2
    Output:
        Returns the prime numbers between 2 and bound-1 (inclusive).
    """
    integers = list(range(2, bound))
    for p in range(2, bound):
        for i in range(2*p, bound, p):
            if i in integers:
                integers.remove(i)
    return integers

print(len(compute_primes(200)))
print(len(compute_primes(2000)))




