"""
read a CSV file as a list of list
select columns and sort by an specific column
"""

import csv

def print_table(table):
    """
    Echo a nested list table to the console
    """
    for row in table:
        print(row)

def read_csv_file(file_name):
    """
    Given a CSV file named file_name, return the data within the file
    as a list of lists.
    """
    table = []
    with open(file_name, newline = '') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        for row in csvreader:
            table.append(row)
        return table
    
def write_csv_file(csv_table, file_name):
    """
    Given a nested list csv_table and a string name file_name, 
    write the fields in the csv_table into a comma-separated CSV file with the name file_name.
    """
    with open(file_name, 'w', newline = '') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = ',', quoting = csv.QUOTE_MINIMAL)
        for row in csv_table:
            csvwriter.writerow(row)

def select_columns(my_table, col_indices):
    """
    Takes a list of lists named my_table and a tuple of indices named col_indices,
    returns a list of lists. Each list contains the elements indexed by col_indices.
    """
    new_table = [[row[col] for col in col_indices] for row in my_table]
    return new_table

def sort_by_column(my_table, col_idx):
    """
    Takes a list of lists named my_table and a column index named col_idx,
    returns a list of list sorted by the element indexed by col_idx.
    """
    my_table.sort(key = lambda row: float(row[col_idx]), reverse = True)

def test_part2_code():
    """
    Run examples that test the functions for part 2
    """
    
    # read a simple CSV file
    test_table = read_csv_file("test_case.csv")
    print_table(test_table)
    print()
    
    # select the first and third column
    print_table(select_columns(test_table, [0, 2]))
    print()
    
    # sort by column 4
    sort_by_column(test_table, 3)
    print_table(test_table)
    print()

    # read cancer-risk data set, select columns A, B, C, E, and L, then sort by column E in descending order
    cancer_risk_table = read_csv_file("cancer_risk05_v4_county.csv")
    col_indices = [0, 1, 2, 4, 11]
    trimmed_risk_table = select_columns(cancer_risk_table, col_indices)
    sort_by_column(trimmed_risk_table, 4)
    write_csv_file(trimmed_risk_table, "cancer_risk_trimmed.csv")
    
    # read the file "cancer_risk_trimmed_solution.csv" and compare with solution named trimmed_risk_table
    trimmed_risk_solution = read_csv_file("cancer_risk_trimmed_solution.csv")
    print(trimmed_risk_table == trimmed_risk_solution)

test_part2_code()

#Output from test_part2_code()
##['1', '2', '3', '4']
##['5', '6', '7', '8']
##['-2', '-3', '-4', '-5']
##
##['1', '3']
##['5', '7']
##['-2', '-4']
##
##['5', '6', '7', '8']
##['1', '2', '3', '4']
##['-2', '-3', '-4', '-5']
