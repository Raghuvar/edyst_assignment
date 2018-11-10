from flask_wtf import FlaskForm
from wtforms.fields.html5 import URLField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, url


class UrlInputForm(FlaskForm):
	url = URLField('url', validators=[DataRequired(), url() ])
	submit = SubmitField('Submit')