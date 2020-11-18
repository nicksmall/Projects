# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 13:57:37 2020

@author: Nick
"""


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

players = pd.read_csv('http://drd.ba.ttu.edu/isqs6339/hw/hw2/players.csv', delimiter= '|') 
player_sessions = pd.read_csv('http://drd.ba.ttu.edu/isqs6339/hw/hw2/player_sessions.csv')
players.fillna('LoD', inplace=True)
player_merged = player_sessions.join(players.set_index('playerid'), on = 'playerid')
player_merged['damage_done'].fillna(round(player_merged['damage_done'].mean(),2), inplace=True)

player_merged['player_performance_metric'] = np.nan
player_merged['dps_quality'] = np.nan
player_merged['player_dkp_gen_rate'] = np.nan

for i in range(len(player_merged['session'])):
    damage_done = round(player_merged['damage_done'][i],2)
    player_merged['player_performance_metric'][i] = ((damage_done * 3.125) + (player_merged['healing_done'][i] * 4.815))/4
    
    if damage_done > 600000:
        player_merged['dps_quality'][i] = 'High'
        player_merged['player_dkp_gen_rate'][i] = player_merged['player_performance_metric'][i] * 1.25
    elif damage_done > 400000 and damage_done < 599999:
        player_merged['dps_quality'][i] = 'Medium'
        player_merged['player_dkp_gen_rate'][i] = player_merged['player_performance_metric'][i] * 1.15
    else:
        player_merged['dps_quality'][i] = 'Low'
        if player_merged['clan'][i] == 'LoD':
            player_merged['player_dkp_gen_rate'][i] = player_merged['player_performance_metric'][i] * 2.35
        else:
            player_merged['player_dkp_gen_rate'][i] = player_merged['player_performance_metric'][i] * 0.85

max_damage = player_merged.loc[player_merged['damage_done'].idxmax(), 'handle']
max_healing = player_merged.loc[player_merged['healing_done'].idxmax(), 'handle']
max_performance_metric = player_merged.loc[player_merged['player_performance_metric'].idxmax(), 'handle']
max_dkp_gen_rate = player_merged.loc[player_merged['player_dkp_gen_rate'].idxmax(), 'handle']
print('max_damage:',max_damage)
print('max_healing:',max_healing)
print('max_performance_metric:',max_performance_metric)
print('max_dkp_gen_rate:',max_dkp_gen_rate)

average_damage_heal_session = player_merged[['session','clan', 'damage_done', 'healing_done']].groupby(['session','clan']).mean()
average_damage_heal_position = player_merged[['position', 'damage_done', 'healing_done']].groupby(['position']).mean()
merged_data = player_merged.sort_values(by=['player_dkp_gen_rate'])

average_damage_heal_position.to_csv('average_damage_heal_position.csv')
average_damage_heal_session.to_csv('average_damage_heal_session.csv')
merged_data.to_csv('merged_data.csv', index=False)


# 1. What is the quality of your data? i.e. how clean is your data? 
#The data had missing values for damage_done and clan. 
#These are two issues that affected the quality of the data and required the data set to be cleaned
#The data is now cleaned and of good quality.

# 2. What steps did you take to clean your data and why did you choose those options?
#The missing data in the damage_done column were cleaned and placed with the mean of the column
#this was chosen because it did not affect the data signicantly and the new data points can be used.

# 3. Are there other potential ways you could have cleaned your data?
#The data could have been cleaned by removing the rows with missing data
#Or the row areas with missing value could be placed with the value of zero.

# 4. Which player has the highest values for:
# damage_done: mindmelter
# healing_done: bakko
# player_performance_metric: bakko
# player_dkp_gen_rate: cerdwin