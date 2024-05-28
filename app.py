from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs_data = [
    
    {
        "id": 1,
        "title": "Frontend Engineer",
        "location": "New York",
        "salary": "$130 000",
    },
    {
        "id": 2,
        "title": "SEO Consultant",
        "location": "San Francisco",
        "salary": "$200 000",
    },
    {
        "id": 3,
        "title": "PPC Consultant",
        "location": "Boston",
        "salary": "$140 000",
    },
    {
        "id": 4,
        "title": "CRM Specialist",
        "location": "Las Vegas",
        "salary": "$150 000",
    }   
    ]
@app.route("/")
def hello_world():
    return render_template("home.html", jobs= jobs_data)

@app.route("/jobs")
def listjobs():
    return jsonify(jobs_data)