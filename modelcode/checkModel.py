"""
    this file is responsible for train the particular categroy
"""
from trainModel import Model
import os 

# create object for the model class
model = Model()

# if we want to train more then one model 
# 
for i in os.listdir("data/"):
    # print(i)
    if i == "categories.csv":
        pass
    else:
        model.readAndProcessData(f"data/{i}",i.replace(" ", "_").lower())

# if we want to train only one model
model.readAndProcessData("filepath.csv","category")
