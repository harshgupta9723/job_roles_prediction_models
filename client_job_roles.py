import requests
import json 
from db_job_roles import store_job_roles, get_jobs_data, get_connection

def get_predicted_job_roles(db, category, job_description, job_title):
    
    result = requests.post('http://127.0.0.1:5000/job_roles',
                            data = {'category': category,
                                    'title': job_title,
                                    'description': job_description})

    result_json=json.loads(result.text)

    predicted_job_roles = result_json['job_roles']

    store_job_roles(predicted_job_roles)


def main():
    
    #db connection
    job_data = get_jobs_data()

    for job in job_data:
        get_predicted_job_roles(job)


if __name__=="__main__":
    main()
    # job title.