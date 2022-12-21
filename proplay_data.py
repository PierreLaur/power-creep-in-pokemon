import sys
import pandas as pd

proplay = pd.DataFrame(columns=["name","proplay_usage"])

def import_data(month) :
    with open("data/proplay/gen8vgc2022-1760_"+month+"22.txt") as data :
        new_data = []
        for line in data :
            if line[1] == "|" :
                new_data.append(line[3:-4].replace(" ","").split("|"))
        df = pd.DataFrame(new_data)
        df.drop(0,inplace=True)
        df.drop([0,2,4,5,6],axis=1,inplace=True)
        df.rename({1:"name",3:"proplay_usage"}, axis=1,inplace=True)
        return df

for month in "01 02 03 04 05 06 07 08 09 10".split() :
    df = import_data(month)
    proplay = pd.concat([proplay, df])

proplay['proplay_usage'] = proplay["proplay_usage"].astype(int)
proplay = proplay.sort_values(by=["name"]).groupby("name").sum()

proplay.to_csv('data/proplay.csv')

