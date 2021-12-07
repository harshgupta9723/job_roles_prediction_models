from trainModel import Model
import os 


model = Model()

# i = "Animal Care.csv"
# for i in os.listdir("data/"):
#     # print(i)
#     if i == "categories.csv":
#         pass
#     else:
#         model.readAndProcessData(f"data/{i}",i.replace(" ", "_").lower())
# model.readAndProcessData(f"data/Animal Care.csv",i.split(".")[0].replace(" ", "_").lower())
model.readAndProcessData("healthcare.csv","healthcare")
