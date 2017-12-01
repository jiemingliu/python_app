from flask import Flask,request,render_template,session,redirect,url_for,flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))

import logging
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

class NameForm(Form):
	name=StringField('what is your name?',validators=[Required()]);
	submit=SubmitField('submit');

app = Flask(__name__)
app.config['SECRET_KEY'] = 'just do it more'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

db=SQLAlchemy(app)

class Role(db.Model):
	__tablename__='roles'
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(64),unique=True)
	
	def __repr__(self):
		return '<Role %r>' % self.name
		
class User(db.Model):
	__tablename__='users'
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(64),unique=True,index=True)
	
	def __repr__(self):
		return '<User %r>' % self.username

@app.route('/',methods=['GET','POST'])
def index():
	form = NameForm();
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('Looks like you have changed your name!')
		session['name']=form.name.data
		logging.info('name=%s'%session.get('name'))
		return redirect(url_for('index'))
	logging.info('name=%s'%session.get('name'))
	return render_template('index.html',form=form,name=session.get('name'));

from flask import make_response
@app.route('/response')
def set_response():
	response = make_response('<h1>视图可以返回由make_response()函数返回的Response对象</h1>');
	response.set_cookie('answer','23');
	return response;
	
@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name=name);
	
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404
	
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
if __name__ == '__main__':
	manager.run()