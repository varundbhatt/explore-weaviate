import json
import pandas as pd # type: ignore
from clients import build_weaviate_client

client = build_weaviate_client()

def load_data_json():
    try:
        collection = client.collections.get("Jobs")
        
        ## load data from csv
        # df = pd.read_csv(
        #     "JobDetails_Dataset__High_Cardinality_Titles_.csv",
        #     quoting=csv.QUOTE_MINIMAL,
        #     escapechar='\\',
        #     doublequote=True)
                
        with open('./data/jobs_response_10.json') as f: #till 3 done 4221
            data = json.load(f)
        
        # Extract desired fields
        rows = []
        for job in data['data']:
            row = {
                "job_id": job["id"],
                "company": job["company"],
                "job_title": job["job_title"],
                "job_description": job["description"],
                "location": job["location"],
                "industry": job["company_object"]["industry"],
                "date_posted": job["date_posted"],
                "salary_min": int(job["min_annual_salary_usd"]) if job["min_annual_salary_usd"] is not None else 0,
                "salary_max": int(job["max_annual_salary_usd"]) if job["max_annual_salary_usd"] is not None else 0,
                "funding_stage": job["company_object"]["funding_stage"],
            }
            rows.append(row)

        # Create DataFrame
        df = pd.DataFrame(rows)
        df["date_posted"] = pd.to_datetime(df["date_posted"]).dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        df = df.iloc[0:501]
    
        
        # Upload data in batch
        with collection.batch.dynamic() as batch:
            for _, row in df.iterrows():
                properties = {
                    "job_id": row["job_id"],
                    "company": row["company"],
                    "job_title": row["job_title"],
                    "job_description": row["job_description"],
                    "location": row["location"],
                    "industry": row["industry"],
                    "date_posted": row["date_posted"],
                    "salary_min": row["salary_min"],
                    "salary_max": row["salary_max"],
                    "funding_stage": row["funding_stage"],
                }
                batch.add_object(properties=properties)
        
    finally:    
        client.close()
        
load_data_json()