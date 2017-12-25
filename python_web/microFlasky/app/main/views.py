from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..modules import User
from ..email import send_email
from . import main
from .forms import NameForm

@main.route('/',methods=['GET','POST'])		#路由修饰器由蓝本提供
def index():
	form = NameForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username = form.name.data).first()
		if user is None:
			user = User(username = form.name.data)
			db.session.add(user)
			db.session.commit()
			session['known'] = False
			if current_app.config['FLASKY_ADMIN']:
				send_email(current_app.config['FLASKY_ADMIN'], 'New User',
					'mail/new_user', user=user)
		else:
			session['known'] = True
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('.index'))
	return render_template('index.html',form=form,name=session.get('name'),
							known = session.get('known',False));

@main.route('/user/<name>')
def user(name):
	return render_template('user.html',name=name);

from flask import make_response
@main.route('/response')
def set_response():
	response = make_response('<h1>视图可以返回由make_response()函数返回的Response对象</h1>');
	response.set_cookie('answer','23');
	return response;