from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)

# No Longer needed the code below it hardcoded,I used SQL Database to store the List # of jobs inside and # I print it out instead.

#JOBS = [
#  {
#    'id': 1,
#    'title': 'Data Analyst',
#    'location': 'San Franciso, USA',
#    'salary': 'USD5600'
#  },
#  {
#    'id': 2,
#    'title': 'Professional Cybersecurity Pentester',
#    'location': 'Singapore',
#    'salary': 'SGD6700'
#  },
#  {
#    'id': 3,
#    'title': 'Network Security Engineer',
#    'location': 'Singapore',
#    'salary': 'SGD6000'
#  },
#  {
#    'id': 4,
#    'title': 'Unity Game Developer',
#    'location': 'Vietnam',
#    'salary': 'VND87300000'
#  },
#  {
#    'id': 5,
#    'title': 'Full Stack Developer',
#    'location': 'United Kingdom of Britain',
#    'salary': 'GBP6900'
#  },
#  {
#    'id': 6,
#    'title': 'PwC IT Governance & Compliance',
#    'location': 'Malaysia',
#  },
#]


@app.route("/")
def hello_world():
  jobs_list = load_jobs_from_db()
  return render_template('home.html', jobs=jobs_list, company_name='Jia Le')


@app.route("/api/jobs")
def list_jobs():
  jobs_list = load_jobs_from_db()
  return jsonify(jobs_list)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
