from flask import Flask,request,jsonify
from flask import app
import joblib
import os

def test(category, description, title):
    job_roles = [category, description, title]
    return job_roles

def main():
    
    # Load pre trained model
    result = loaded_model.predict()
    
    return result

app=Flask(__name__)

@app.route('/job_roles',methods= ["POST", "GET"] )     
def job_role():

    category = request.form.get('category')
    description = request.form.get('description')
    title = request.form.get('title')
    
    predicted_job_roles = test(category, description, title)

    return jsonify(predicted_job_roles)

if __name__=="__main__":
    # Load the model from disk
    # model = os.getenv("prediction_model")
    # loaded_model = joblib.load(model)
    
    app.run()