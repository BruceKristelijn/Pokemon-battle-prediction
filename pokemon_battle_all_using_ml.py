# Import the necessary libraries
from sklearn.model_selection import train_test_split
# Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier
# Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Import Pokemon classes
from pokemon.pokemon import get_pokemon
from pokemon.pokemontype import get_typetable
from pokemon.battle import battle

import random
import pandas as pd

import csv

# Get mewtwo

allpokemon = get_pokemon()
results = []

# arr of type id's
types = get_typetable().columns.tolist()

# Read pokemon
data = pd.read_csv("pokemon_simulation.csv")

# Pre create values
x = []
y = []

for index in data.index:
     series = data.iloc[index]
     winner = [series['winner_level'], series['winner_hp'], series['winner_attack'], series['winner_defense'], series['winner_speed'], types.index(series['winner_type'])]
     loser = [series['loser_level'], series['loser_hp'], series['loser_attack'], series['loser_defense'], series['loser_speed'], types.index(series['loser_type'])]

     # print([winner, loser])

     # Randomize
     if(random.randint(0, 2) == 1):
          x.append(winner + loser)
          y.append([1,0])
     else:
          x.append(loser + winner)
          y.append([0,1])

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3) # 70% training and 30% test

#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# simulate

print("Simulating all pokemon, length: " + str(len(allpokemon) * len(allpokemon)))

for pokemon in allpokemon:
    print("Simulating " + pokemon.Name + " [" + str(pokemon.Number) + "]")

    wins = 0
    for enemypokemon in allpokemon:
        if(enemypokemon != pokemon):
            result = clf.predict([[pokemon.Level, pokemon.get_hp(), pokemon.get_attack(), pokemon.get_defense(), pokemon.get_speed(), types.index(pokemon.Type1), 
                         enemypokemon.Level, enemypokemon.get_hp(), enemypokemon.get_attack(), enemypokemon.get_defense(), enemypokemon.get_speed(), types.index(enemypokemon.Type1) ]])     
            # Add if first wins or no
            wins += result[0][0]
    results.append({'wins': wins, 'info': pokemon})
    print("Done, " + pokemon.Name +" wins: " + str(wins) + ". Left: " + str(len(allpokemon) - pokemon.Number))

# export results
with open('pokemon_battle_all.csv', 'w') as file:
    writer = csv.writer(file)

    writer.writerow(['number', 'name', 'wins', 'type', 'attack'])

    for result in results:
        writer.writerow([
            result['info'].Number, 
            result['info'].Name, 
            result['wins'],
            result['info'].Type1,
            result['info'].source.Attack,
        ])