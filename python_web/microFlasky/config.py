import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = 'just do it more' #os.environ.get('SECRET_KEY') or 'just do it more'
	MAIL_SERVER = 'smtp.163.com' #os.environ.get('MAIL_SERVER') or 'smtp.163.com'
	MAIL_PORT = 25 #int(os.environ.get('MAIL_PORT')) or 25
	MAIL_USE_TLS = True
	MAIL_USE_SSL = False
	MAIL_USERNAME = 'liumingjie_blog@163.com' #os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = '626231329mingjie' #os.environ.get('MAIL_PASSWORD')
	FLASKY_MAIL_SUBJECT_PREFIX = 'This is from Lmj'
	FLASKY_MAIL_SENDER = 'liumingjie_blog@163.com' #os.environ.get('MAIL_USERNAME') or 'liumingjie_blog@163.com'
	FLASKY_ADMIN = 'liumingjie.blog@foxmail.com' #os.environ.get('FLASKY_ADMIN') or 'liumingjie.blog@foxmail.com'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	@staticmethod
	def init_app(app):
		pass
		
class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'app/','data-dev.sqlite')
	print(SQLALCHEMY_DATABASE_URI)
	
class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
			'sqlite:///' + os.path.join(basedir, 'tests/','data-dev.sqlite')
	
class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir,'data.sqlite')
		
config = {
	'development':DevelopmentConfig,
	'testing':TestingConfig,
	'production':ProductionConfig,
	'default':DevelopmentConfig
}