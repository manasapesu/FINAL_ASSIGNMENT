# Accuracy : 0.9972924505081051

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("dataset\\Australia.csv") # dataset of all 49 cities

data = data.fillna(0)

direction = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']
wind_dir={}
s=0
for i in direction:
    wind_dir[i]=s
    s+=22.5
    
rain = {'No':0,'Yes':1}

data = data.replace({'WindGustDir':wind_dir,'WindDir9am':wind_dir,'WindDir3pm':wind_dir,'RainToday':rain,'RainTomorrow':rain})

train , test = train_test_split(data, test_size = 0.2)

train_feat = train.iloc[:,lambda train:range(2,23)]
train_targ = train['RainTomorrow']
test_feat = test.iloc[:,lambda test:range(2,23)]
test_targ = test['RainTomorrow']

lr = LogisticRegression()
lr.fit(train_feat, train_targ)

#pred = lr.predict(test_feat)
print('Accuracy on test set: ',lr.score(test_feat, test_targ))

'''
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(test_targ, pred)
print(confusion_matrix)
'''