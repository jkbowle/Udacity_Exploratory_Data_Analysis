'''
Created on May 15, 2015

@author:  Jason Bowles
'''
import zipfile
import urllib2
import os


url_prefix = 'http://www.retrosheet.org/gamelogs/'
url_suffix = 'glYYYY.zip'
download_dir = r'D:\python_scripts\retro_data'
full_data = 'game_log.csv'
header = ['date','game_number','day_of_week','visiting_team', 'visiting_league',
          'visiting_game_number', 'home_team', 'home_league', 'home_game_number',
          'visit_score','home_score','game_outs','day_night_ind','completion_info',
          'forfeit_info','protest_info','park_id','attendance','time_of_game',
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
          'home_errors','home_passed_ball','home_DP', 'home_TriplePlay','Home_ump_id','Home_ump_name','1B_ump_id',
          '1B_ump_name','2B_ump_id','2B_ump_name','3B_ump_id','3B_ump_name','LF_ump_id',
          'LF_ump_name','RF_ump_id','RF_ump_name','visit_mgr_id','visit_mgr_name','home_mgr_id',
          'home_mgr_name','win_pitcher_id','win_pitcher_name','lose_pitcher_id','lose_pitcher_name',
          'save_pitcher_id','save_pitcher_name','game_win_batter_id','game_winner_batter_name',
          'visit_starting_pitcher_id','visit_starting_pitcher_name','home_starting_pitcher_id','home_starting_pitcher_name',
          'visit_order_1_id','visit_order_1_name','visit_order_1_position',
          'visit_order_2_id','visit_order_2_name','visit_order_2_position',
          'visit_order_3_id','visit_order_3_name','visit_order_3_position',
          'visit_order_4_id','visit_order_4_name','visit_order_4_position',
          'visit_order_5_id','visit_order_5_name','visit_order_5_position',
          'visit_order_6_id','visit_order_6_name','visit_order_6_position',
          'visit_order_7_id','visit_order_7_name','visit_order_7_position',
          'visit_order_8_id','visit_order_8_name','visit_order_8_position',
          'visit_order_9_id','visit_order_9_name','visit_order_9_position',
          'home_order_1_id','home_order_1_name','home_order_1_position',
          'home_order_2_id','home_order_2_name','home_order_2_position',
          'home_order_3_id','home_order_3_name','home_order_3_position',
          'home_order_4_id','home_order_4_name','home_order_4_position',
          'home_order_5_id','home_order_5_name','home_order_5_position',
          'home_order_6_id','home_order_6_name','home_order_6_position',
          'home_order_7_id','home_order_7_name','home_order_7_position',
          'home_order_8_id','home_order_8_name','home_order_8_position',
          'home_order_9_id','home_order_9_name','home_order_9_position',
          'additional_info','acquisition_info'
          ]
start = 1950
year = start

print 'header has: '+str(len(header))+ ' fields'
proxy_handler = urllib2.ProxyHandler({'http': 'http://ccproxy.countrylan.com:8080'})
proxy_auth_handler = urllib2.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('retro_sheet', 'http://www.retrosheet.org/gamelogs/', '*******', '********')
opener = urllib2.build_opener(proxy_handler, proxy_auth_handler)
urllib2.install_opener(opener)
    
while year <= 2014:
    suffix = url_suffix.replace("YYYY", str(year))
    url = url_prefix+suffix
    

    response = urllib2.urlopen(url)
    zippedData = response.read()
    outfile = os.path.join(download_dir,suffix)
    output = open(outfile,'wb')
    output.write(zippedData)
    output.close()
    year = year +1
    
year = start
first = True
outputFilename = os.path.join(download_dir,full_data)
output = open(outputFilename,'wb')
output.write(",".join(header)+"\n");
while year <= 2014:
    suffix = url_suffix.replace("YYYY", str(year))
    outfile = os.path.join(download_dir,suffix)
    zfobj = zipfile.ZipFile(outfile)
    for name in zfobj.namelist():
        uncompressed = zfobj.read(name)
        output.write(uncompressed)
    year = year + 1

output.close()
