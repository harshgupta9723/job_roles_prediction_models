from flask import Flask,request,jsonify
from flask import app
import pandas as pd
import numpy as np
import re
import io
import joblib
import pickle
from nltk.corpus import stopwords
import os
from scipy.sparse import hstack
from sklearn.preprocessing import MultiLabelBinarizer

#Load all important files to predict job_title
#these files including encodings and pretrained models

desc_title_vectorizer = 'saved_model/vectorizer'
prediction_model = 'saved_model/model'
class_list = 'saved_model/classes.txt'

#Datacleaning function to clean data
def clean_data(job_data):
    stop_words = set(stopwords.words('english'))
    text = job_data
    text = text.lower()
    text = re.sub('[^A-Za-z]+', ' ', str(text))  #removing special characters
    text = ' '.join([text for text in text.split() if text not in stop_words]) #removing stopwords
    return text


# loaded_vectorizer = joblib.load(desc_title_vectorizer)
# loaded_model = joblib.load(prediction_model)
# loaded_class = pickle.load(open(class_list, 'rb'))
# loaded_class = joblib.load(class_list)


# def find_class(df):
#     y = df['job_roles']
#     y = y.values.reshape(-1,1)
#     mlb = MultiLabelBinarizer()
#     y_bin = mlb.fit_transform(y)
#     return mlb

def predict_job_roles(q):
    q = clean_data(q)
    q_vec = loaded_vectorizer.transform([q])
    q_pred = loaded_model.predict(q_vec)
    return loaded_class.inverse_transform(q_pred)

def main(description , title):
    final_string = description + ' '+ title
    
    result = predict_job_roles(final_string)
    return result




# text1 = 'Must have excellent management and communication skills\r\n•\r\nFamiliarity with business skills as relating to ground operations, i.e. budgeting, cost control, labor allocation, and inventory management\r\n•\r\nProficient in MS Office suite'
# text2 = 'Airline - Ground Handling Manager'
# # data = [[text1,text2]]
# col_names = ['description', 'title']
# df = pd.DataFrame(data,columns=col_names)

# main(text1 ,text2)


app=Flask(__name__)

@app.route('/job_roles',methods= ["POST", "GET"] )
def job_role():
    description = request.form.get('description')
    title = request.form.get('title')
    category = request.form.get('category')
    job_roles = main(description, title)
    return jsonify(job_roles)



if __name__=="__main__":

    app.run()