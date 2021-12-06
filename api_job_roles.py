# It loads all trained model and use them to predict the job_roles.
# Description ,Category and Title are given as input and job-title is output.


from flask import Flask,request,jsonify
from flask import app
import re
import joblib
import pickle
from nltk.corpus import stopwords
import pandas as pd


def clean_data(job_data):
    """
    It cleans the given text.
    Input: Text
    Output: Clean text
    """
    stop_words = set(stopwords.words('english'))
    text = job_data
    text = text.lower()
    text = re.sub('[^A-Za-z]+', ' ', str(text))  #removing special characters
    text = ' '.join([text for text in text.split() if text not in stop_words]) #removing stopwords
    return text

# working properly
def load_model(vector_path,model_path,class_path):
    """
    It loads the all three trained models.
    Input : path of saved model.
    Output: loaded models
    """
    loaded_model = joblib.load(model_path)
    loaded_vectorizer = pickle.load(open(vector_path, 'rb'))

    class_data = pd.read_csv(class_path)
    loaded_class = list(class_data["classes"])

    return loaded_vectorizer,loaded_model,loaded_class


def inverse_transform(class_list,encoded_list):
    """
    It map the classes with encoded result.
    Input : list of class ,predicted encoded value.
    Output : predicted job roles.
    """

    result = [class_list[i] for i in range(len(encoded_list[0])) if encoded_list[0][i] == 1]
    return result


app=Flask(__name__)

@app.route('/job_roles',methods= ["POST", "GET"] )

def job_role():
    """
    It is main function to use all the loaded models.
    Input :None
    Output: Predicted job-roles
    """
    description = request.form.get('description')
    title = request.form.get('title')
    category = request.form.get('category')

    model_folder = "models" + "/" + category + "/"
    
    vector_path = model_folder + category + "_vectorizer.pickle"

    model_path =  model_folder + category + ".sav"

    class_path = model_folder + category + ".csv"
    
    loaded_vectorizer,loaded_model,loaded_class = load_model(vector_path,model_path,class_path)

    def predict_job_roles(q):
        """
        It predict the job roles
        Input: text
        Output : job_roles
        """
        q = clean_data(q)
        q_vec = loaded_vectorizer.transform([q])
        q_pred = loaded_model.predict(q_vec)
        final_result = inverse_transform(loaded_class,q_pred)
        return final_result


    final_string = description + ' '+ title
    result = predict_job_roles(final_string)
    return jsonify(result)


if __name__=="__main__":

    app.run()