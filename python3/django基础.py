Django

	python开发的web框架, 开发动态网站；避免一些重复性工作 
	
	基于MVC模型的web框架
	
		重量级：Django， 基于MTV模型工作
		
		轻量级: Flask 
	
	松耦合的思想

		MVC模型  ---  Model View  Controller
		
			Model	模型,  负责数据库操作
			View	视图， 负责模板，展示操作
			Controller控制器, 	负责业务处理操作
			
		MTV模型
		
			Model       模型， 负责数据库操作 
			Template	负责HTML模板，展示
			View		负责业务处理逻辑 
		
		
		
		
1、安装django

1)、创建虚拟环境 

D:\>python -m venv venv
D:\>cd venv
D:\venv>cd Scripts
D:\venv\Scripts>activate

2)、安装django
	
	>> pip install django 
	
	>>> import django
	>>> django.get_version()
	'2.1.3'
	>>>
	
	
2、创建django项目

(django_venv) E:\>django-admin startproject webproject

		
3、启动django项目
		
(venv) D:\django_test\web01>python manage.py runserver
		
		
	方法1) python manage.py runserver

		默认监听在127.0.0.1:8000
	
	方法2) python manage.py runserver IP:port
	
	settings.py 
	
		ALLOWED_HOSTS = ["*",]
		
		
		
项目文件介绍：

	manage.py 	管理脚本 
	settings.py 	项目配置文件(设置允许主机、指定模板路径、指定数据库连接)
	urls.py 		设置url地址与视图函数的关系 
	wsgi.py 		nginx, django结合使用时
	
	
		
		
		
		
		
		
		
		
		
简单示例：初体验 

1) 在项目同名目录下创建一个views.py文件 ：

	from django.shortcuts import HttpResponse

	'''
		处理业务逻辑的视图函数
		作用：根据客户端的访问请求，给予客户端响应
		视图函数：
			1) 必须有一个参数 request
			2) 返回HttpResponse响应
	'''
	def test(request):
		return HttpResponse("这是一个测试页面")



2) 编辑urls.py文件，添加url地址和视图函数的映射关系 

	from . import views 
	
	urlpatterns = [
		path('admin/', admin.site.urls),
		'''
			定义url地址及函数的对应关系
		'''
		path('test/', views.test),
	]

通过浏览器访问 http://127.0.0.1:8080/test可以看到函数返回的数据






4、创建app

>> django-admin startapp <app名称>


示例：创建app

1)、创建app

	(django_venv) E:\webproject>django-admin startapp user

	(django_venv) E:\webproject>django-admin startapp group

	(django_venv) E:\webproject>django-admin startapp host


2) 视图函数  user/views.py 

	from django.shortcuts import render, HttpResponse

	# Create your views here.

	def login(request):
		return HttpResponse("用户登录界面")

	def register(request):
		return HttpResponse("用户注册界面")


3) urls.py

	from django.contrib import admin
	from django.urls import path
	from user import views



	urlpatterns = [
		path('admin/', admin.site.urls),
		path('login/', views.login),
		path('register/', views.register),

	]

浏览器测试访问


4) 在项目中注册app 

	settings.py 
	
			
		INSTALLED_APPS = [
			'django.contrib.admin',
			'django.contrib.auth',
			'django.contrib.contenttypes',
			'django.contrib.sessions',
			'django.contrib.messages',
			'django.contrib.staticfiles',
			'user',
			'group',
			'host',
		]



app目录介绍

	migrations	用于记录数据库操作记录(针对表结构的记录)
	admin.py 	默认提供数据库管理后台；注册自定义的model
	apps.py 	针对当前app的配置
	models.py 	用于定义model模型，定义数据库表结构、关系 
	tests.py 	用于定义单元测试代码 
	views.py 	用于定义视图函数, 业务逻辑处理函数 
	
	
	
	
	
	
	
	
	
	
	
	
	


示例：编写登录界面 

1)、定义url及函数对应关系 

settings.py 


	from cmdb import views

	urlpatterns = [
		path('login/', views.login),

2)、 编辑视图函数

