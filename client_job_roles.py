import requests
import json 
from db_job_roles import store_job_roles, get_jobs_data

def get_predicted_job_roles(job_title, job_description, category):
    
    result = requests.post('http://127.0.0.1:5000/job_roles',
                            data = {'category': category,
                                    'title': job_title,
                                    'description': job_description})

    result_json=json.loads(result.text)

    predicted_job_roles = result_json['job_roles']

    print(predicted_job_roles)
    #store results

def main():
    
    #db connection
    job_data = get_jobs_data()

    for job in job_data:

        job_title = job[0]
        job_description = job[1]
        job_industry = job[2].replace(' ', '_').lower()
        
        get_predicted_job_roles(job_title, job_description, job_industry)
        

if __name__=="__main__":
    main()
    # job title.