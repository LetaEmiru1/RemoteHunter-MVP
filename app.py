from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
import os

app = Flask(__name__)
from flask_cors import CORS

# Enable CORS for all routes
CORS(app)

 
# Define a route for the root URL
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Define a route to fetch and print jobs
import requests
import json
from supabase import create_client, Client
import os
from dotenv import load_dotenv

#jooble api
host = 'jooble.org'
key = os.environ.get("JOOBLE_KEY")


load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

@app.route('/api/jobs')
def get_jobs():
    try:
        response = supabase.table('jobs').select('*').order('created_at', desc=True).limit(50).execute()
        return jsonify(response.data)
    except Exception as e:
        # Return an error if the database call fails
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(port=5000, debug=True)