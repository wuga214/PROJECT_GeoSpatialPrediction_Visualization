'''
Created on 09-22-2015

@author: Wuga
'''
import pandas as pd
def readfile(LOCATION):
    df=pd.read_csv(LOCATION)
    Price_Location_Data=zip(df['Sale_Amount'],df['ADDRESS'])
    df_PLD=pd.DataFrame(data=Price_Location_Data, columns=['Price','Location'])
    return df_PLD