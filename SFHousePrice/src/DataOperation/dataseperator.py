'''
Created on Sep 29, 2015

@author: Wuga
'''
import numpy as np
#import DataOperation as DO
import pandas as pd

def dataseperator(df):
    perm=np.random.permutation(range(1, len(df)))
    training_index=perm[:(len(df)-1)/2]
    testing_index=perm[(len(df)-1)/2:len(df)-1]
    house_price=[x.replace(",","") for x in df['Price']]
    house_price=[x[1:] for x in house_price]
    house_price=np.array(house_price)
    house_price=house_price.transpose()
    training_set=zip(house_price[training_index],df['Latitude'][training_index],df['Longitude'][training_index])
    training_df=pd.DataFrame(data=training_set,columns=['Price','Latitude','Longitude'])
    testing_set=zip(house_price[testing_index],df['Latitude'][testing_index],df['Longitude'][testing_index])
    testing_df=pd.DataFrame(data=testing_set, columns=['Price','Latitude','Longitude'])
    return (training_df,testing_df,training_index,testing_index)

# LOCATION='/Users/Wuga/Documents/DATA/SFREHPDATA/HousingSales2012PL_GOOGLE.csv'
# df= DO.readgeofile(LOCATION)
# train,test=dataseperator(df)
# print df['Price'][0]
# print df['Price'][0]
# #print train
# #print test
# TRAIN_LOCATION='/Users/Wuga/Documents/DATA/SFREHPDATA/HousingSales2012PL_GOOGLE_TRAIN.csv'
# TEST_LOCATION='/Users/Wuga/Documents/DATA/SFREHPDATA/HousingSales2012PL_GOOGLE_TEST.csv'
# DO.write(train, TRAIN_LOCATION)
# DO.write(test, TEST_LOCATION)
    