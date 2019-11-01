from sportsreference.nfl.teams import Teams
import pandas as pd
import numpy as np


teams = Teams()
d = []
def nfl_stats():
    for team in teams:
        d.append({'Rank': team.rank, 'Team': team.name, 'W': team.wins, 'L': team.losses})
        
    #DataFrame will be splitted in upper and lower half for visability  
    df = pd.DataFrame(d)
    dfs = np.split(df, [16], axis=0)
    return(dfs)


