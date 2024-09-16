from flask import Flask, render_template, request
from form import InputForm
from database import init_db, get_db, close_db
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

with app.app_context():
    init_db()

model = joblib.load('pipeline.joblib')
scaler = StandardScaler()

def map_and_standardize_columns(df):
    # Mapping categorical columns to numerical values
    df['Contract'] = df['Contract'].map({'Month-to-month': 0, 'One year': 1, 'Two year': 2})
    df['Partner'] = df['Partner'].map({'Yes': 1, 'No': 0})
    df['Dependents'] = df['Dependents'].map({'Yes': 1, 'No': 0})
    df['PhoneService'] = df['PhoneService'].map({'Yes': 1, 'No': 0})
    df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})
    df['MultipleLines'] = df['MultipleLines'].map({'No phone service': 0, 'No': 1, 'Yes': 2})
    df['OnlineSecurity'] = df['OnlineSecurity'].map({'No internet service': 0, 'Yes': 2, 'No': 1})
    df['OnlineBackup'] = df['OnlineBackup'].map({'No internet service': 0, 'Yes': 2, 'No': 1})
    df['DeviceProtection'] = df['DeviceProtection'].map({'No internet service': 0, 'Yes': 2, 'No': 1})
    df['TechSupport'] = df['TechSupport'].map({'No internet service': 0, 'Yes': 2, 'No': 1})
    df['StreamingTV'] = df['StreamingTV'].map({'No internet service': 0, 'Yes': 2, 'No': 1})
    df['PaperlessBilling'] = df['PaperlessBilling'].map({'Yes': 1, 'No': 0})
    df['PaymentMethod'] = df['PaymentMethod'].map({
        'Electronic check': 0, 
        'Mailed check': 1, 
        'Bank transfer (automatic)': 2, 
        'Credit card (automatic)': 3
    })
    df['InternetService'] = df['InternetService'].map({
        'DSL': 0, 
        'Fiber optic': 1, 
        'No': 2
    })

     # Handling non-numeric values in TotalCharges
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())

    # Handle missing values for other columns (if any)
    df.fillna(df.median(numeric_only=True), inplace=True)
    df.fillna(0, inplace=True)
    
            # Standardizing all columns that are not in the form
    columns_to_standardize = ['tenure', 'MonthlyCharges', 'TotalCharges']
    for col in columns_to_standardize:
        variance = df[col].var()
        if pd.isna(variance) or variance == 0:
            print(f"Column '{col}' has no variance or is NaN; keeping original value.")
        else:
            scaler = StandardScaler()
            df[col] = scaler.fit_transform(df[[col]])

    return df
@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm()
    prediction = None
    prediction_result = None
    if form.validate_on_submit():
        data = {
            'tenure': form.tenure.data,
            'MonthlyCharges': float(form.MonthlyCharges.data),
            'TotalCharges': float(form.TotalCharges.data),
            'Contract': form.Contract.data,
            'Partner': form.Partner.data,
            'Dependents': form.Dependents.data,
            'PhoneService': form.PhoneService.data,
            'gender': form.gender.data,
            'SeniorCitizen': form.SeniorCitizen.data,
            'MultipleLines': form.MultipleLines.data,
            'OnlineSecurity': form.OnlineSecurity.data,
            'OnlineBackup': form.OnlineBackup.data,
            'DeviceProtection': form.DeviceProtection.data,
            'TechSupport': form.TechSupport.data,
            'StreamingTV': form.StreamingTV.data,
            'PaperlessBilling': form.PaperlessBilling.data,
            'PaymentMethod': form.PaymentMethod.data,
            'InternetService': form.InternetService.data
        }

        print("Data before transformation:", data)              # Debugging print

        # Convert the data into a DataFrame for transformation
        df = pd.DataFrame([data])

         # Define the correct order of features as expected by the model
        feature_columns = [
            'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
            'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
            'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
            'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges',
            'TotalCharges'
        ]

         # Reorder columns to match the feature columns expected by the model
        df = df[feature_columns]

        # Apply transformations to the data
        df = map_and_standardize_columns(df)
        print("DataFrame after transformation:", df)  # Debugging print

         # Make prediction using   loaded model
        prediction = int(model.predict(df)[0])  
        prediction_result = "Churning" if prediction == 1 else "Not Churning"
        print("Prediction:", prediction)  # Debugging print

           # Insert data into the database
        db = get_db()
        try:
            db.execute(
                '''INSERT INTO churn (tenure, MonthlyCharges, TotalCharges, Contract, Partner, Dependents, 
                PhoneService, gender, SeniorCitizen, MultipleLines, OnlineSecurity, OnlineBackup, DeviceProtection, 
                TechSupport, StreamingTV, PaperlessBilling, PaymentMethod, InternetService, prediction) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (data['tenure'], data['MonthlyCharges'], data['TotalCharges'], data['Contract'], data['Partner'],
                data['Dependents'], data['PhoneService'], data['gender'], data['SeniorCitizen'], data['MultipleLines'],
                data['OnlineSecurity'], data['OnlineBackup'], data['DeviceProtection'], data['TechSupport'],
                data['StreamingTV'], data['PaperlessBilling'], data['PaymentMethod'], data['InternetService'], 
                prediction)
            )
            db.commit()
            print("Data inserted into the database successfully.")  # Debugging print
        except Exception as e:
            print(f"An error occurred during database insertion: {e}")  # Error handling

         # Render the template with the prediction result
        return render_template('index.html', form=form, prediction=prediction, prediction_result=prediction_result)
    else:
        print(form.errors)  # Debugging print to check form validation errors

    return render_template('index.html', form=form, prediction=prediction, prediction_result=prediction_result)

if __name__ == '__main__':
    app.run(debug=True)