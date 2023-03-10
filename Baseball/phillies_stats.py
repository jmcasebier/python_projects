#!/usr/bin/env python3
#type:ignore

#####PITCHER STATCAST#####
# from pybaseball import playerid_lookup, statcast_pitcher

# # Get player IDs
# wheeler_id = playerid_lookup(last='wheeler', first='zack').loc[0, 'key_mlbam'].item() # Zack Wheeler
# nola_id = playerid_lookup(last='nola', first='aaron').loc[0, 'key_mlbam'].item() # Aaron Nola

# # Get pitcher statcasts
# wheeler_statcast = statcast_pitcher(start_dt='2022-04-07', end_dt='2022-11-05', player_id=wheeler_id) # Zack Wheeler
# nola_statcast = statcast_pitcher(start_dt='2022-04-07', end_dt='2022-11-05', player_id=nola_id) # Aaron Nola

# # Write pitcher statcast to Excel
# wheeler_statcast.to_excel('wheeler_statcast_pitcher.xlsx')
# print('Wheeler pitcher statcast data written to Excel')
# nola_statcast.to_excel('nola_statcast_pitcher.xlsx')
# print('Nola pitcher statcast data written to Excel')

#####BATTER SPRAYCHART#####
# from pybaseball import playerid_lookup, statcast_batter, spraychart

# # Get player IDs
# harper_id = playerid_lookup(last='harper', first='bryce').loc[0, 'key_mlbam'].item() # Bryce Harper
# hoskins_id = playerid_lookup(last='hoskins', first='rhys').loc[0, 'key_mlbam'].item() # Rhys Hoskins

# # Get batter statcasts
# harper_statcast = statcast_batter(start_dt='2022-04-07', end_dt='2022-11-05', player_id=harper_id)
# hoskins_statcast = statcast_batter(start_dt='2022-04-07', end_dt='2022-11-05', player_id=hoskins_id)

# # Get home game data subsets
# harper_statcast_subset = harper_statcast[harper_statcast['home_team'] == 'PHI']
# hoskins_statcast_subset = hoskins_statcast[hoskins_statcast['home_team'] == 'PHI']

# # Create spraycharts
# spraychart(data=harper_statcast_subset, team_stadium='phillies', title='Bryce Harper (2022)', size=50)
# spraychart(data=hoskins_statcast_subset, team_stadium='phillies', title='Rhys Hoskins (2022)', size=50)

#####TEAM GAME LOGS#####
# from pybaseball import team_game_logs, spraychart

# # Get team batting game logs
# batting_logs = team_game_logs(season=2022, team='PHI', log_type='batting')

# # Write team batting logs to Excel
# batting_logs.to_excel('team_batting_logs.xlsx')
# print('Team batting game logs written to Excel')

# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#         000  0000000000    000000000    #
#         000  00000000000  00000000      #
#         001  001 001 001  100           #
#         101  101 101 101  101           #
#         110  011 110 010  101           #
#         101  101  10 101  101           #
#         111  111   1 111  111           #
#    111  111  111     111  111           #
#    111 1 11  111     11    111 111 1    #
#     1 111     1      1      1 11 11     #
#                                         #
#          http://jmcasebier.com          #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #