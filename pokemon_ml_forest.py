# Import the necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from timeit import default_timer as timer

# Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier

# Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# Import Pokemon classes
from pokemon.pokemon import get_pokemon
from pokemon.pokemontype import get_typetable

import random
import pandas as pd

# arr of type id's
types = get_typetable().columns.tolist()

# Read pokemon
data = pd.read_csv("pokemon_simulation.csv")

# Pre create values
x = []
y = []

for index in data.index:
    series = data.iloc[index]
    winner = [
        series["winner_level"],
        series["winner_hp"],
        series["winner_attack"],
        series["winner_defense"],
        series["winner_speed"],
        types.index(series["winner_type"]),
    ]
    loser = [
        series["loser_level"],
        series["loser_hp"],
        series["loser_attack"],
        series["loser_defense"],
        series["loser_speed"],
        types.index(series["loser_type"]),
    ]

    # print([winner, loser])

    # Randomize
    if random.choice([True, False]):
        x.append(winner + loser)
        y.append(0)
    else:
        x.append(loser + winner)
        y.append(1)

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3
)  # 70% training and 30% test

forest_amount = 200
# Create a RF Classifier, 100 seems to be the sweet spot.
training_start = timer()
clf = RandomForestClassifier(n_estimators=forest_amount)
training_end = timer()
# Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print(f"Amount of trees generated: {forest_amount}")
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print(metrics.classification_report(y_test, y_pred))

# PRUNING (not really worth it)
# important_features = clf.feature_importances_
# X_important = X_train[:, important_features > 0]
#
# pruned_model = RandomForestClassifier(n_estimators=forest_amount)
# pruned_model.fit(X_important, y_train)
#
# y_prune_pred = clf.predict(X_test)
#
# # Prune Model Accuracy, how often is the classifier correct?
# print(f"Amount of trees generated: {forest_amount}")
# print("Accuracy:", metrics.accuracy_score(y_test, y_prune_pred))
# print(metrics.classification_report(y_test, y_prune_pred))
#
# breakpoint()


print("\nGenerate confusion matrix plot? (type 'y' or 'n')")
if "y" in input().lower():
    matrix = metrics.confusion_matrix(y_test, y_pred)
    matrix = matrix.astype("float") / matrix.sum(axis=1)[:, np.newaxis]

    # Build the plot
    plt.figure(figsize=(16, 7))
    sns.set(font_scale=1.5)
    sns.heatmap(
        matrix, annot=True, annot_kws={"size": 10}, cmap=plt.cm.Greens, linewidths=0.6
    )

    # Add labels to the plot
    class_names = ["positive", "negative"]
    tick_marks = np.arange(len(class_names))
    tick_marks2 = tick_marks + 0.5
    plt.xticks(tick_marks, class_names, rotation=25, ha="center")
    plt.yticks(tick_marks2, class_names, rotation=0)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix for Random Forest Pokemon Model")
    plt.show()

print("\nGenerate decision tree visualization? (type 'y' or 'n')")
if "y" in input().lower():
    from sklearn.tree import export_graphviz

    # Export as dot file
    export_graphviz(
        clf.estimators_[5],
        out_file="tree.dot",
        feature_names=data.columns.tolist(),
        class_names=types,
        rounded=True,
        precision=2,
        filled=True,
    )

    # Convert to png using system command (requires Graphviz)
    from subprocess import call

    call(["dot", "-Tpng", "tree.dot", "-o", "tree.png", "-Gdpi=600"])

    # Display in jupyter notebook
    from IPython.display import Image

    Image(filename="tree.png")

while True:
    print("Give first Pokemon name or id:")
    pokemonName1 = input()
    if pokemonName1.isnumeric():
        pokemonName1 = int(pokemonName1)
    try:
        level1 = int(input("Please enter the Pokemon level: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        # better try again... Return to the start of the loop
        continue

    print("Give second Pokemon name or id:")
    pokemonName2 = input()
    if pokemonName2.isnumeric():
        pokemonName2 = int(pokemonName2)
    try:
        level2 = int(input("Please enter the Pokemon level: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        # better try again... Return to the start of the loop
        continue

    pokemon1 = get_pokemon(pokemonName1)
    pokemon1.setLevel(level1)

    pokemon2 = get_pokemon(pokemonName2)
    pokemon2.setLevel(level2)

    start = timer()
    winner = clf.predict(
            [
                [
                    pokemon1.Level,
                    pokemon1.get_hp(),
                    pokemon1.get_attack(),
                    pokemon1.get_defense(),
                    pokemon1.get_speed(),
                    types.index(pokemon1.Type1),
                    pokemon2.Level,
                    pokemon2.get_hp(),
                    pokemon2.get_attack(),
                    pokemon2.get_defense(),
                    pokemon2.get_speed(),
                    types.index(pokemon2.Type1),
                ]
            ]
        )
    end = timer()

    print("Result")
    print("winner: ", f"pokemon {winner[0] + 1}")
    print('trees amount: ', forest_amount)
    print('prediction time: ', round(end - start, 6))
    print('training time: ', round(training_end - training_start, 6))
    print("----")
