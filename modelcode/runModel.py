
from sklearn.svm import SVC
# Binary Relevance
from sklearn.multiclass import OneVsRestClassifier
# Performance metric
from sklearn.metrics import f1_score
import pickle
from sklearn.neighbors import KNeighborsClassifier

from trainModel import Model

model = Model()

def cleaning_facility(xtrain, xtest, ytrain, ytest, folder_name, category):
    print("################## Model building started #################\n")
    classifier = KNeighborsClassifier(n_neighbors = 5, weights = 'distance',algorithm = 'brute',metric = 'minkowski')

    classifier.fit(xtrain, ytrain)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))
    loaded_model = pickle.load(open(filename, 'rb'))

    print("################## Making prediction #################\n")
    svm_pred = classifier.predict(xtest)
    # evaluate performance
    print(f1_score(ytest, svm_pred, average="micro"))
        


def modelcleaning_facility():
    # preprocess text 
    xtrain, xtest, ytrain, ytest , category = model.readAndProcessData("cleaning_and_facilities.csv", 
                                                                        "cleaning_and_facilities")

    cleaning_facility(xtrain, xtest, ytrain, ytest, category, category)


modelcleaning_facility()