"""
read a CSV file as a list of list
select columns and sort by an specific column
"""

import csv
import random

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
        csvreader = csv.reader(csvfile, skipinitialspace = True)
        for row in csvreader:
            table.append(row)
        return table
    
def write_csv_file(csv_table, file_name):
    """
    Given a nested list csv_table and a string name file_name, 
    write the fields in the csv_table into a comma-separated CSV file with the name file_name.
    """
    with open(file_name, 'w', newline = '') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = ',')
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
    sorted_table = my_table.sort(key = lambda row: row[col_idx], reverse = True)
    return sorted_table

# read a simple CSV file
test_table = read_csv_file("test_case.csv")  # file is available in this repository
print_table(test_table)
print()

# select the first and third column
print_table(select_columns(test_table, [0, 2]))
print()

# sort by the fourth column
sort_by_column(test_table, 3)
print_table(test_table)
print()

# read cancer-risk data set, select columns A, B, C, E, and L, then sort by column E in descending order
cancer_risk_table = read_csv_file("cancer_risk05_v4_county.csv")
col_indices = [0, 1, 2, 4, 11]
trimmed_risk_table = select_columns(cancer_risk_table, col_indices)
sort_by_column(trimmed_risk_table, 4)

# write trimmed and sorted cancer-risk data
write_csv_file(trimmed_risk_table, "sorted_cancer_risk_trimmed.csv")
    
# read the file "sorted_cancer_risk_trimmed.csv" and compare with your solution
trimmed_risk_solution_copy = read_csv_file("sorted_cancer_risk_trimmed.csv")

# test if sorted table and the copy are the same
print(trimmed_risk_table == trimmed_risk_solution_copy)