cmdb/views.py

	from django.shortcuts import render

	def login(request):
		'''
			render(request参数, "模板名称")
		'''
		return render(request,"login.html")


3)、创建模板目录templates,创建login.html模板

	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Login Test</title>

		<style>
			label{
				width: 80px;
				text-align: right;
				display: inline-block;
			}
		</style>
	</head>
	<body>

		<form action="/login/" method="post">
			'''
				表单提交方法为post时，需要设置csrf_token认证
			'''
			{% csrf_token %}
			<p>
				<label for="username">用户名：</label>
				<input type="text" id="username" name="user" />
			</p>

			<p>
				<label for="password">密码：</label>
				<input type="password" id="password" name="pwd" />
			</p>

			<p>
				<input type="submit" value="提交" />
			</p>
		</form>

	</body>
	</html>


4)、注册模板目录 

settings.py 

	TEMPLATES = [
		{
			'BACKEND': 'django.template.backends.django.DjangoTemplates',
			'DIRS': [
				'''
					添加模板所在目录 
				'''
				"d:/django_test/web01/templates",
			],


5)、浏览器测试访问http://127.0.0.1:8000/login/




配置静态资源(css/js文件等)

1) 在项目下创建static目录，存储静态文件

	D:\django_test\web01\static 的目录

	2018/09/26  20:59            86,927 jquery-3.3.1.min.js
	2018/10/19  12:43                52 test.css


2) 定义静态文件存储路径 

settings.py

	STATIC_URL = '/static/'
	STATICFILES_DIRS = (
		os.path.join(BASE_DIR,"static"),
	)


3) 在html文件中引入静态资源 

	'''
		引入文件路径时，以settings.py中定义的STATIC_URL地址为访问地址
	'''

    <link rel="stylesheet" href="/static/test.css" />

	<script src="/static/jquery-3.3.1.min.js" />





客户端在向服务器提交请求时，所有的请求数据会保存在一个类似于字典的对象中，request.META

	通过遍历字典的方式可以查询所有请求数据 
	
	def login(request):
		for k, v in request.META.items():
			print("%s---%s" % (k, v))
		return render(request, "login.html"

	后台获取表单中的数据 
	
		表单提交数据的方法：
			GET	----------- 类似于字典的对象  request.GET 
			POST ---------- 类似于字典的对象  request.POST 
		
	
示例>>> 实现表单的简单验证

1、login.html模板样式修改

		<!DOCTYPE html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<title>用户登录</title>
		</head>
		<body>

		<form action="/login/" method="POST">
			{% csrf_token %}
			<p>
				用户名：<input type="text" name="username" />
			</p>

			<p>
				密码：<input type="password" name="pwd" />
			</p>

			<p>
				# {{ 变量名称 }}，定义模板变量
				<span style="color: red">{{ error_msg }}</span>
			</p>

			<p>
				<input type="submit" value="登录"/>
			</p>
		</form>
		</body>
		</html>

2、修改视图函数login

from django.shortcuts import render, HttpResponse, redirect

def login(request):
    # 判断用户是直接通过url地址访问的网页
    if request.method == "GET":
        return render(request, "login.html")
    # 判断用户点击提交按钮提交数据
    elif request.method == "POST":
        # 获取数据
        username = request.POST.get("username")
        password = request.POST.get("pwd")

        if username == "martin" and password == "redhat":
            return redirect("http://www.baidu.com")
        else:
            return render(request, "login.html", {"error_msg":"用户名或密码错误"})


3、url定义 

		from django.contrib import admin
		from django.urls import path
		from app01 import views


		urlpatterns = [
			path('admin/', admin.site.urls),
			path('login/', views.login),
		]
			
			
			
			
			
			


示例>>>>   修改上述示例，将用户验证通过后跳转到自定义的界面  

1) 定义模板文件，用于显示用户验证成功后的页面

