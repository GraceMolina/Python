"""
read and write CSV files
"""

import csv

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

def print_table(table):
    """
    Print a nested list named table in the console.
    """
    for row in table:
        print(row)

def test_code():
    """
    Run examples to test the functions read_csv_file() and write_csv_file().
    """
    # test the reader function
    test_table = read_csv_file("test_case.csv")
    print_table(test_table)
    print()

    # test the writer function
    cancer_risk_table = read_csv_file("cancer_risk05_v4_county.csv")
    write_csv_file(cancer_risk_table, "cancer_risk05_v4_county_copy.csv")
    cancer_risk_copy = read_csv_file("cancer_risk05_v4_county_copy.csv")

    # test whether the tables cancer_risk_table and cancer_risk_copy are the same
    if (cancer_risk_table == cancer_risk_copy):
        print("The tables are the same.")
    else:
        print("The tables differ.")

# test the functions
test_code()
