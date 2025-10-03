import requests
import json
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import resend


#jooble api
host = 'jooble.org'
key = 'a62b1126-f8a5-44cf-82c3-9bf4c2c66e9b'

load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)


def notify_new_job(job):
    resend.api_key = os.environ.get("RESEND_API_KEY")
    params: resend.Emails.SendParams = {
    "from": "RemoteHunter <onboarding@resend.dev>",
    "to": [user_response.user.email],
    "subject": f"New Job Alert - {job['title']} at {job['company']}",
    "html": "<p>A new job matching your keyword has been posted:</p>"
            f"<p><strong>Title:</strong> {job['title']}</p>"
            f"<p><strong>Company:</strong> {job['company']}</p>"
            f"<p><strong>Link:</strong> <a href='{job['link']}'>{job['link']}</a></p>"
            "<p>Best regards,<br/>RemoteHunter Team</p>",
    "reply_to": "onboarding@resend.dev"
    }
    email = resend.Emails.send(params)
    print(email)

response = (
    supabase.table('profiles')
    .select("user_id, job_keyword")
    .not_.is_('job_keyword', None)
    .execute()
)

profiles_with_keywords = response.data

# Fetch jobs added in the last day
recent_response =  (
    supabase.table("jobs")
    .select("*")
    .gt("created_at", (datetime.now() - timedelta(days=1)).isoformat())
    .execute()
)


recent_jobs = recent_response.data # List of jobs added in the last day
print(f"Found {len(recent_jobs)} recent jobs added in the last day.")

for profile in profiles_with_keywords:
    user_id = profile['user_id']
    keyword = profile['job_keyword']
    user_response  = supabase.auth.admin.get_user_by_id(user_id)
    if user_response.user: 
        email = user_response.user.email
        print(f"User ID: {user_id} | Email: {email} | Job Keyword: {keyword}")
    else:
        email = "Not found"
        print(f"User ID: {user_id} | Email: Not found | Job Keyword: {keyword}")
        continue
    matched_jobs = [job for job in recent_jobs if keyword.lower() in job['title'].lower()]
    print(f"User ID: {user_id} | Keyword: {keyword} | Matched Jobs: {len(matched_jobs)}")
    for job in matched_jobs:
        print(f"  - {job['title']} at {job['company']} ({job['link']})")
        notify_new_job(job)
        print("Notification sent.")