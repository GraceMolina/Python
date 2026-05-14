"""
analyze baseball data
"""

import csv

###############################
# functions to read CSV files #
###############################

# read a CSV file as a list of dictionaries
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
    
# read a CSV file as a dictionary of dictionaries
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
    
###################################
# formulas for batting statistics #
###################################

# typical cutoff used for official statistics
MINIMUM_AB = 500

# compute the player's batting average
def batting_average(info, batting_stats):
    """
    Inputs:
        info - dictionary with baseball data information
        batting_stats - dictionary with batting statitics
    Outputs:
        Returns the batting average as a float.
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return hits / at_bats
    else:
        return 0
    
# compute the player's on-base percentage
def onbase_percentage(info, batting_stats):
    """
    Inputs:
        info - dictionary with baseball data information
        batting_stats - dictionary with batting statitics
    Outputs:
        Returns the on-base percentage as a float.
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    walks = float(batting_stats[info["walks"]])
    if at_bats >= MINIMUM_AB:
        return (hits + walks) / (at_bats + walks)
    else:
        return 0
    
# compute the player's slugging percentage
def slugging_percentage(info, batting_stats):
    """
    Inputs:
        info - dictionary with baseball data information
        batting_stats - dictionary with batting statitics
    Outputs:
        Returns the slugging percentage as a float.
    """
    hits = float(batting_stats[info["hits"]])
    doubles = float(batting_stats[info["doubles"]])
    triples = float(batting_stats[info["triples"]])
    home_runs = float(batting_stats[info["homeruns"]])
    singles = hits - doubles - triples - home_runs
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return (singles + 2 * doubles + 3 * triples + 4 * home_runs) / at_bats
    else:
        return 0

##################################
# part 1: compute players with   #
# top batting statistics by year #
##################################

def filter_by_year(statistics, year, yearid):
    """
    Takes a list of dictionaries named statistics, where each dictionary
    contains batting statistics. The function also takes a year and the 
    key for the year values. It returns a list of dictionaries for the given year.
    """
    filtered_statistics = []
    for row in statistics:
        if float(row[yearid]) == year:
            filtered_statistics.append(row)
    return filtered_statistics

def top_player_ids(info, statistics, formula, numplayers):
    """
    Inputs:
        info - dictionary with baseball data information
        statistics - list of dictionaries, where each dictionary contains 
                     batting statistics
        formula - function that takes info and statistics as arguments
                  and returns a compound statistic
        numplayers - number of top players to return
    Outputs:
        Returns a list of 2-tuples of the top numplayers sorted in decreasing 
        order of the compound statistic. Each 2-tuple consists of the id of 
        the player and their corresponding compound statistic.
    """
    compound_statistics = []
    for row in statistics:
        compound_statistic = formula(info, row)
        compound_statistics.append((row[info["playerid"]],compound_statistic))
    compound_statistics.sort(key = lambda pair : pair[1], reverse = True)
    top_players = [compound_statistics[i] for i in range(min(numplayers, len(compound_statistics)))]
    return top_players

def lookup_player_names(info, top_ids_and_stats):
    """
    Inputs:
        info - dictionary with baseball data information
        top_ids_and_stats - list of 2-tuples. The first component of each
                            2-tuple corresponds to the playerid and the second
                            component to a compound statistic
    Output:
        Returns a list of strings. Each string has the format 
        "x.xxx -- FirstName LastName", where "x.xxx" corresponds 
        to a player's compound statistic and "FirstName LastName" 
        corresponds to the player's name.
    """
    masterfile = read_csv_as_nested_dict(info["masterfile"], 
                                         info["playerid"], info["separator"], info["quote"])
    top_stats_and_names = []
    for pair in top_ids_and_stats:
        name = masterfile[pair[0]][info["firstname"]] + ' ' + masterfile[pair[0]][info["lastname"]]
        stat_and_name = f"{pair[1]:.3f}" + ' --- ' + name
        top_stats_and_names.append(stat_and_name)
    return top_stats_and_names

def compute_top_stats_year(info, formula, numplayers, year):
    """
    Inputs:
        info - dictionary with baseball data information
        formula - function that takes info and statistics as arguments
                  and returns a compound statistic
        numplayers - number of top players to return
        year - an interger denoting a year
    Outout:
        Returns a list of strings. The list consists of the top numplayers for a given year, 
        as determined by the specified formula.
    """
    data = read_csv_as_list_dict(info["battingfile"], info["separator"], info["quote"])
    data_by_year = filter_by_year(data, year, info["yearid"])
    top_statistics_byid = top_player_ids(info, data_by_year, formula, numplayers)
    top_statistics_byname = lookup_player_names(info, top_statistics_byid)
    return top_statistics_byname

