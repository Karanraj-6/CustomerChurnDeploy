import sqlite3
from flask import g

DATABASE = 'churn.db'  #path

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with db:
        db.executescript('''
            CREATE TABLE IF NOT EXISTS churn (

            gender INTEGER,
            SeniorCitizen INTEGER,
            Partner INTEGER,
            Dependents INTEGER,
            tenure INTEGER,
            PhoneService INTEGER,
            MultipleLines INTEGER,
            InternetService INTEGER,
            OnlineSecurity INTEGER,
            OnlineBackup INTEGER,
            DeviceProtection INTEGER,
            TechSupport INTEGER,
            StreamingTV INTEGER,
            PaperlessBilling INTEGER,
            PaymentMethod INTEGER,
            MonthlyCharges REAL,
            TotalCharges REAL,
            Contract INTEGER,  
            prediction INTEGER
        );

        ''')
