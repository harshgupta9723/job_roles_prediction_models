from flask import Flask,request,jsonify
from flask import app
import pandas as pd
import numpy as np
import re
import io
import joblib
from nltk.corpus import stopwords
import os
from scipy.sparse import hstack
from sklearn.preprocessing import MultiLabelBinarizer

#Load all important files to predict job_title
#these files including encodings and pretrained models

desc_title_vectorizer = '/home/harsh/job_roles_prediction_models/job_description_vectorizer'
prediction_model = '/home/harsh/job_roles_prediction_models/svm_desc_title_prediction_model'

#Datacleaning function to clean data
def clean_data(job_data):
    stop_words = set(stopwords.words('english'))
    text = job_data
    text = text.lower()
    text = re.sub('[^A-Za-z]+', ' ', str(text))  #removing special characters
    text = ' '.join([text for text in text.split() if text not in stop_words]) #removing stopwords
    return text

def encoding_data_point(df):
    encode_description = joblib.load(desc_title_vectorizer)
    description_title_tfidf = encode_description.transform(df) # transform data point
    return description_title_tfidf

def find_class(df):
    y = df['job_roles']
    y = y.values.reshape(-1,1)
    mlb = MultiLabelBinarizer()
    y_bin = mlb.fit_transform(y)
    return mlb

def infer_tags_svm(data):
    q_vec = encoding_data_point(data)
    print(q_vec)
    q_pred = prediction_model.predict(q_vec)
    return mlb.inverse_transform(q_pred)

def main(df):
    df['desc_title'] = df['description'] + ' '+ df['title']
    df['clean_desc_title']= df['desc_title'].apply(clean_data)
    
    results = infer_tags_svm(df['clean_desc_title'])
    print(results)

    return 


text1 = 'Must have excellent management and communication skills\r\n•\r\nFamiliarity with business skills as relating to ground operations, i.e. budgeting, cost control, labor allocation, and inventory management\r\n•\r\nProficient in MS Office suite'
text2 = 'Airline - Ground Handling Manager'
data = [[text1,text2]]
col_names = ['description', 'title']
df = pd.DataFrame(data,columns=col_names)

main(df)


# app=Flask(__name__)

# @app.route('/job_roles',methods= ["POST", "GET"] )
# def job_role():

#     category = request.form.get('category')
# def infer_tags(q):
#     q = clean_data(q)
#     q_vec = encode_description.transform([q])
#     q_pred = model.predict(q_vec)
#     # return mlb.inverse_transform(q_pred)#     title = request.form.get('title')

# infer_tags(text2)
#     predicted_job_roles = test(category, description, title)

#     return jsonify(predicted_job_roles)

# if __name__=="__main__":
#     # Load the model from disk
#     # model = os.getenv("prediction_model")
#     # loaded_model = joblib.load(model)

#     app.run()