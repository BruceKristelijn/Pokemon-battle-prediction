# # Import the necessary libraries
# from sklearn.ensemble import RandomForestClassifier

# # Define the input data
# # In this example, we have two Pokemon with the following stats:
# # - Pokemon 1: level 10, attack 10, defense 10, speed 10
# # - Pokemon 2: level 15, attack 15, defense 15, speed 15
# x = [[10, 10, 10, 10],
#      [15, 15, 15, 15]]

# # Define the output data
# # In this example, we have simulated the battle between the two Pokemon and
# # determined that Pokemon 1 wins
# y = [1, 0]

# # Create the random forest model
# model = RandomForestClassifier()

# # Train the model on the input and output data
# model.fit(x, y)

# # Use the trained model to make predictions about the outcome of future battles
# # For example, if we have a new Pokemon with the following stats:
# # - Pokemon 3: level 12, attack 12, defense 12, speed 12
# new_pokemon = [[6, 6, 6, 6]]
# prediction = model.predict(new_pokemon)

# # The prediction will be either 1 (if Pokemon 3 wins) or 0 (if Pokemon 3 loses)
# print(prediction)

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# load the data into a pandas dataframe
df = pd.read_csv('pokemon_battles.csv')

# create the features and target variables
X = df[['pokemon1', 'pokemon2', 'level1', 'level2', 'hp1', 'hp2', 'attack1', 'attack2', 'defense1', 'defense2', 'speed1', 'speed2']]
y = df['outcome']

# create and fit the decision tree model
model = DecisionTreeClassifier()
model.fit(X, y)

# make a prediction for a battle
p1 = ['Charmander', 5, 100, 50, 50, 100]
p2 = ['Squirtle', 5, 100, 50, 50, 50]

prediction = model.predict([p1, p2])

# print the result of the battle
if prediction[0] == prediction[1]:
    print("The battle is a tie!")
else:
    winner = prediction[0] if model.predict_proba([p1, p2])[0][0] > 0.5 else prediction[1]
    print(f"{winner} wins the battle!")