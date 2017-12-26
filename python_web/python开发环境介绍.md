# 在windows下使用virtualenv(或者pyvenv)虚拟开发环境
1. 使用pip install virtualenv安装，如果不行，使用python -m pip install virtualenv安装
2. 使用virtualenv [yourName] 安装项目环境
3. 使用 yourName\Scripts\activate 启动虚拟环境
4. 然后安装所需类库方法，跟非虚拟环境一样
5. 退出虚拟环境 deactivate
   
6. pyvenv在python3.4版本以后自带，用法同virtualenv几乎一样
   
7. 批量安装包的方法，将所需要的包和包的版本写在一个 .txt 文件中，启动虚拟环境，运行命令 pip install -r requests.txt