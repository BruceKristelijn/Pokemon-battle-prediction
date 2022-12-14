# Import the necessary libraries
from sklearn.model_selection import train_test_split
#Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

import random
import pandas as pd

# Read pokemon
data = pd.read_csv("pokemon_simulation_10k.csv")

# Pre create values
x = []
y = []

for index in data.index:
     series = data.iloc[index]
     winner = [series['winner_level'], series['winner_hp'], series['winner_attack'], series['winner_defense'], series['winner_speed']]
     loser = [series['loser_level'], series['loser_hp'], series['loser_attack'], series['loser_defense'], series['loser_speed']]

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

print(clf.predict([[97, 9000, 0, 0, 0, 0, 98, 0, 0, 0]]))