"""
working with strings in python
"""

# form a string using format 
country = 'France'
capital = 'Paris'
sentence = 'The capital of {} is {}.'.format(country, capital)
print(sentence)

mood1 = 'happy'
mood2 = 'sad'
sentence1 = "I feel {0}, do you feel {0}? Or are you {1}? I'm not sure if we should be {0}.".format(mood1, mood2)
print(sentence1)

name1 = 'Pierre'
age1 = 7
name2 = 'May'
age2 = 13
line1 = '{0:^10} {1:>3}'.format(name1, age1)
line2 = '{0:^10} {1:>3}'.format(name2, age2)
print(line1)
print(line2)

num = 3.283663293
output = '{0:<7.3f} {0:<7.2f}'.format(num)
print(output)

def echo(call, repeats):
    """
    Inputs:
        call - string
        repeats - integer
    Output:
        Prints repeats copies of the string call, adding a line break after each repetition.
    """
    word = call + '\n'
    print(word*repeats)

echo('optimistic', 5)

def is_substring(example_string, test_string):
    """
    Input:
        example_string - string
        test_string - string
    Output:
        Returns True if test_string is part of example_string. Returns False otherwise.
    """
    if example_string.count(test_string) >= 1:
        return True
    else:
        return False
    # return test_string in example_string # another way to define this function

print(is_substring("hola", "bla"))

def make_nametag(name, topic):
    """
    Input: 
        name - string
        topic - string
    Output:
        Returns a name tag.
    """
    name_tag = "Hi! My name is {}. This lecture covers {}.".format(name, topic)
    return name_tag

print(make_nametag('Edith', 'auctions'))

def make_int(int_string):
    """
    Inputs:
        int_string - string
    Output: 
        Returns int_string as an integer if int_string represents a non-negative number in 
        string format. Returns -1 otherwise.
    """
    if int_string.isdigit():
        return int(int_string)
    else:
        return -1

print(make_int('hola'))

def name_swap(name_string):
    """
    Input: 
        name_string - string consisting of a first name and a last name separated by an space.
    Output:
        Swaps the first name with the last name and returns the resulting string.
    """
    space = name_string.find(' ')
    first_name = name_string[:space]
    last_name = name_string[space + 1:]
    swaped = last_name + ' ' + first_name
    return swaped

print(name_swap('Salvador Amaya'))

def count_vowels(word):
    """
    Input:
        word - string
    Output
        Returns the number of lowercase vowels in word.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for vowel in vowels:
        count = word.count(vowel) + count
    return count

print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))

def demystify(l1_string):
    """
    Input:
        l1_string - string
    Output:
        Replace each 'l' with 'a' and each '1' with 'b' 
    """
    word = ''
    for letter in l1_string:
        if letter == 'l':
            word = word + 'a'
        elif letter == '1':
            word = word + 'b'
        else:
            word = word + letter
    return word

print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))
