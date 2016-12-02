from flask import Flask, render_template, flash, request, session
from flask_bootstrap import Bootstrap
from wtforms.fields import *
from wtforms import widgets, Form as _Form, validators
from wtforms.fields.html5 import DateField, EmailField

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'GNV45w2m9WpMQSXEVp7c45ZtGfgAcXRqxJJ7ndKeyshrFSymAbE9ZmQWGfC7PbMr'

class OnboardForm(_Form):
	customername = TextField('Customer Name:', validators=[validators.required()])
	customercontactname = TextField('Contact Name:', validators=[validators.required()])
	customercontactemail = EmailField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
	customerphone = TextField('Phone Number:', validators=[validators.required()])


@app.route("/", methods=['GET', 'POST'])
def hello():
	form = OnboardForm(request.form)

	print form.errors
	if request.method == 'POST':
		#date=DateField('Date:', format="%Y-%m-%dT%H:%M:%S", default=datetime.today(), validators=[validators.DataRequired()])
		customername=request.form['customername']
		customercontactname=request.form['customercontactname']
		customercontactemail=request.form['customercontactemail']
		customerphone=request.form['customerphone']
		print customername
		
		if form.validate():
			# Save the comment here.
			flash('Thanks for registration ' + customername)
		else:
			flash('Error: All the form fields are required. ')

	return render_template('hello.html', form=form)

if __name__ == "__main__":
	app.run()