templates/hosts.html 

	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>主机列表</title>
	</head>
	<body>

		<h2>主机列表</h2>

		<table border="1px">
			<tr>
				<td>主机IP</td>
				<td>主机名称</td>
				<td>主机状态</td>
			</tr>
			'''
				模板语言中的循环生成表格的多行
				host_list由后台传数据
			'''
			{% for host_info in host_list %}
				<tr>
					<td>{{ host_info.ip }}</td>
					<td>{{ host_info.hostname }}</td>
					<td>{{ host_info.status }}</td>
				</tr>
			{% endfor %}
			
		</table>

	</body>
	</html>
	
	

2) 定义视图函数用于返回模板内容 

app01/views.py 

	host_list = [
		{"ip":"1.1.1.10", "hostname": "tomcat.linux.com", "status":"Warning"},
		{"ip":"1.1.1.100", "hostname": "web01.linux.com", "status":"ok"},
		{"ip":"1.1.1.20", "hostname": "web02.linux.com", "status":"warn"},
		{"ip":"1.1.1.190", "hostname": "zabbix.linux.com", "status":"Error"},
		{"ip":"1.1.1.110", "hostname": "ansible.linux.com", "status":"Error"},
	]


	def host(request):

		return render(request, "hosts.html", {"host_list":host_list})
		
	

3) 定义url关联视图函数 

	urlpatterns = [
		path('hosts/', views.host),
	]


4) 修改login视图函数


	def login(request):
		if request.method == "GET":
			return render(request, "login.html")

		elif request.method == "POST":

			username = request.POST.get("username")
			password = request.POST.get("pwd")

			if username == "martin" and password == "redhat":
				# 跳转到新页面
				return redirect("/hosts")
			else:
				return render(request, "login.html", {"error_msg":"用户名或密码错误"})



5) 浏览器验证访问，登录界面验证成功后，即可跳转到自定义的后台管理界面；表格中显示的数据为列表USER_LIST中的数据 




示例>>>  在hosts.html界面中添加在线添加用户功能 

1) 修改模板，新增添加用户的表单

templates/hosts.html

    <h2>主机列表</h2>

    <div style="margin-bottom: 10px">
        <form action="/hosts/" method="POST">
            {% csrf_token %}
            <input type="text" name="ip" placeholder="ip地址" />
            <input type="text" name="hostname" placeholder="主机名" />
            <input type="text" name="status" placeholder="主机状态" />
            <input type="submit" value="添加" />
        </form>
    </div>


2) 编辑home视图函数，接收表单数据

app01/views.py 

		host_list = [
			{"ip":"1.1.1.10", "hostname": "tomcat.linux.com", "status":"Warning"},
			{"ip":"1.1.1.100", "hostname": "web01.linux.com", "status":"ok"},
			{"ip":"1.1.1.20", "hostname": "web02.linux.com", "status":"warn"},
			{"ip":"1.1.1.190", "hostname": "zabbix.linux.com", "status":"Error"},
			{"ip":"1.1.1.110", "hostname": "ansible.linux.com", "status":"Error"},
		]


		def host(request):

			
			if request.method == "POST":
				'''
					接收添加新的主机数据
				'''
				ip_address = request.POST.get("ip")
				hostname = request.POST.get("hostname")
				status = request.POST.get("status")
				
				'''
					拼成临时字典，追加到列表
				'''
				temp_dict = {"ip": ip_address, "hostname": hostname, "status": status}
				host_list.append(temp_dict)


			return render(request, "hosts.html", {"host_list":host_list})




模板语言：

1、模板中定义变量

	{{ 模板变量名称 }}
	
2、For循环 

	{% for 变量 in  取值列表 %}
		...
		...
		...
	{% endfor %}
	

3、模板中通过点"."的方式获取索引对应的值

	例如： 
	
		["martin", "Tome"]		python：list[1]   模板：list.1
		{"name":"martin", "age":20}		python: dict.get("name")    模板：dict.name 
		

4、条件判断 

	{% if 条件 %}
	
		条件为真执行的操作
		
	{% endif %}
	
	
	{% if 条件 %}
		条件为真的操作
	{% else %}
		条件为假的操作
	{% endif %}
		
	
		
		
		
		
		
		