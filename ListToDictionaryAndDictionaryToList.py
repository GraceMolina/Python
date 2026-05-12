"""
convert a list of tuples to a dictionary, and a dictionary to a list of tuples
"""

def covert_list_to_dict(namelist):
    """
    Takes a list of tuples and returns a dictionary. Each tuple is converted to an 
    item in the dictionary, where the first component is the key and the second component is the corresponding value
    """
    dict = {pair[0] : pair[1] for pair in namelist}
    return dict

def convert_dict_to_list(namedict):
    """
    Takes a dictionary and returns a list of tuples. Each item in the 
    dictionary is converted to a tuple, where the key is the first component 
    and the value is the second component
    """
    list = [(key, value) for key, value in namedict.items()]
    return list

# test functions
gpa_list = [("Camila Barker", 3.9), ("Elias Brasher", 2.8),
              ("Julia Hathaway", 3.3), ("Selena Bailey", 3.5)]

# test covert_list_to_dict()
gpa_dict = covert_list_to_dict(gpa_list)

# test convert_dict_to_list()
gpa_list_copy = convert_dict_to_list(gpa_dict)

print(gpa_list == gpa_list_copy)