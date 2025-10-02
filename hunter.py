import requests
import json
from supabase import create_client, Client
import os
from dotenv import load_dotenv

#jooble api
host = 'jooble.org'
key = 'a62b1126-f8a5-44cf-82c3-9bf4c2c66e9b'

#json query
data = {
    "keywords": "remote, developer, engineer, python, backend, fullstack, django, flask, aws, devops, kubernetes, docker, 100% remote",
    "location": "USA, remote, Canada, Europe, UK, Australia, Germany, Netherlands, Switzerland, France, Spain, Italy, Poland",
    "page": 2,  # Page number for pagination
    "salary": 30000,  # Minimum salary filter  
}

resp = requests.post('https://jooble.org/api/' + key, json=data)
response = resp.json()

job_list = response.get('jobs', [])
print(f"DEBUG: Jooble API returned {len(job_list)} jobs.")
for job in job_list:
    print(f"DEBUG: Job Title - {job.get('title')}, Company - {job.get('company')}, Link - {job.get('link')}")
load_dotenv() # Load environment variables from .env file

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

for job in response.values():
    # skip if job is an integer (e.g., "totalCount")
    if isinstance(job, int):
        continue

    for item in job:
        title = item.get("title", "title not provided")
        company = item.get("company", "company not provided")
        link = item.get("link")
        if link:
            resp = (
            supabase.table("jobs")
            .upsert({"title": title, "company": company, "link": link})
            .execute()
            )