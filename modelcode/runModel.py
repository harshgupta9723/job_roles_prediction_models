from sklearn.svm import SVC
# Binary Relevance
from sklearn.multiclass import OneVsRestClassifier
from sklearn.neighbors import KNeighborsClassifier
# Performance metric
from sklearn.metrics import f1_score
import pickle
from sklearn.linear_model import SGDClassifier

from trainModel import Model

model = Model()

"""
Please change you function according to this

def cateogoryName(x,y, folder_name, category):
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(estimator=XGBClassifier(gamma =0.2,max_depth = 4,min_child_weight=1,learning_rate=0.05,eval_metric='mlogloss',use_label_encoder =False))
    classifier.fit(x, y)
    print("################## Model building end #################\n")

    # saving the model 
    # make folder if not exist    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))

def modelCategory():
    # preprocess text 
    x,y,category = model.readAndProcessData("Healthcare.csv","healthcare")

    health(x,y, category, category)
    """
def healthcare(x,y, folder_name, category):
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(estimator=SGDClassifier(loss = 'hinge' ,alpha = 0.001,penalty = 'none' ))
    # classifier = OneVsRestClassifier(estimator=XGBClassifier(gamma =0.2,max_depth = 4,min_child_weight=1,learning_rate=0.05,eval_metric='mlogloss',use_label_encoder =False))
    classifier.fit(x, y)
    print("################## Model building end #################\n")

    # saving the model 
    # make folder if not exist    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))

def modelhealth():
    # preprocess text 
    x,y,category = model.readAndProcessData("Healthcare.csv","healthcare")

    healthcare(x,y, category, category)

    
def restaurant_hospitality(x,y, folder_name, category):
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(estimator=SGDClassifier(loss = 'modified_huber' ,alpha = 0.0001,penalty = 'l1' ))

    classifier.fit(x, y)
    print("################## Model building end #################\n")

    # saving the model 
    # make folder if not exist    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))

def model_restaurant_hospitality():
    # preprocess text 
    x,y,category = model.readAndProcessData("restaurant_and_hospitality.csv","restaurant_and_hospitality")

    restaurant_hospitality(x,y, category, category)


def computer(x, y, folder_name, category):
    
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(estimator=SGDClassifier(alpha = 0.0001, eta0= 0.5, learning_rate = 'optimal', loss = 'hinge', penalty = 'l1'))
    classifier.fit(x, y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))


def modelComputer():
    # preprocess text 
    x, y, category = model.readAndProcessData("computer_and_it.csv",  "computer_and_it")

    computer(x, y, category, category)


def education(x, y, folder_name, category):
    
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(SGDClassifier(alpha = 0.0001, eta0= 10, learning_rate = 'adaptive', loss = 'modified_huber', penalty = 'l1'))
    classifier.fit(x, y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))


def modelEducation():
    # preprocess text 
    x, y, category = model.readAndProcessData("Education.csv", "education")

    education(x, y, category, category) 


def customer_service(x, y, folder_name, category):
    
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(SGDClassifier(alpha = 0.0001, eta0= 10, learning_rate = 'constant', loss = 'modified_huber', penalty = 'l1'))
    classifier.fit(x, y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))


def modelCustomer():
    # preprocess text 
    x,y,category = model.readAndProcessData("customer_service.csv", "customer_service")

    customer_service(x, y, category, category)  
    
    
def sales(x,y, folder_name, category):
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(estimator=SGDClassifier(loss = 'modified_huber' ,alpha = 0.01,penalty = 'none' ))
    classifier.fit(x, y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))
    

def modelSales():
    # preprocess text 
    x, y, category = model.readAndProcessData("sales_and_retail.csv", "sales_and_retail")
    sales(x, y, category, category)



def manufacturing_and_warehouse(x,y, folder_name, category):
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(estimator=SGDClassifier(alpha = 0.0001, eta0= 10, learning_rate = 'adaptive', loss = 'modified_huber', penalty = 'l1'))
    classifier.fit(x, y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))
    

def modelManufacturing():
    # preprocess text 
    x, y, category = model.readAndProcessData("manufacturing_and_warehouse.csv", "manufacturing_and_warehouse")

    manufacturing_and_warehouse(x, y, category, category)


def cleaning_and_facilities(x,y, folder_name, category):
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(estimator=SGDClassifier(loss = 'hinge' ,alpha = 0.0001,penalty = 'none' ))
    classifier.fit(x, y)
    print("################## Model building end #################\n")

    # saving the model 
    # make folder if not exist    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))

def model_cleaning_and_facilities():
    # preprocess text 
    x,y,category = model.readAndProcessData("cleaning_and_facilities.csv","cleaning_and_facilities")

    cleaning_and_facilities(x,y, category, category)

    
def account_and_finance(x,y, folder_name, category):
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(estimator=SGDClassifier(loss = 'hinge' ,alpha = 0.0001,penalty = 'l1' ))
    classifier.fit(x, y)
    print("################## Model building end #################\n")

    # saving the model 
    # make folder if not exist    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))

def model_account_and_financial():
    # preprocess text 
    x,y,category = model.readAndProcessData("account_and_financial.csv","account_and_financial")

    account_and_finance(x,y, category, category)


def media_communication(x,y, folder_name, category):
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(estimator=SGDClassifier(loss = 'modified_huber' ,alpha = 0.01,penalty = 'none' ))
    classifier.fit(x, y)
    print("################## Model building end #################\n")

    # saving the model 
    # make folder if not exist    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))

def model_media_communication():
    # preprocess text 
    x,y,category = model.readAndProcessData("media_communications.csv","media_communications")

    media_communication(x,y, category, category)

def advertising(x,y, folder_name, category):
    print("################## Model building started #################\n")
    sgd_clf = OneVsRestClassifier(estimator=SGDClassifier(eta0 = 1, loss = 'hinge', penalty = 'l1'))
    sgd_clf.fit(x,y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    #   
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(sgd_clf, open(f'models/{folder_name}/{category}.sav', 'wb'))
        
def model_advertising_and_marketing():
    # preprocess text 
    x,y, category = model.readAndProcessData("advertising_and_marketing.csv", 
                                                                        "advertising_and_marketing")

    advertising(x,y, category, category)


# modelEducation()
# model_media_communication()
model_advertising_and_marketing()
    

