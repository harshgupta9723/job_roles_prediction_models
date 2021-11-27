# process all jobs
import csv
import os
import sqlalchemy
from sqlalchemy import create_engine
import pymysql


def get_connection():

    #get environment variable
    user=os.getenv("DBUSER")
    passwd=os.getenv("DBPASS")
    host=os.getenv("DBHOST")
    database=os.getenv("DBNAME")

    #connection string
    con_string="mysql+pymysql://{}:{}@{}/{}".format(user, passwd, host, database)

    #create engine
    sqlEngine = create_engine(con_string, pool_recycle=3600)
    db = sqlEngine.raw_connection()
    return db


def get_jobs_data():
    
    db = get_connection()
    cur = db.cursor()

    data = []

    query = ""
    cur.execute(query)
    job_list = cur.fetchall()

    for row in job_list:
        data.append(row)

    cur.close()
    db.close()

    return data

def store_job_roles(predicted_job_roles):
    
    #predicted_job_roles
    print('predicted_job_roles')
    
    db = get_connection()
    cur = db.cursor()

    query = "update query"
    cur.execute(query)

    cur.close()
    db.close()
    
    
    return