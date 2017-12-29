from flask import render_template,redirect,url_for
from . import auth
from flask_login import logout_user,login_required

@auth.route('/login')
def login():
	return render_template('auth/login.html')
	
@auth.route('/logout')
def logout():
	logout_user()
	flask('U have been logged out')
	return redirect(url_for('main.index'))
	
@auth.route('/register',methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(email=form.email.data,
		username=form.username.data,
		password=form.password.data)
		db.session.add(user)
		flash('You can now login.')
		return redirect(url_for('auth.login'))
	return render_template('auth/register.html', form=form)