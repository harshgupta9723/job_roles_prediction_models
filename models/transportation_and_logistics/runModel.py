
from sklearn.svm import SVC
# Binary Relevance
from sklearn.multiclass import OneVsRestClassifier
from sklearn.neighbors import KNeighborsClassifier
# Performance metric
from sklearn.metrics import f1_score
import pickle
import xgboost as xgb
from trainModel import Model
from sklearn.linear_model import SGDClassifier

model = Model()

def advertising(xtrain, xtest, ytrain, ytest, folder_name, category):
    print("################## Model building started #################\n")
    sgd_clf = OneVsRestClassifier(estimator=SGDClassifier(eta0 = 1, loss = 'hinge', penalty = 'l1'))
    sgd_clf.fit(xtrain, ytrain)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(sgd_clf, open(f'models/{folder_name}/{category}.sav', 'wb'))
    loaded_model = pickle.load(open(filename, 'rb'))

    print("################## Making prediction #################\n")
    svm_pred = _clf.predict(xtest)
    # evaluate performance
    print(f1_score(ytest, svm_pred, average="micro"))
        
def sales_and_retail(xtrain, xtest, ytrain, ytest, folder_name, category):
    pass

def advertising_and_marketing():
    # preprocess text 
    xtrain, xtest, ytrain, ytest , category = model.readAndProcessData("advertising_and_marketing.csv", 
                                                                        "advertising_and_marketing")

    advertising(xtrain, xtest, ytrain, ytest, category, category)


advertising_and_marketing()