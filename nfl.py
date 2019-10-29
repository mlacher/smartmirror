from sportsreference.nfl.teams import Teams
import pandas as pd


teams = Teams()
d = []
def nfl_stats():
    for team in teams:
        d.append({'Rank': team.rank, 'Team': team.name, 'Win': team.wins, 'Lose': team.losses})
        
        # Prints the team's average margin of victory
        
    return(pd.DataFrame(d))