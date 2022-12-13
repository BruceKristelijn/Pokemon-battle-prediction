import pandas as pd
from sklearn.linear_model import LogisticRegression

# load the data from the CSV file
df = pd.read_csv('pokemon_simulation_10k.csv')

# create a list of the features we want to use
features = ['winner_level', 'winner_hp', 'winner_attack', 'winner_defense', 'winner_speed',
            'loser_level', 'loser_hp', 'loser_attack', 'loser_defense', 'loser_speed']

# create the X and y arrays from the dataframe
X = df[features]
y = df['winner_level']

# create a logistic regression model and fit it to the data
model = LogisticRegression()
model.fit(X, y)

# make predictions on new data
new_data = [[100, 100, 100, 100, 100, 50, 50, 50, 50, 50]]
predictions = model.predict(new_data)

# print the predictions
print(predictions)