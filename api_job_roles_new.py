from flask import Flask,request,jsonify
from flask import app
from nltk.util import pr
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

# desc_title_vectorizer = 'saved_model/vectorizer'
# prediction_model = 'saved_model/model'
# class_list = 'saved_model/classes.txt'

#Datacleaning function to clean data
def clean_data(job_data):
    stop_words = set(stopwords.words('english'))
    text = job_data
    text = text.lower()
    text = re.sub('[^A-Za-z]+', ' ', str(text))  #removing special characters
    text = ' '.join([text for text in text.split() if text not in stop_words]) #removing stopwords
    return text


def load_model(vector_path,model_path,class_path):
    loaded_vectorizer = joblib.load(vector_path)
    loaded_model = joblib.load(model_path)
    loaded_class = joblib.load(class_path)
    return loaded_vectorizer,loaded_model,loaded_class
# loaded_class = joblib.load(class_list)


# def predict_job_roles(q):
#     q = clean_data(q)
#     q_vec = loaded_vectorizer.transform([q])
#     q_pred = loaded_model.predict(q_vec)
#     return loaded_class.inverse_transform(q_pred)

# def main(description , title):
#     final_string = description + ' '+ title    
#     result = predict_job_roles(final_string)
#     return result




text1 = 'Must have excellent management and communication skills\r\n•\r\nFamiliarity with business skills as relating to ground operations, i.e. budgeting, cost control, labor allocation, and inventory management\r\n•\r\nProficient in MS Office suite'
text2 = 'Airline - Ground Handling Manager'
text3 = 'property'

# main(text1 ,text2)


# app=Flask(__name__)

# @app.route('/job_roles',methods= ["POST", "GET"] )
def job_role(description, title, category):

    # description = request.form.get('description')
    # title = request.form.get('title')
    # category = request.form.get('category')


    model_folder = "/home/harsh/job_roles_prediction_models/models" + "/" + category + "/"
    print(model_folder)
    
    vector_path = model_folder + category + "_vectorizer.pickle"
    print(vector_path)

    model_path =  model_folder + category + ".sav"
    print(model_path)

    class_path = model_folder + category
    print(class_path)

    loaded_vectorizer,loaded_model,loaded_class = load_model(vector_path,model_path,class_path)

    def predict_job_roles(q):
        q = clean_data(q)
        q_vec = loaded_vectorizer.transform([q])
        q_pred = loaded_model.predict(q_vec)
        return loaded_class.inverse_transform(q_pred)

    final_string = description + ' '+ title
    result = predict_job_roles(final_string)
    print(result)

    

    # def main(description , title):

    #     final_string = description + ' '+ title    
    #     result = predict_job_roles(final_string)
    #     return result


    

job_role(text1,text2,text3)

    # job_roles = main(description, title)
    # return jsonify(job_roles)



# if __name__=="__main__":

#     app.run()