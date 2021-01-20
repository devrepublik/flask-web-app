# Importing the libraries
import pandas as pd
import pickle

dataset = pd.read_csv('hiring.csv')

print(dataset)

X = dataset.iloc[:, :3]
y = dataset.iloc[:, -1]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)


y_pred = regressor.predict(X)
print(f"R^2-score: {r2_score(y, y_pred)*100:.2f}%")


# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))


'''
# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2, 9, 6]]))
'''