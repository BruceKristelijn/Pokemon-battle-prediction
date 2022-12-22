# Import Random Forest Model
# Import train_test_split to split tests
# Import scikit-learn metrics module for accuracy calculation
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

import random
import pandas as pd

# Read 10.000 Pokémon battle simulations we ran ourselves earlier
data = pd.read_csv("pokemon_simulation_10k.csv")

# Create empty x and y variables
x = []
y = []

print(data.shape)

# For loop that goes through all simulations with 10.000 rows with 10 columns
# Split the data, first 5 columns are the winner's stats, last 5 columns are the loser's stats
for index in data.index:
    series = data.iloc[index]
    winner = [
        series["winner_level"],
        series["winner_hp"],
        series["winner_attack"],
        series["winner_defense"],
        series["winner_speed"],
    ]
    loser = [
        series["loser_level"],
        series["loser_hp"],
        series["loser_attack"],
        series["loser_defense"],
        series["loser_speed"],
    ]

    # print([winner, loser])

    # Randomize (we don't want the model to learn that the first 5 columns are the winner's data)
    if random.randint(0, 2) == 1:
        x.append(winner + loser)
        y.append([1, 0])
    else:
        x.append(loser + winner)
        y.append([0, 1])

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3
)  # 70% training and 30% test

# Create classifier
clf = RandomForestClassifier(n_estimators=100)

# Train the model using the training sets
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Balanced precision:", metrics.average_precision_score(y_test, y_pred))

print(clf.predict([[7, 30, 23, 21, 14, 99, 326, 206, 216, 195]]))
