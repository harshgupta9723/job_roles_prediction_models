import numpy as np 
import pandas as pd 
import os

import pickle
# load stop words
import nltk
from nltk.corpus import stopwords
stop_word = stopwords.words('english')
from cleantext import clean
import re
from bs4 import BeautifulSoup
# mulitlable encoder
from sklearn.preprocessing import MultiLabelBinarizer

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

# from sklearn.svm import SVC
# from sklearn.neighbors import KNeighborsClassifier
# # Binary Relevance
# from sklearn.multiclass import OneVsRestClassifier
# # Performance metric
# from sklearn.metrics import f1_score


class Model:
    def __init__(self):
        print("Modeling building")


    # txt cleaning
    def textCleaning(self, text):      
                            
        #     bs4
        soup = BeautifulSoup(text, 'lxml')
        text = soup.text
        #     remove urls
        text = re.sub(r'http\S+', " ", text)

        #     remove mentions
        text = re.sub(r'@\w+',' ',text)

        #     remove hastags
        text = re.sub(r'#\w+', ' ', text)
        
        # take alphanumerical
        text = re.sub(r'\W+', ' ', text)

        #     remove digits
        text = re.sub(r'\d+', ' ', text)

        #     remove html tags
        text = re.sub('r<.*?>',' ', text)
        
        #     remove stop words 
        text = text.split()
        text = " ".join([word for word in text if not word in stop_word])    
        
        
        return clean(text,
            fix_unicode=True,               # fix various unicode errors
            to_ascii=True,                  # transliterate to closest ASCII representation
            lower=True,                     # lowercase text
            no_line_breaks=False,           # fully strip line breaks as opposed to only normalizing them
            no_urls=False,                  # replace all URLs with a special token
            no_emails=False,                # replace all email addresses with a special token
            no_phone_numbers=False,         # replace all phone numbers with a special token
            no_numbers=False,               # replace all numbers with a special token
            no_digits=False,                # replace all digits with a special token
            no_currency_symbols=False,      # replace all currency symbols with a special token
            no_punct=False,                 # remove punctuations
            replace_with_punct="",          # instead of removing punctuations you may replace them
            replace_with_url=" ",
            replace_with_email="<EMAIL>",
            replace_with_phone_number="<PHONE>",
            replace_with_number="<NUMBER>",
            replace_with_digit="0",
            replace_with_currency_symbol="<CUR>",
            lang="en"                       # set to 'de' for German special handling
        )

    def readAndProcessData(self, csvpath, categroy):
        
        print("################## Reading data #################\n")
        # read data 
        csv_data = pd.read_csv(csvpath)
        df = csv_data[["job_roles","clean_desc","title"]]
        df = df[df['clean_desc'] != "No Information Found"]
       
        # df['job_roles'] = df['search_query'].apply(lambda x : x.split('jobs')[0])
        # df['clean_desc'] = df['desc'].apply(lambda x: self.textCleaning(x))    
        # print(df['clean_desc'].head())

        # making folder
        folder_name = categroy
        if not os.path.exists(f"models/{folder_name}"):
            os.makedirs(f"models/{folder_name}")
        else:
            pass

        print("################## Encoding started #################\n")
        # encoding y 
        y = df['job_roles']
        y = y.values.reshape(-1,1)
        mlb = MultiLabelBinarizer()
        y_mul = mlb.fit_transform(y)
        all_classes = mlb.classes_

        value = []
        for i in all_classes:
            value.append(i)
        
        pd.DataFrame({"classes": value}).to_csv(f"models/{folder_name}/{categroy}.csv", index=False)

        # encoding x 
        x = df['clean_desc']
        # tfidf_vectorizer = TfidfVectorizer(max_df=10,max_features=100000,min_df=5)
        tfidf_vectorizer = TfidfVectorizer(max_features=5000)
        print(len(x), len(y_mul))
        # split the dataset into training and valid test 
        # xtrain, xval, ytrain, yval = train_test_split(x, y_mul, test_size=0.2, random_state=9)
        # create Tf-IDF features
        xtrain_tfidf = tfidf_vectorizer.fit(x)
        # saving tfidf
        pickle.dump(xtrain_tfidf, open(f"models/{folder_name}/{categroy}_vectorizer.pickle", "wb"))

        xtrain_tfidf = tfidf_vectorizer.transform(x)
        # xval_tfidf = tfidf_vectorizer.transform(xval) 
        print("################## Encoding encoded #################\n")
        # 

        return xtrain_tfidf,y_mul, categroy


        # print("################## Model building started #################\n")
        # svc = SVC( kernel='rbf', C=1e9, gamma=1e-07)
        # # svc = KNeighborsClassifier(n_neighbors = 5, weights = 'distance',algorithm = 'brute',metric = 'minkowski')
        # svm_clf = OneVsRestClassifier(svc)
        # svm_clf.fit(xtrain_tfidf, ytrain)
        # print("################## Model building end #################\n")
        # # saving the model 
        # # make folder if not exist
       
        # filename = f'models/{folder_name}/{categroy}.sav'
        # pickle.dump(svm_clf, open(f'models/{folder_name}/{categroy}.sav', 'wb'))
        # loaded_model = pickle.load(open(filename, 'rb'))

        # print("################## Making prediction #################\n")
        # svm_pred = svm_clf.predict(xval_tfidf)
        # # evaluate performance
        # print(f1_score(yval, svm_pred, average="micro"))
        