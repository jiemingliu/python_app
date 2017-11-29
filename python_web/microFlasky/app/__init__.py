from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent')
	return '<h1>hello ,your browser is %s</h1>' % user_agent;
	
@app.route('/error')
def error():
	return '<h1>找不到页面</h1?',400;

from flask import make_response
@app.route('/response')
def set_response():
	response = make_response('<h1>视图可以返回由make_response()函数返回的Response对象</h1>');
	response.set_cookie('answer','23');
	return response;
	
@app.route('/user/<name>')
def user(name):
	return '<h1>hello,%s!</h1>' % name;

from flask import redirect,url_for
@app.route('/redirect')
def redirect():
	return redirect('www.baidu.com');

if __name__ == '__main__':
	app.run(debug=True)