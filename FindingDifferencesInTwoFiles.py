"""
finding differences in the contents of two files
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Input:
        line1 - string
        line2 - string
    Output:
        This function returns the index of the first character 
        that differs between the two strings. If both strings are 
        identical, the function will return the constant IDENTICAL. 
        If the strings have different lengths and the shorter string 
        matches the beginning of the longer string, the returned 
        index will be the index of the first character of the longer 
        string after the shorter string.
    """
    len1 = len(line1)
    len2 = len(line2)
    if len1 == len2:
        for index in range(0, len1):
            if line1[index] != line2[index]:
                return index
        return IDENTICAL
    else:
        for index in range(0, min(len1, len2)):
            if line1[index] != line2[index]:
                return index
        return min(len1, len2)
    
# test
# print(singleline_diff("Hola", "Hola"))
# print(singleline_diff("Hola", "Hola Mundo"))
# print(singleline_diff("Latex", "LaTeX"))
# print(singleline_diff("Uruguay", "Cabo Verde"))

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
        line1 - string 
        line2 - string
        idx - non-negative integer denoting the index of the first 
        character that differs between line1 and line2
    Output:
        Returns a string that, when printed, shows where the first 
        difference occurs between line1 and line2. If line1 or 
        line2 contains a newline or carriage return character 
        ('\n', '\r'), the function returns an empty string. It 
        also returns an empty string if idx is not between 0 and 
        the length of the shorter string.
    """
    newline1 = line1.count('\n') + line1.count('\r')
    newline2 = line2.count('\n') + line2.count('\r')
    if newline1 >= 1 or newline2 >= 1:
        return ''
    if idx == IDENTICAL:
        return ''
    elif 0 <= idx <= min(len(line1), len(line2)):
        string = '=' * idx + '^'
        return '{}\n{}\n{}\n'.format(line1, string, line2)
    else:
        return ''

# test
# line1 = "print 'Hola'"
# line2 = "print('Hola')"
# idx = singleline_diff(line1, line2)
# print(singleline_diff_format(line1, line2, idx))

# line1 = "print('Hola')"
# line2 = "print('Hola')"
# idx = singleline_diff(line1, line2)
# print(singleline_diff_format(line1, line2, idx))

# line1 = "print\n'Hola'"
# line2 = "print('Hola')"
# idx = singleline_diff(line1, line2)
# print(singleline_diff_format(line1, line2, idx))

# line1 = "print\r'Hola'"
# line2 = "print('Hola')"
# idx = singleline_diff(line1, line2)
# print(singleline_diff_format(line1, line2, idx))

# line1 = "filmaker"
# line2 = "film"
# idx = singleline_diff(line1, line2)
# print(singleline_diff_format(line1, line2, idx))

# line1 = "back"
# line2 = "background"
# idx = singleline_diff(line1, line2)
# print(singleline_diff_format(line1, line2, idx))

def multiline_diff(lines1, lines2):
    """
    Inputs:
        lines1 - List of strings where each string denotes a sigle line of text.
        lines2 - List of strings where each string denotes a sigle line of text.
    Outputs:
        Returns the index of the first string in lines1 or lines2 that differs. 
        It also returns the index within that string where the first difference 
        occurs. If both lists are the same, the function returns the tuple 
        (IDENTICAL, IDENTICAL). If one list is longer and the shorter list 
        matches the beginning of the longer list, the index of the first string 
        that differs is the index of the string after the end of the shorter 
        string in the longer string. The index of that string where the first 
        difference occurs is 0.
    """
    len1 = len(lines1)
    len2 = len(lines2)
    if len1 == len2:
        for idx in range(0, len1):
            if lines1[idx] != lines2[idx]:
                line = idx
                index = singleline_diff(lines1[idx], lines2[idx])
                return (line, index)
        return (IDENTICAL, IDENTICAL)
    else:
        for idx in range(0, min(len1, len2)):
            if lines1[idx] != lines2[idx]:
                line = idx
                index = singleline_diff(lines1[idx], lines2[idx])
                return (line, index)
        return (min(len1, len2), 0)

# test 
# list1 = ["The Picture of Dorian Gray", "Oscar Wilde"]
# list2 = ["The Picture of Dorian Gray", "Oscar Wilde"]
# print(multiline_diff(list1, list2))

# list3 = ["The Picture of Dorian Gray", "Oscar Wilde"]
# list4 = ["The Picture of Dorian Gray", "Oscar Wilde (1890)"]
# print(multiline_diff(list3, list4))

# list5 = ["The Picture of Dorian Gray", "Oscar Wilde", "1980"]
# list6 = ["The Art of War", "Sun Tzu"]
# print(multiline_diff(list3, list4))

# list7 = ["The Picture of Dorian Gray", "Oscar Wilde", "1980"]
# list8 = ["The Picture of Dorian Gray", "Oscar Wilde"]
# print(multiline_diff(list7, list8))

def get_file_lines(filename):
    """
    Input:
        filename - string that corresponds to a file to read.
    Output:
        Returns a list of lines, where each line in the list corresponds 
        to a line from the file. The function removes any newline and 
        carriage return ('\n', '\r') characters from every line.
    """
    with open(filename, 'r', encoding = 'utf-8') as file:
        table = []
        for line in file:
            updated_line = line.replace('\n', '')
            updated_line = updated_line.replace('\r', '')
            table.append(updated_line)
        return table

def file_diff_format(filename1, filename2):
    """
    Input:
        filename1 - string that corresponds to a file to read and compare.
        filename2 - string that corresponds to a file to read and compare.
    Output:
        Returns a string that, when printed, shows where the first difference 
        occurs between filename1 and filename2. The string contains the line
        index where the first difference occurs and displays the position in 
        that line where it occurs.
    """
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    line, index = multiline_diff(lines1, lines2)
    difference = '=' * index + '^'
    if (line, index) == (IDENTICAL, IDENTICAL):
        return "No differences\n"
    elif 0 <= line < len(lines1) and 0 <= line < len(lines2):
        line1 = lines1[line]
        line2 = lines2[line]
        new_line = 'Line {}:\n{}\n{}\n{}\n'.format(line, line1, difference, line2)
        return new_line
    elif line == len(lines1) and 0 <= line < len(lines2):
        new_line = 'Line {}:\n{}\n{}\n{}\n'.format(line, '', difference, lines2[line])
        return new_line
    elif line == len(lines2) and 0 <= line < len(lines1):
        new_line = 'Line {}:\n{}\n{}\n{}\n'.format(line, lines1[line], difference, '')
        return new_line
    else:
        return "Invalid line index"

# test
# filename1 = r'project2\file1.txt'
# filename2 = r'project2\file2.txt'
# print(file_diff_format(filename1, filename2))

# filename1 = r'project2\file3.txt'
# filename2 = r'project2\file4.txt'
# print(file_diff_format(filename1, filename2))

# filename1 = r'project2\file5.txt'
# filename2 = r'project2\file6.txt'
# print(file_diff_format(filename1, filename2))

# filename1 = r'project2\file7.txt'
# filename2 = r'project2\file8.txt'
# print(file_diff_format(filename1, filename2))

# filename1 = r'project2\file9.txt'
# filename2 = r'project2\file10.txt'
# print(file_diff_format(filename1, filename2))
