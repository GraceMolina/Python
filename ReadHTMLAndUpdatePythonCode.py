"""
updating code from Python 2 to Python 3
"""

import re

def update_line(line):
    """
    Input:
        line - string corresponding to a line of code in Python 2
    Output:
        If the line is a print statement, it updates the line to 
        enclose the arguments for print in parentheses. Indentation 
        spaces are preserved. If the line is not a print statement, 
        it remains unchanged.
    """
    if line == 'print':
        return 'print()'
    else:
        updated_line = re.sub(r'print (.*)', r'print(\1)', line)
        return updated_line

# Some simple tests
print(update_line(""))
print(update_line("foobar()"))  
print(update_line("print 1 + 1"))      
print(update_line("    print 2, 3, 4"))

def update_pre_block(pre_block):
    """
    Input:
        pre_block - string corresponding to code enclosed by a pair of <pre>...</pre>
    Output:
        Replaces every print statement in pre_block that is writen in Python 2 to Python 3.
    """
    lines = pre_block.split('\n')
    for line in lines:
        updated_line = update_line(line)
        i = lines.index(line)
        lines[i] = updated_line
    block = "\n".join(lines)
    return block

# Some simple tests
print(update_pre_block(""))
print(update_pre_block("foobar()"))
print(update_pre_block("if foo():\n    bar()"))
print(update_pre_block("print\nprint 1+1\nprint 2, 3, 4"))
print(update_pre_block("    print a + b\n    print 23 * 34\n        print 1234"))

def update_file(input_file_name, output_file_name):
    """
    Input:
        input_file_name - name of a file containing code with print statements in Python 2.
        output_file_name - name used to save the updated version of input_file, where 
        Python 2 print statements are converted to Python 3 print statements.
    Output:
        Updates Python 2 print statements in input_file_name with Python 3 print statements
        and saves the updated file as output_file_name.
    """
    with open(input_file_name, 'r', encoding = 'utf-8') as file:
        pattern = r'(<pre class="cm">)(.*?)(</pre>)'
        table = []
        for line1 in file:
            updated_line = re.sub(pattern, lambda m: f"{m.group(1)}{update_pre_block(m.group(2))}{m.group(3)}", line1)
            table.append(updated_line)
    with open(output_file_name, 'w', encoding = 'utf-8') as file:
        for line in table:
            file.write(line)

# a couple of test files
update_file(r"project1\table.html", "table_updated.html")
update_file(r"project1\docs.html", "docs_updated.html")

# import some code to check whether table_updated.html is correct
import examples3_file_diff as file_diff
file_diff.compare_files("table_updated.html", r"project1\table_updated_solution.html")
