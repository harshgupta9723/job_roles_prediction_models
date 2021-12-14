
from sklearn.svm import SVC
# Binary Relevance
from sklearn.multiclass import OneVsRestClassifier
# Performance metric
from sklearn.metrics import f1_score
import pickle

from trainModel import Model

model = Model()

def health(xtrain, xtest, ytrain, ytest, folder_name, category):
    print("################## Model building started #################\n")
    svc = SVC( kernel='rbf', C=1e9, gamma=1e-07)
    # svc = KNeighborsClassifier(n_neighbors = 5, weights = 'distance',algorithm = 'brute',metric = 'minkowski')
    svm_clf = OneVsRestClassifier(svc)
    svm_clf.fit(xtrain, ytrain)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(svm_clf, open(f'models/{folder_name}/{category}.sav', 'wb'))
    loaded_model = pickle.load(open(filename, 'rb'))

    print("################## Making prediction #################\n")
    svm_pred = svm_clf.predict(xtest)
    # evaluate performance
    print(f1_score(ytest, svm_pred, average="micro"))
        


def modelHealth():
    # preprocess text 
    xtrain, xtest, ytrain, ytest , category = model.readAndProcessData("Healthcare.csv", 
                                                                        "Healthcare")

    health(xtrain, xtest, ytrain, ytest, category, category)


modelHealth()