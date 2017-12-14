from flask import Flask,request,render_template,session,redirect,url_for,flash
from flask_script import Manager,Shell
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_mail import Mail,Message
import os
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

#数据库配置
db=SQLAlchemy(app)
migrate = Migrate(app,db)
app.config['SECRET_KEY'] = 'just do it more'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#邮件服务器配置
mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

app.config['FLASKY_MAIL_SUBJECT_PREFIX']='This is from Lmj'
app.config['FLASKY_MAIL_SENDER']='Flasky Admin <liumingjie.blog@foxmail.com>'
def send_email(to,subject,template,**kwargs):
	msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX']+subject,sender=app.config['FLASKY_MAIL_SENDER'],recipients=[to])
	msg.body=render_template(template+'.txt',**kwargs)
	msg.html=render_template(template+'.html',**kwargs)
	mail.send(msg)

#初始化方式
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

manager.add_command('db',MigrateCommand)


class Role(db.Model):
	__tablename__='roles'
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(64),unique=True)
	users = db.relationship('User',backref = 'role')
	
	def __repr__(self):
		return '<Role %r>' % self.name
		
class User(db.Model):
	__tablename__='users'
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(64),unique=True,index=True)
	role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
	
	def __repr__(self):
		return '<User %r>' % self.username

#定义回调函数，通过shell命令(python app.py shell)，直接导入特定的对象
def make_shell_context():
	return dict(app=app,db=db,User=User,Role=Role)
manager.add_command("shell",Shell(make_context=make_shell_context))

@app.route('/',methods=['GET','POST'])
def index():
	form = NameForm();
	if form.validate_on_submit():
		user = User.query.filter_by(username = form.name.data).first()
		if user is None:
			user = User(username = form.name.data)
			db.session.add(user)
			db.session.commit()
			session['known'] = False
			if app.config['FLASKY_ADMIN']:
				logging('EMAIL SEND SUCCESSFULLY')
				send_email(app.config['FLASKY_ADMIN'],'new User','mail/new_user',user=user)
		else:
			session['known'] = True
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('index'))
	return render_template('index.html',form=form,name=session.get('name'),
							known = session.get('known',False));

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

if __name__ == '__main__':
	manager.run()