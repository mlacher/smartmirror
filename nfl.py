from sportsreference.nfl.teams import Teams
import pandas as pd
import numpy as np


teams = Teams()
d = []
def nfl_stats():
    for team in teams:
        d.append({'Rank': team.rank, 'Team': team.name, 'W': team.wins, 'L': team.losses})
        
        # Prints the team's average margin of victory
    df = pd.DataFrame(d)
    dfs = np.split(df, [16], axis=0)
    on = dfs[0]
    tw = dfs[1]
    #tw = tw.reset_index()
    dfs_s = pd.concat([on, tw])
    print(on)
    print(tw)
    return(dfs_s)

