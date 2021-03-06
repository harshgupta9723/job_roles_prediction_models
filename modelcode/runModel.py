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
    classifier = OneVsRestClassifier(estimator=SGDClassifier(loss = 'squared_hinge' ,alpha = 0.001,penalty = 'none' ))
    # classifier = OneVsRestClassifier(estimator=XGBClassifier(gamma =0.2,max_depth = 4,min_child_weight=1,learning_rate=0.05,eval_metric='mlogloss',use_label_encoder =False))
    classifier.fit(x, y)
    print("################## Model building end #################\n")

    # saving the model 
    # make folder if not exist    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))

def modelhealth():
    # preprocess text 
    # taking csv data as input
    x,y,category = model.readAndProcessData("Healthcare.csv","healthcare")

    healthcare(x,y, category, category)

    
def restaurant_hospitality(x,y, folder_name, category):
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(estimator=SGDClassifier(loss = 'modified_huber' ,alpha = 0.01,penalty = 'none' ))

    classifier.fit(x, y)
    print("################## Model building end #################\n")

    # saving the model 
    # make folder if not exist    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))

def model_restaurant_hospitality():
    # preprocess text 
    # taking csv as input
    x,y,category = model.readAndProcessData("Restaurant and Hospitality.csv","restaurant_and_hospitality")

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
    classifier = OneVsRestClassifier(estimator=SGDClassifier(alpha = 0.0001, eta0 = 1,learning_rate = 'optimal', loss = 'modified_huber', penalty = 'l1'))
    classifier.fit(x, y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist

    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))
    

def modelSales():
    # preprocess text 
    x, y, category = model.readAndProcessData("Sales and Retail.csv", "sales_and_retail")
    sales(x, y, category, category)


def manufacturing_and_warehouse(x,y, folder_name, category):
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(estimator=SGDClassifier(loss = 'squared_hinge',alpha  = 0.001,penalty = 'none'))
    classifier.fit(x, y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))
    

def modelManufacturing():
    # preprocess text 
    x, y, category = model.readAndProcessData("Manufacturing and Warehouse.csv", "manufacturing_and_warehouse")

    manufacturing_and_warehouse(x, y, category, category)


def cleaning_and_facilities(x,y, folder_name, category):
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(estimator=SGDClassifier(loss = 'modified_huber' ,alpha = 0.001,penalty = 'none' ))
    classifier.fit(x, y)
    print("################## Model building end #################\n")

    # saving the model 
    # make folder if not exist    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))

def model_cleaning_and_facilities():
    # preprocess text 
    x,y,category = model.readAndProcessData("Cleaning and Facilities .csv","cleaning_and_facilities")

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
    classifier = OneVsRestClassifier(estimator=SGDClassifier(loss ='modified_huber',alpha  = 0.001,penalty = 'none' ))
    classifier.fit(x, y)
    print("################## Model building end #################\n")

    # saving the model 
    # make folder if not exist    
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))

def model_media_communication():
    # preprocess text 
    x,y,category = model.readAndProcessData("Media, Communications and Writing.csv","media_communications_and_writing")

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


def scienceAndEngineering(x,y, folder_name, category):
    print("################## Model building started #################\n")
    sgd_clf = OneVsRestClassifier(estimator=SGDClassifier(loss = 'hinge',alpha=0.0001, penalty = 'l1'))
    sgd_clf.fit(x,y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    #   
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(sgd_clf, open(f'models/{folder_name}/{category}.sav', 'wb'))
        
def modelScienceAndEngineering():
    # preprocess text 
    x,y, category = model.readAndProcessData("Science and Engineering.csv", 
                                                                        "science_and_engineering")

    advertising(x,y, category, category)


def admin_office(x,y, folder_name, category):
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(estimator=SGDClassifier(loss ='hinge', alpha  = 0.001, penalty = 'none' ))
    classifier.fit(x, y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist    

    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))

def model_admin_office():
    # preprocess text 
    x,y,category = model.readAndProcessData("Admin and Office.csv","admin_and_office")

    admin_office(x,y, category, category)


