from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class InputForm(FlaskForm):
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    SeniorCitizen = SelectField('Senior Citizen', choices=[('0', 'No'), ('1', 'Yes')], validators=[DataRequired()])
    Partner = SelectField('Partner', choices=[('Yes', 'Yes'), ('No', 'No')], validators=[DataRequired()])
    Dependents = SelectField('Dependents', choices=[('Yes', 'Yes'), ('No', 'No')], validators=[DataRequired()])
    tenure = IntegerField('Tenure', validators=[DataRequired()])
    PhoneService = SelectField('Phone Service', choices=[('Yes', 'Yes'), ('No', 'No')], validators=[DataRequired()])
    MultipleLines = SelectField('Multiple Lines', choices=[('No phone service', 'No phone service'), ('No', 'No'), ('Yes', 'Yes')], validators=[DataRequired()])
    InternetService = SelectField('Internet Service', choices=[('DSL', 'DSL'), ('Fiber optic', 'Fiber optic'), ('No', 'No')], validators=[DataRequired()])
    OnlineSecurity = SelectField('Online Security', choices=[('No internet service', 'No internet service'), ('No', 'No'), ('Yes', 'Yes')], validators=[DataRequired()])
    OnlineBackup = SelectField('Online Backup', choices=[('No internet service', 'No internet service'), ('No', 'No'), ('Yes', 'Yes')], validators=[DataRequired()])
    DeviceProtection = SelectField('Device Protection', choices=[('No internet service', 'No internet service'), ('No', 'No'), ('Yes', 'Yes')], validators=[DataRequired()])
    TechSupport = SelectField('Tech Support', choices=[('No internet service', 'No internet service'), ('No', 'No'), ('Yes', 'Yes')], validators=[DataRequired()])
    StreamingTV = SelectField('Streaming TV', choices=[('No internet service', 'No internet service'), ('No', 'No'), ('Yes', 'Yes')], validators=[DataRequired()])
    Contract = SelectField('Contract', choices=[('Month-to-month', 'Month-to-month'), ('One year', 'One year'), ('Two year', 'Two year')], validators=[DataRequired()])
    PaperlessBilling = SelectField('Paperless Billing', choices=[('Yes', 'Yes'), ('No', 'No')], validators=[DataRequired()])
    PaymentMethod = SelectField('Payment Method', choices=[('Electronic check', 'Electronic check'), ('Mailed check', 'Mailed check'), ('Bank transfer (automatic)', 'Bank transfer (automatic)'), ('Credit card (automatic)', 'Credit card (automatic)')], validators=[DataRequired()])
    MonthlyCharges = DecimalField('Monthly Charges', validators=[DataRequired()])
    TotalCharges = DecimalField('Total Charges', validators=[DataRequired()])

    submit = SubmitField('Submit')
