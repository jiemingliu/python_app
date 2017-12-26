# 
## 一些框架用到的模块
1. from flask_script import Manager 为程序添加一个命令行解析器，例如：可用 python app.py shell 在应用程序上下文中运行python shell
2. 数据库相关操作用
   from flask.ext.sqlalchemy import SQLAlchemy  
   db = SQLAlchemy(app)
   创建数据库 db.create_all()
   更新数据库表结构
   from flask_migrate import Migrate,MigrateCommand
   migrate = Migrate(app, db)
   manager.add_command('db', MigrateCommand)
   python app.py db init	(创建迁移仓库)
   python app.py db migrate -m "initial migration"	(创建迁移脚本)
   python app.py db upgrade		(更新数据表结构)