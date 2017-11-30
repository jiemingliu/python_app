from flask import Flask,request,render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'just do it more'

@app.route('/')
def index():
	# user_agent = request.headers.get('User-Agent')
	# return '<h1>hello ,your browser is %s</h1>' % user_agent;
	return render_template('index.html',current_time=datetime.utcnow());

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