# Science and Engineering
def sportAndFitness(x,y, folder_name, category):
    print("################## Model building started #################\n")
    sgd_clf = OneVsRestClassifier(estimator=SGDClassifier(loss = 'hinge',alpha  = 0.0001,penalty = 'none'))
    sgd_clf.fit(x,y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    #   
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(sgd_clf, open(f'models/{folder_name}/{category}.sav', 'wb'))
        
def modelsportAndFitness():
    # preprocess text 
    x,y, category = model.readAndProcessData("/home/himanshu/Downloads/Sports Fitness and Recreation.csv", 
                                                                        "sports_fitness_and_recreation")

    sportAndFitness(x,y, category, category)


# Energy and Mining
def energyAndMining(x,y, folder_name, category):
    print("################## Model building started #################\n")
    sgd_clf = OneVsRestClassifier(estimator=SGDClassifier(loss = "hinge",alpha  = 0.0001,penalty = "l2"))
    sgd_clf.fit(x,y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    #   
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(sgd_clf, open(f'models/{folder_name}/{category}.sav', 'wb'))
        
def modelEneryAndMining():
    # preprocess text 
    x,y, category = model.readAndProcessData("/home/himanshu/Downloads/Energy and Mining.csv", 
                                                                        "energy_and_mining")

    energyAndMining(x,y, category, category)


def business_operation(x,y, folder_name, category):
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(estimator=SGDClassifier(loss ='squared_hinge',alpha  = 0.001,penalty = 'none' ))
    classifier.fit(x, y)
    print("################## Model building end #################\n")

    # saving the model
    # make folder if not exist
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))


def model_business_operation():
    # preprocess text
    x,y,category = model.readAndProcessData("Business Operations.csv","Business Operations")

    business_operation(x,y, category, category)

def installation_maintenance(x,y, folder_name, category):
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(estimator=SGDClassifier(loss ='modified_huber',alpha  = 0.001,penalty = 'none' ))
    classifier.fit(x, y)
    print("################## Model building end #################\n")

    # saving the model
    # make folder if not exist
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))


def model_installation_maintenance():
    # preprocess text
    x,y,category = model.readAndProcessData("Installation, Maintenance and Repair.csv","installation_maintenance_and_repair")

    business_operation(x,y, category, category)

