import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


df = pd.read_csv("car_data.csv", delimiter=";")

df = df.dropna()
#print(df)

y = df['Selling_Price(euro)']
X =df.iloc[:, 1:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=6)
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)

model =LinearRegression ()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print(f'MSE {mse:.2f}')
print(f'R2 {r2:.2f}')