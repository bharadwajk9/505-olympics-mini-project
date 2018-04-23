import pandas as pd


def load_data():
#load csv as dataframe, skip first row
    olympics_df3 = pd.read_csv('https://raw.githubusercontent.com/commit-live-students/505-olympics-mini-project/master/files/olympics.csv',skiprows=1)

#Rename 01, 02, 03 as Gold, Silver, Bronze
    olympics_df3.rename(columns={'01 !':'Gold', '02 !':'Silver', '03 !':'Bronze',
                             '01 !.1':'Gold', '02 !.1':'Silver', '03 !.1':'Bronze',
                             '01 !.2':'Gold', '02 !.2':'Silver', '03 !.2':'Bronze'},inplace=True)
    country_names = [x.split('(')[0] for x in olympics_df3.iloc[:,0]]
    
    olympics_df3.set_index(pd.Series(country_names), inplace=True)
    olympics_df3.drop(['Unnamed: 0'],axis=1, inplace= True)
    olympics_df3.drop(['Totals'],axis=0, inplace= True)
    return olympics_df3


def first_country(df):
    return olympics_df3.iloc[0:1]


def gold_medal(df):
    return olympics_df3.iloc[:, [1]].idxmax()[0]


def biggest_difference_in_gold_medal(df):
   return (olympics_df3.iloc[:, [1]]-olympics_df3.iloc[:, [6]]).abs().idxmax()[0]

def get_points(df):
    olympics_df3.columns.values[-4] = 'Gold_Total'
    olympics_df3.columns.values[-3] = 'Silver_Total'
    olympics_df3.columns.values[-2] = 'Bronze_Total'
    olympics_df3['Points']=olympics_df3.loc[:,'Gold_Total']*3+olympics_df3.loc[:,'Silver_Total']*2+olympics_df3.loc[:,'Bronze_Total']
    return olympics_df3['Points']


# df = load_data()
# print(first_country(df)["# Summer"])
# print(gold_medal(df))
# print(biggest_difference_in_gold_medal(df))
# print(get_points(df))
