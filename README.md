# Pokemon-battle-prediction
Based on pokemon stats find out which is most likely to win a pokemon battle. A project for the Minor Data Science at the Rotterdam University of Applied Sciences.

## Installation
To install all dependencies for this repository, simply run the following command:

`pip install -r requirements.txt`

## Run model
To train and run the model run the following command:

`python3 pokemon_ml_forest.py`

After training, it will print out a summary of the model's performance. 
This includes:

`accuracy` `precision` `recall`  `f1-score`  `support`

### Generate visuals
Then, it will ask you for some inputs through the terminal:
1. **Set trees amount**: _Define the amount of trees being created by RandomForest._
2. **Create confusion matrix**: _y or n to generate a visual representation of the confusion matrix._
3. **Decision tree visualization**: _y or n to generate a full visualization of the RandomForest tree (file will be quite big)._

### Making predictions
Now you will be able to make predictions using the model via the terminal. 
Set the first pokemon by id or name, then its level. After, do the same for the second pokemon.

For each battle, the following result will be printed out:

`classified winner` `trees amount` `prediction time` `training time`


## Regenerate data tables
The data is already there, but if in any case the data should be regenerated:
- set correct google key in .env
- run: `source .env`
- run: `python test_....py` or `python main.py`
