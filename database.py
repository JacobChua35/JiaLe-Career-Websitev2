from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://w60od2gi5xx87b94x1m0:pscale_pw_pd8NONWqHC6UB6YmNUA20ekrz5AsIVB0zzTVxbIQIlY@aws.connect.psdb.cloud/jia_le_careers?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    column_names = result.keys()

    jobs = []

    for row in result.all():
      jobs.append(dict(zip(column_names, row)))
    return jobs


# database: jia_le_careers
# username: w60od2gi5xx87b94x1m0
# host: aws.connect.psdb.cloud
# password: pscale_pw_pd8NONWqHC6UB6YmNUA20ekrz5AsIVB0zzTVxbIQIlY
