from pathlib import Path

import pandas as pd
import  os
def preprocess(df,region_df):
    # filtering for summer olympics
    df = df[df['Season'] == 'Summer']
    # merge with region_df
    df = df.merge(region_df, on='NOC', how='left')
    # dropping duplicates
    df.drop_duplicates(inplace=True)
    # one hot encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df




def dataset():
    BASE_DIR = Path(__file__).resolve().parent.parent

    print(f"BASE  : {BASE_DIR}")
    df = pd.read_csv(f'{BASE_DIR}/bll/athlete_events.csv')
    region_df = pd.read_csv(f'{BASE_DIR}/bll/noc_regions.csv')

    df = preprocess(df, region_df)
    return df
























# 1
# def save_to_json(df, filename):
#     df.to_json(filename, orient='records', lines=True)
#
#
#
# def save_to_csv(df, filename):
#     df.to_csv(filename, index=False)