#################################################################
# part 2: compute players with top batting statistics by career #
#################################################################

def aggregate_by_player_id(statistics, playerid, fields):
    """
    Inputs:
        statistics - list of dictionaries, where each dictionary contains 
                     batting statistics
        playerid - name of the column that contains players' ids
        fields - list of the names of the columns that should be aggregated
    Output:
        Returns a dictionary of dictionaries. Each key is the player's id and 
        its corresponding value a dictionary of batting statistics.
    """
    players_list = []
    for row in statistics:
        players_list.append(row[playerid])
    players_list = list(set(players_list))
    dict1 = {}
    for player in players_list:
        player_dict = {key : 0 for key in fields}
        player_dict[playerid] = player
        dict1[player] = player_dict
    for row in statistics:
        player_iq = row[playerid]
        for col in fields:
            dict1[player_iq][col] += float(row[col])
    return dict1

def compute_top_stats_career(info, formula, numplayers):
    """
    Inputs:
        info - dictionary with baseball data information
        formula - function that takes info and statistics as arguments
                  and returns a compound statistic
        numplayers - number of top players to return
    Output:
        Returns a list of strings. The list consists of the top numplayers
        determined by the given formula.
    """
    data = read_csv_as_list_dict(info["battingfile"], info["separator"], info["quote"])
    aggregate_data = aggregate_by_player_id(data, info["playerid"], info["battingfields"])
    list_of_statistics = list(aggregate_data.values())
    top_stats_byid = top_player_ids(info, list_of_statistics, formula, numplayers)
    top_stats_byname = lookup_player_names(info, top_stats_byid)
    return top_stats_byname

#############
# test code #
#############

def test_baseball_statistics():
    """
    Simple testing code.
    """

    #
    # Dictionary containing information needed to access baseball statistics
    # This information is all tied to the format and contents of the CSV files
    #
    baseballdatainfo = {"masterfile": "Master_2016.csv",   # Name of Master CSV file
                        "battingfile": "Batting_2016.csv", # Name of Batting CSV file
                        "separator": ",",                  # Separator character in CSV files
                        "quote": '"',                      # Quote character in CSV files
                        "playerid": "playerID",            # Player ID field name
                        "firstname": "nameFirst",          # First name field name
                        "lastname": "nameLast",            # Last name field name
                        "yearid": "yearID",                # Year field name
                        "atbats": "AB",                    # At bats field name
                        "hits": "H",                       # Hits field name
                        "doubles": "2B",                   # Doubles field name
                        "triples": "3B",                   # Triples field name
                        "homeruns": "HR",                  # Home runs field name
                        "walks": "BB",                     # Walks field name
                        "battingfields": ["AB", "H", "2B", "3B", "HR", "BB"]}

    print("Top 5 batting averages in 1923")
    top_batting_average_1923 = compute_top_stats_year(baseballdatainfo, batting_average, 5, 1923)
    for player in top_batting_average_1923:
        print(player)
    print("")

    print("Top 10 batting averages in 2010")
    top_batting_average_2010 = compute_top_stats_year(baseballdatainfo, batting_average, 10, 2010)
    for player in top_batting_average_2010:
        print(player)
    print("")

    print("Top 10 on-base percentage in 2010")
    top_onbase_2010 = compute_top_stats_year(baseballdatainfo, onbase_percentage, 10, 2010)
    for player in top_onbase_2010:
        print(player)
    print("")

    print("Top 10 slugging percentage in 2010")
    top_slugging_2010 = compute_top_stats_year(baseballdatainfo, slugging_percentage, 10, 2010)
    for player in top_slugging_2010:
        print(player)
    print("")

    # can also use lambdas for the formula
    # this one computes onbase plus slugging percentage
    print("Top 10 OPS in 2010")
    top_ops_2010 = compute_top_stats_year(baseballdatainfo,
                                          lambda info, stats: (onbase_percentage(info, stats) +
                                                               slugging_percentage(info, stats)),
                                          10, 2010)
    for player in top_ops_2010:
        print(player)
    print("")

    print("Top 20 career batting averages")
    top_batting_average_career = compute_top_stats_career(baseballdatainfo, batting_average, 20)
    for player in top_batting_average_career:
        print(player)
    print("")

test_baseball_statistics()