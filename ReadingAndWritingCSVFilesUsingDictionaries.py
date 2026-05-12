"""
read a CSV file as a list of dictionaries and as a dictionary of dictionaries
write a list of dictionaries as a CSV file
"""

import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Takes a CSV file, a separator, and a quote and returns a list of the field names from that file.
    It assumes that the first row of the CSV file contains the field names.
    """
    with open(filename, "rt", newline = '', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter = separator, 
                                   quotechar = quote)
        return csvreader.fieldnames
    
def read_csv_as_list_dict(filename, separator, quote):
    """
    Takes a CSV file, a separator, and a quote and returns the data within 
    the file as a list of dictionaries.
    """
    table = []
    with open(filename, "rt", newline = '', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter = separator, 
                                   quotechar = quote)
        for row in csvreader:
            table.append(row)
        return table

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Imputs:
        filename - a CSV file
        keyfield - name of the colum with the id of each observation in the CSV file
        separator - delimiter of the CSV file
        quoate - text qualifiers used to encapsulate entries with delimiters
    Output:
        returns the data within the file as a dictionary of dictionaries
    """
    table = {}
    with open(filename, "rt", newline = '', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter = separator, 
                                   quotechar = quote)
        for row in csvreader:
            table[row[keyfield]] = row
        return table

def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
        filename - name of the created csv file
        table - a list of dictionaries with the data to create the CSV file
        fieldnames - list of string containing the field names in order
        separator - delimiter of the CSV file
        quoate - text qualifiers used to encapsulate entries with delimiters
    Output:
        A CSV file with the name filename, usign the given fieldnames. The CSV file should
        use the given separator and quote characters. All non-numeric fields will be quoted.
    """
    with open(filename, 'w', newline = '', encoding='utf-8') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames = fieldnames, delimiter = separator, 
                                   quotechar = quote, quoting = csv.QUOTE_NONNUMERIC)
        csvwriter.writeheader()
        for row in table:
            csvwriter.writerow(row)

