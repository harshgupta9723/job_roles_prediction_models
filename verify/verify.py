# from flask import request
import requests
import json
import pandas as pd 

df = pd.read_csv('inputfile.csv',encoding="ISO-8859-1")


def testing(x,y,z):
    result = requests.get(" http://143.198.113.228:5080/job_roles",
    data={
        "title":x,
        "description":y,
        "category":z,
    })

    results =json.loads(result.text)
    return results

df['output']= df[['title' ,'description','category']].apply(lambda x: testing(x['title'],x['description'],x['category']),axis=1)

df.to_csv('testing.csv',index=False)
