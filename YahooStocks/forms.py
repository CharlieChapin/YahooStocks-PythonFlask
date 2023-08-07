# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired

class StockDataForm(FlaskForm):
    tickers = StringField('Tickers', validators=[DataRequired()])
    start_date = DateField('Start Date', format='%Y-%m-%d', validators=[DataRequired()])
    end_date = DateField('End Date', format='%Y-%m-%d', validators=[DataRequired()])
    interval = SelectField('Interval', choices=[
        ('1d', '1 day'),
        ('5d', '5 days'),
        ('1wk', '1 week'),
        ('1mo', '1 month'),
        ('3mo', '3 months'),
        ('6mo', '6 months'),
        ('1y', '1 year'),
        ('2y', '2 years'),
        ('5y', '5 years'),
        ('10y', '10 years'),
        ('ytd', 'YTD'),
        ('max', 'Max')
    ], validators=[DataRequired()])
    submit = SubmitField('Get Data')
