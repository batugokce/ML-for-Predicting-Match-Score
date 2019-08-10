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
    
def latestPointDealer(arr,el): # keep just previous 5 matches in the array
    if (len(arr) == 5):
        arr.pop(0)
        arr.append(el)
    else:
        arr.append(el)
    return arr

def createDictForRow(row,home,away):
    newRow = {}
    newRow["Home"] = row["HomeTeam"]
    newRow["Away"] = row["AwayTeam"]
    newRow["HG"] = int(row["FTHG"])
    newRow["AG"] = int(row["FTAG"])
    newRow["HAP"] = home[0]
    newRow["AAP"] = away[0]
    newRow["HLP"] = home[1]
    newRow["ALP"] = away[1]
    newRow["HAG"] = home[2]
    newRow["AAG"] = away[2]
    newRow["HAAG"] = home[3]
    newRow["AAAG"] = away[3]
    return newRow
    
def getSomeData(df,teamName,ind):
    nOfMatch = 0
    totalPoint = 0
    totalGoal = 0
    againstGoal = 0
    latestPoints = []
    for index, row in df.iterrows():
        if (index >= ind):
            return [round(totalPoint/nOfMatch,3),sum(latestPoints),round(totalGoal/nOfMatch,3),round(againstGoal/nOfMatch,3)]
        elif (row["HomeTeam"] == teamName):
            if (row["FTR"] == 'H' ):
                totalPoint += 3
                latestPoints = latestPointDealer(latestPoints,3)
            elif (row["FTR"] == 'D'):
                totalPoint += 1
                latestPoints = latestPointDealer(latestPoints,1)
            else:
                latestPoints = latestPointDealer(latestPoints,0)
            totalGoal += row["FTHG"]
            againstGoal += row["FTAG"]
            nOfMatch += 1
        elif (row["AwayTeam"] == teamName):
            if (row["FTR"] == 'A' ):
                totalPoint += 3
                latestPoints = latestPointDealer(latestPoints,3)
            elif (row["FTR"] == 'D'):
                totalPoint += 1
                latestPoints = latestPointDealer(latestPoints,1)
            else:
                latestPoints = latestPointDealer(latestPoints,0)
            totalGoal += row["FTAG"]
            againstGoal += row["FTHG"]
            nOfMatch += 1
        else:
            continue
        
    return [round(totalPoint/nOfMatch,3),sum(latestPoints),round(totalGoal/nOfMatch,3),round(againstGoal/nOfMatch,3)]
            
        
def createCSV(dataName):
    nOfTeams = 20
    nOfMatchPerWeek = nOfTeams / 2
    nOfTotalMatch = nOfTeams * (nOfTeams - 1)
    
    veriler = pd.read_csv("Pure data/" + dataName)
    istenen = pd.DataFrame(columns=["Ev sahibi","Misafir"])
    result = pd.DataFrame(columns=["Home","Away","HG","AG","HAP","AAP","HLP","ALP","HAG","AAG","HAAG","AAAG"])
    
    for index, row in veriler.iterrows():
        if (index >= 50):
            home = getSomeData(veriler,row["HomeTeam"],index)
            away = getSomeData(veriler,row["AwayTeam"],index)
            newRow = createDictForRow(row,home,away)
            result = result.append(newRow, ignore_index = 1)
        
    result.to_csv("Modified data/modified_" + dataName, index = None)   

if (__name__ == "__main__"):
    createCSV("1819.csv")
   

