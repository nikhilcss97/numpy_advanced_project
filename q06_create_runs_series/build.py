#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_runs_series(match_code):




    temp=ipl_matches_array[0]==match_code

    return pd.Series(data=ipl_matches_array[16][temp],index=ipl_matches_array[11][temp])




print create_runs_series('392203')
