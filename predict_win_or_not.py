import pandas as pd 

data = pd.read_excel("C:\\users\\HP\\Documents\\datascience task\\win_prediction.xlsx")
x = data[['Kill','Death']].values
y = data[['Won']].values

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=.11)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(x,y)

y_predicted = model.predict(x_test)
