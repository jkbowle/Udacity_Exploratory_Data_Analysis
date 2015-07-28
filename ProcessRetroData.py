'''
Created on Jul 24, 2015

@author:  Jason Bowles
'''
import csv
import math

# http://www.huffingtonpost.com/quora/what-are-the-major-eras-o_b_3547814.html

def get_era(in_year):
    year = int(in_year)
    if year < 1953:
        return  'post war'
    if year >= 1953 and year <= 1961:
        return 'westward expansion'
    if year > 1961 and year < 1969:
        return 'deadball 2'
    if year > 1968 and year < 1991:
        return 'free agency/arbitration'
    if year >= 1991 and year <= 2003:
        return 'steroids'    
    if year > 2003:
        return 'current'
    return 'none'

def load_hof_ids():
    hof_file = r'D:\python_scripts\retro_data\hof_pitchers.csv'
    hof_list = []
    with open(hof_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            hof_list.append(row['ID'])
    return hof_list

def get_innings_from_line(line_score):
    innings = 0
    paren = False
    for x in range(len(line_score)):
        val = line_score[x]
        if paren:
            if val == ")":
                innings = innings + 1
                paren = False
        else:
            if val == "(":
                paren = True
            else:
                innings = innings + 1
    return innings

file1 = r'D:\python_scripts\retro_data\game_log.csv'
file2 = r'D:\python_scripts\retro_data\game_log2.csv'
writer = None
output = open(file2, 'w')
first = True
header = ['date','starting_hof','era','game_number','day_of_week','visiting_team', 'visiting_league',
          'visiting_game_number', 'home_team', 'home_league', 'home_game_number','innings_played',
          'visit_score','home_score','game_outs','day_night_ind','attendance','time_of_game',
          'visit_line_score','home_line_score','visit_AB', 'visit_hits','visit_2B',
          'visit_3B','visit_HR','visit_RBI','visit_SACH','visit_SAC','visit_HBP',
          'visit_BB','visit_IBB', 'visit_SO','visit_SB', 'visit_CS','visit_GDP',
          'visit_CatherInterference','visit_LOB','visit_pitchers','visit_IndER', 
          'visit_TeamER', 'visit_WildPitch','visit_Balk','visit_Putout','visit_assists',
          'visit_errors','visit_passed_ball','visit_DP', 'visit_TriplePlay','home_AB', 'home_hits','home_2B',
          'home_3B','home_HR','home_RBI','home_SACH','home_SAC','home_HBP',
          'home_BB','home_IBB', 'home_SO','home_SB', 'home_CS','home_GDP',
          'home_CatherInterference','home_LOB','home_pitchers','home_IndER', 
          'home_TeamER', 'home_WildPitch','home_Balk','home_Putout','home_assists',
          'home_errors','home_passed_ball','home_DP', 'home_TriplePlay']
hof = load_hof_ids()
with open(file1) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if first:
            first = False
            writer = csv.DictWriter(output, fieldnames=header, lineterminator='\n')
            writer.writeheader()
        
        home_line = row['home_line_score']
        home_innings = get_innings_from_line(home_line)
        visit_line = row['visit_line_score']
        visit_innings = get_innings_from_line(visit_line)
        innings = math.ceil((home_innings + visit_innings)/2)
        row['innings_played'] = innings
        row['era'] = get_era(row['date'][:4])
        starting_hof = 0
        if row['visit_starting_pitcher_id'] in hof:
            starting_hof = 1
        
        if row['home_starting_pitcher_id'] in hof:
            starting_hof = starting_hof + 1
        
        row['starting_hof'] = starting_hof 
        new_row = {}
        for key in row.keys():
            if key in header:
                new_row[key] = row[key]
        writer.writerow(new_row)
        
output.close()
