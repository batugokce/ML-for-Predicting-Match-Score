# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 23:49:34 2019

@author: Batuhan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def getWinnerTeam(row):
    if (row["FTR"] == 'H'):
        return row["HomeTeam"]
    elif (row["FTR"] == 'A'):
        return row["AwayTeam"]
    else:
        return "DRAW"


veriler = pd.read_csv("1819.csv")
istenen = pd.DataFrame(columns=["Ev sahibi","Misafir"])

for index, row in veriler.iterrows():
    if (row["HomeTeam"] == "Man United" ):
        print(index, row['HomeTeam'], row['AwayTeam'])
        print(getWinnerTeam(row))
        istenen = istenen.append({"Ev sahibi":row["HomeTeam"], "Misafir":row["AwayTeam"]},ignore_index = 1)
        
        
        
        