# Human Resources
def humanResources(x,y, folder_name, category):
    print("################## Model building started #################\n")
    sgd_clf = OneVsRestClassifier(estimator=SGDClassifier(loss = "hinge",alpha  = 0.0001,penalty = "l2"))
    sgd_clf.fit(x,y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    #   
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(sgd_clf, open(f'models/{folder_name}/{category}.sav', 'wb'))
        
def modelHumanResources():
    # preprocess text 
    x,y, category = model.readAndProcessData("/home/himanshu/Downloads/Human Resources.csv", 
                                                                        "human_resources")

    humanResources(x,y, category, category)


def management(x,y, folder_name, category):
    print("################## Model building started #################\n")
    sgd_clf = OneVsRestClassifier(estimator=SGDClassifier(eta0 = 3, loss = 'hinge', penalty = 'l1'))
    sgd_clf.fit(x,y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    #   
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(sgd_clf, open(f'models/{folder_name}/{category}.sav', 'wb'))
        
def model_management():
    # preprocess text 
    x,y, category = model.readAndProcessData("Management.csv", 
                                                                        "management")

    management(x,y, category, category)

def entertainment_and_travel(x,y, folder_name, category):
    print("################## Model building started #################\n")
    sgd_clf = OneVsRestClassifier(estimator=SGDClassifier(eta0 = 2, loss = 'hinge', penalty = 'l1'))
    sgd_clf.fit(x,y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    #   
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(sgd_clf, open(f'models/{folder_name}/{category}.sav', 'wb'))
        
def model_entertainment_and_travel():
    # preprocess text 
    x,y, category = model.readAndProcessData("Entertainment and Travel.csv", 
                                                                        "entertainment_and_travel")

    entertainment_and_travel(x,y, category, category)

def property(x,y, folder_name, category):
    print("################## Model building started #################\n")
    sgd_clf = OneVsRestClassifier(estimator=SGDClassifier(eta0 = 3, loss = 'hinge', penalty = 'l1'))
    sgd_clf.fit(x,y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    #   
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(sgd_clf, open(f'models/{folder_name}/{category}.sav', 'wb'))
        
def model_property():
    # preprocess text 
    x,y, category = model.readAndProcessData("Property.csv", 
                                                                        "property")

    property(x,y, category, category)

def social_services_and_non_profit(x,y, folder_name, category):
    print("################## Model building started #################\n")
    sgd_clf = OneVsRestClassifier(estimator=SGDClassifier(alpha = 0.0001, eta0= 10, penalty = 'l1'))
    sgd_clf.fit(x,y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    #   
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(sgd_clf, open(f'models/{folder_name}/{category}.sav', 'wb'))
        
def model_social_services_and_non_profit():
    # preprocess text 
    x,y, category = model.readAndProcessData("Social_Services_and_Non_Profit.csv", 
                                                                        "social_services_and_non_profit")

    social_services_and_non_profit(x,y, category, category)


def animal_care(x,y, folder_name, category):
    print("################## Model building started #################\n")
    sgd_clf = OneVsRestClassifier(estimator=SGDClassifier(loss = "modified_huber",alpha  = 0.01,penalty = "none"))
    sgd_clf.fit(x,y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    #   
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(sgd_clf, open(f'models/{folder_name}/{category}.sav', 'wb'))
        
def model_animal_care():
    # preprocess text 
    x,y, category = model.readAndProcessData("Animal Care.csv","animal_care")

    animal_care(x,y, category, category)


def art_fashion(x,y, folder_name, category):
    print("################## Model building started #################\n")
    sgd_clf = OneVsRestClassifier(estimator=SGDClassifier(alpha  = 0.0001,penalty = "elasticnet", eta0 = 1))
    sgd_clf.fit(x,y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
 
    pickle.dump(sgd_clf, open(f'models/{folder_name}/{category}.sav', 'wb'))
        
def model_art_fashion():
    # preprocess text 
    x,y, category = model.readAndProcessData("Art, Fashion and Design.csv","art_fashion_and_design")

    art_fashion(x,y, category, category)


def protective_services(x,y, folder_name, category):
    print("################## Model building started #################\n")
    classifier = OneVsRestClassifier(estimator=SGDClassifier(alpha = 0.0001, eta0 = 10,learning_rate = 'optimal', loss = 'modified_huber', penalty = 'l1'))
    classifier.fit(x, y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    pickle.dump(classifier, open(f'models/{folder_name}/{category}.sav', 'wb'))
    

def modelProtective():
    # preprocess text 
    x, y, category = model.readAndProcessData("Protective Services.csv", "protective_services")
    protective_services(x, y, category, category)


def farming_and_outdoor(x,y, folder_name, category):
    print("################## Model building started #################\n")
    sgd_clf = OneVsRestClassifier(estimator=SGDClassifier(eta0 = 4, loss = 'hinge', penalty = 'l1'))
    sgd_clf.fit(x,y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist
    #   
    filename = f'models/{folder_name}/{category}.sav'
    pickle.dump(sgd_clf, open(f'models/{folder_name}/{category}.sav', 'wb'))
        
def model_farming_and_outdoor():
    # preprocess text 
    x,y, category = model.readAndProcessData("Farming and Outdoors.csv","farming_and_outdoor")

    farming_and_outdoor(x,y, category, category)


def construction(x,y, folder_name, category):
    print("################## Model building started #################\n")
    sgd_clf = OneVsRestClassifier(estimator=SGDClassifier(alpha = 0.0001, eta0= 0.5, penalty = 'elasticnet'))
    sgd_clf.fit(x,y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist

    pickle.dump(sgd_clf, open(f'models/{folder_name}/{category}.sav', 'wb'))
        
def model_construction():
    # preprocess text 
    x,y, category = model.readAndProcessData("Construction.csv","construction")

    construction(x,y, category, category)


def transportation(x,y, folder_name, category):
    print("################## Model building started #################\n")
    sgd_clf = OneVsRestClassifier(estimator=SGDClassifier(alpha = 0.0001, eta0= 0.1,learning_rate = 'optimal',loss = 'modified_huber', penalty = 'l1'))
    sgd_clf.fit(x,y)
    print("################## Model building end #################\n")
    # saving the model 
    # make folder if not exist

    pickle.dump(sgd_clf, open(f'models/{folder_name}/{category}.sav', 'wb'))


def modelTransportation():
    # preprocess text 
    x,y, category = model.readAndProcessData("Transportation and Logistics.csv", "transportation_and_logistics")

    transportation(x,y, category, category)