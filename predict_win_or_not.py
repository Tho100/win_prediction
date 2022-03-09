import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
data = pd.read_excel("C:\\users\\HP\\Documents\\Datascience task\\win_prediction.xlsx")

le = preprocessing.LabelEncoder()

inputs = data.drop(['Win'],axis='columns')
target = data['Win']

inputs['kill_n'] = le.fit_transform(inputs['Kill'])
inputs['death_n'] = le.fit_transform(inputs['Death'])

inputs_n = inputs.drop(['Kill','Death'],axis='columns')
inputs_n

from sklearn.naive_bayes import GaussianNB

classifier = GaussianNB()

classifier.fit(inputs_n,target)
classifier.score(inputs_n,target)
classifier.predict([[3,0]]) # Kills = 12, Death = 0, Win = T (True)
