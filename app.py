from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'San Franciso, USA',
    'salary': 'USD5600'
  },
  {
    'id': 2,
    'title': 'Professional Cybersecurity Pentester',
    'location': 'Singapore',
    'salary': 'S$6700'
  },
  {
    'id': 3,
    'title': 'Network Security Engineer',
    'location': 'Singapore',
    'salary': 'S$6000'
  },
  {
    'id': 4,
    'title': 'Unity Game Developer',
    'location': 'Vietnam',
    'salary': 'Đồng 87300000'
  },
  {
    'id': 5,
    'title': 'Full Stack Developer',
    'location': 'United Kingdom of Britain',
    'salary': '£6900'
  },
  {
    'id': 6,
    'title': 'PwC IT Governance & Compliance',
    'location': 'Malaysia',
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Jia Le')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
