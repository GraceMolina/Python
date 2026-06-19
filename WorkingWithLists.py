"""
working with lists
"""

# exercise 1
prime_numbers = [2, 3, 5, 7, 11, 13]
# print 2nd, 4th, and 6th numbers in this list
for i in range(1, 6, 2):
    print(prime_numbers[i])

# exercise 2
example_list1 = ['e', 'x', 'a', 'm', 'p', 'l', 'e']
# form a list of the first and last element of example_list
first_and_last = []
first_and_last.append(example_list1[0])
first_and_last.append(example_list1[-1])
print(first_and_last)
# another way: first_and_last = [example_list1[0], example_list1[-1]]

# exercise 3
example_list2 = ['D', 'a', 't', 'a']
# form a list excluding the first and last element in example_list2
middle_list = example_list2[1:-1]
print(middle_list)

# exercise 4
# create a list whose first eight elements are True, followed by eight
# elements as False
true_false_list = [True for i in range(0, 8)]
for i in range(0, 8):
    true_false_list.append(False)
print(true_false_list)
# another way: true_false_list = 8 * [True] + 8 * [False]

# exercise 5
text = 'The world cup winner in 2022 was Argentina.'
words = text.split(' ')
print(words)

# exercise 6
def word_count(text, word):
    """
    Input:
        text - string
        word - string
    Outputs:
        Returns a list and a number. The elements of the list are the words in text,
        and the number is how many times word appears in text.
    """
    words = text.split(' ')
    number = text.count(word)
    return words, number

text = 'Experience is merely the name men gave to their mistakes.'
word = 'men'
words_list, word_count = word_count(text, word)
print(words_list)
print(word_count)

# exercise 7
list1 = ['H', 'a', 'y', 'a', 'o']
list2 = list1
print(list1)
print(list2)
# update the first item of list2
list2[0] = 'M'
print(list1)
print(list2)
# the resulting output is:
#['K', 'a', 'y', 'a', 'o']
#['K', 'a', 'y', 'a', 'o']
# since list1 and list2 point to the same object, updating the first element in list2 
# also updates the first element of list1

# exercise 8
list3 = ['M', 'i', 'y', 'a', 'z', 'a', 'k', 'i']
list4 = list(list3)
print(list3)
print(list4)
# update the first item of list4
list4[0] = 'H'
print(list3)
print(list4)
# the resulting output is:
#['M', 'i', 'y', 'a', 'z', 'a', 'k', 'i']
#['H', 'i', 'y', 'a', 'z', 'a', 'k', 'i']
# list() creates a copy of list3 that points to a different object, hence modifying 
# the first item of list4 does not change the first item of list3

# exercise 9
def list_max(num_list):
    """
    Input:
        num_list - list of numbers
    Output:
        Returns the maximum number in the list.
    """
    max_num = num_list[0]
    for i in num_list:
        if max_num < i:
            max_num = i
    return max_num

print(list_max([1, 4, 442, 6, 7, 2]))

# exercise 10
def concatenate_ints(int_list):
    """
    Input:
        int_list - list of integers
    Output:
        Concatenates the integers in int_list and returns the resulting number.
    """
    concatenation = ''
    for num in int_list:
        concatenation = concatenation + str(num)
    return int(concatenation)

print(concatenate_ints([1, 2, 3, 4, 5]))

# exercise 11
my_list = ["This", "course", "is", "great"]
print(my_list)

# split my_list in halves
half1 = my_list[0 : len(my_list) // 2]
half2 = my_list[len(my_list) // 2 : len(my_list)]
print(half1)
print(half2)
print("")

half1 = my_list[: len(my_list) // 2]
half2 = my_list[len(my_list) // 2 :]
print(half1)
print(half2)
print("")

# exercise 12
def strange_sum(numbers):
    """
    Intput:
        numbers - list of integers
    Output:
        Returns the sum of the integer numbers in number that are not divisible by 3.
    """
    sum = 0
    for num in numbers:
        if (num % 3) != 0:
            sum += num
    return sum 

print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
print(strange_sum(list(range(123)) + list(range(77))))
