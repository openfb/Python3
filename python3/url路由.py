django接收表单数据的方式

	1) request.POST.get()
		request.POST.getlist()
		
	2) request.GET.get()
	
	3) request.FILES
		request.FILES.name 	    获取文件名称 
		request.FILES.chunks()	获取文件数据，返回是个生成器
	

示例>>>   验证接收表单数据

1) 用户注册表单页面

templates/register.html 

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

    <form action="/register/" method="post" enctype="multipart/form-data">
        {% csrf_token %}
        <p>
            <input type="text" name="username" placeholder="用户名"/>
        </p>
        <p>
            <input type="password" name="pwd1" placeholder="密码"/>
        </p>
        <p>
            <input type="password" name="pwd2" placeholder="再次输入密码"/>
        </p>

        <p>
            男：<input type="radio" name="gender" value="M" />
            女：<input type="radio" name="gender" value="F" />
        </p>

        <p>
            足球<input type="checkbox" name="favor" value="football"/>
            台球<input type="checkbox" name="favor" value="taiqiu"/>
            音乐<input type="checkbox" name="favor" value="music"/>
            体育<input type="checkbox" name="favor" value="tiyue"/>
        </p>

        <p>
            <select name="city">
                <option value="bj">北京</option>
                <option value="sh">上海</option>
                <option value="wh">武汉</option>
            </select>
        </p>

        <p>
            照片：<input name="picture" type="file"/>
        </p>

        <p>
            <input type="submit" value="提交"/>
        </p>


    </form>

</body>
</html>


2) 视图函数

app01/views.py

	def register(request):
		if request.method == "POST":
			'''
				获取表单中的单个数据，例如用户名、密码、性别等数据
				方法：
					request.POST.get()
					request.GET.get()
			'''
			username = request.POST.get("username")
			pwd1 = request.POST.get("pwd1")
			pwd2 = request.POST.get("pwd2")
			gender = request.POST.get("gender")
			city = request.POST.get("city")
			print(username, pwd1, pwd2, gender,city)

			'''
				获取多个表单项数据，例如爱好
				request.POST.getlist()， 以列表的形式呈现多个数据
			'''

			favor = request.POST.getlist("favor")
			print(favor)

			'''
				接收表单上传的文件
				django使用request.FILES来获取表单获取的文件
				
				chunks方法用于以块的方式获取上传的数据；通过循环来接收数据 
			'''

			file_obj = request.FILES.get("picture")
			print(file_obj.name)

			import os
			file_name = os.path.join("upload", file_obj.name)
			f = open(file_name,"wb")
			for i in file_obj.chunks():
				f.write(i)
			f.close()


		return render(request, "regisgter.html")



3) url路由配置

urls.py  

	urlpatterns = [
		path('register/', views.register),
	]
	]


	
	
	

url匹配执行操作的两种方式

	FBV/CBV

	1、FBV 
		Function Base View
		
		url对应函数执行
		
	2、CBV
		Class Base View 
		
		url对应一个类，当客户端请求匹配该url时，执行类中对应的方法 
	
	
	
示例：CBV使用方式 

1、创建类，分别定义get,post方法

app01/views.py 

	from django.views import View

	'''
		创建继承类
	'''
	class Test(View):

		'''
			客户端请求方法为get时执行的操作
		'''
		def get(self,request):
			print("请求方法: %s" % request.method)
			return render(request,"test.html")

		'''
			客户端请求为POST时执行的操作
		'''
		def post(self,request):
			print("请求方法：%s" % request.method)
			return HttpResponse("POST提交数据后操作")	
	
	
2、定义url

urls.py 

	urlpatterns = [
		'''
			模块名称.类名称.as_view()
			固定写法
		'''
		path('test/', views.Test.as_view()),
	]	
		
	
	
	
	
======================================


url写法：

一、向指定url地址传递参数

1、通过拼接url的方式传递参数

	url地址/?参数名称=参数值&参数名称=参数值 
	
示例： 

1) 定义显示主机概要信息的函数

app01/views.py 


	'''
		定义显示主机概要信息的函数
	'''
	def comment(request):
		host_info = {
			"1": "主机A",
			"2": "主机B",
			"3": "主机C",
		}
		return render(request, "host_comment.html", {"host_info": host_info})


templates/host_comment.html 

	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Host Comment</title>
	</head>
	<body>

		'''
			定义ul列表显示主机
		'''
		<ul>
			{% for key, val in host_info.items %}
				'''
					每个主机的超链接，同时将主机对应的ID传递给/detail视图函数
				'''
				<a target="_blank" href="/detail/?hid={{ key }}&hname={{ val }}"><li>{{ val }}</li></a>
			{% endfor %}
		</ul>

	</body>
	</html>		
		
		

2) 定义显示主机详细信息

app01/views.py 		
		
	'''
		显示主机详细信息 
	'''
	def detail(request):
		hid = request.GET.get("hid")
		hname = request.GET.get("hname")
		return render(request, "host_detail.html",{"hname":hname})
		
		
templates/host_detail.html 

	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>host detail</title>
	</head>
	<body>

		<h1>主机{{ hname }}详细信息</h1>

	</body>
	</html>
	
	
3) url设置 

urlpatterns = [
    path("comment/", views.comment),
    path("detail/", views.detail),
]






2、通过正则表达式传递信息  

1、通过( )圆括号分组的方式传递参数 

示例：

修改上述显示主机概要信息模板

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Host Comment</title>
</head>
<body>

    <ul>
        {% for key, val in host_info.items %}
			'''
				将字典中的key作为参数传递给不同的url, 后述url的定义以正则表达式来匹配请求
			'''
            <a href="/detail_{{ key }}"><li>{{ val }}</li></a>
        {% endfor %}
    </ul>

</body>
</html>



1) 修改url定义，表示以正则分组的形式接收参数

from django.urls import path,re_path

urlpatterns = [
    path("comment/", views.comment),
	'''
		(\d+)表示数字 
	'''
    re_path("detail_(\d+)/", views.detail),
]


2) 定义detail函数，接收处理参数

app01/views.py 

	'''
		为函数定义一个形参hid，名称可自定义
		用于接收url通过正则分组传递过来的参数
		该形参只接收传递过来的正则的第一个分组的数据，如果url正则中有多个分组，需要定义多个形参依次接收参数
	'''
	def detail(request, hid):
		return render(request, "host_detail.html", {"hid": hid})
	

	同样，可以通过变长参数的方式接收参数
	
	def func(request, *args):
		pass
	
	

3) 显示主机详细信息的模板

templates/host_detail.html 

	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>host detail</title>
	</head>
	<body>

		<h1>主机{{ hid }}详细信息</h1>

	</body>
	</html>	



通过正则表达式自定义分组(?P<自定义组名>)的方式传递参数 


示例： 

urls.py 

	urlpatterns = [
		re_path("detail_(?P<username>\w+)_(?P<password>\d+)/", views.user_detail),
	]

app01/views.py 

	'''
		形参名称要与正则自定义的组名一致
	'''
	def user_detail(request, password, username):
		str = "<h1 style='color: blue'>用户名：%s, 密码: %s</h1>" % (username, password)
		return HttpResponse(str)


	同样函数也可以通过变长参数的方式接收
	
	
	def user_detail(request, **kwargs):
		str = "<h1 style='color: green'>用户名：%s, 密码: %s</h1>" % (kwargs["username"], kwargs.get("password"))
		return HttpResponse(str)


		
		
		
url路由分发

	所有url对应关系写在项目目录下，当url过多时，会导致混乱；此时可以在不同的app下创建不同的urls.py文件，对应保存当前app下的路径关系，在项目目录下通过include的方式引用即可
	
示例：
 

1) 定义redis app下的url
 
redis/urls.py 

	from django.contrib import admin
	from django.urls import path,re_path,include
	from redis import views

	urlpatterns = [
		path("login/", views.login),
	]

2) 定义mongodb app下的url 

mongodb/urls.py 
	
	from django.contrib import admin
	from django.urls import path,re_path,include
	from mongodb import views

	urlpatterns = [
		path("login/", views.login),
	]		
		

3) 项目目录下引用 

project01/urls.py 

	from django.contrib import admin
	from django.urls import path,re_path,include
	from app01 import views

	urlpatterns = [
		path('admin/', admin.site.urls),
		'''
			当用户访问的URL地址为/redis时，则再次通过redis app下的urls.py进行下级匹配
			当用户访问的URL地址为/mongodb时，则再次通过mongodb app下的urls.py进行下级匹配
		'''
		path("redis/", include("redis.urls")),
		path("mongodb/", include("mongodb.urls")),
	]
	

		
		
		

		
url命名

	Django在定义url对应关系时，可以为url对应关系设置一个自定义的名称，主要用于方便生成或引用url地址 
	

示例01：引用url地址	
	
定义url名称 

from django.contrib import admin
from django.urls import path,re_path,include
from redis import views

urlpatterns = [
    path("login/", views.login),
	'''
		name=参数用于定义url对应关系名称
	'''
    re_path("register/", views.register, name="redis_user_register"),
    re_path("register/(\d+)/", views.register, name="redis_user_register"),
]
		

		
在模板语言中引用

	1) url中不包括正则表达式时
	
	<form action={% url "redis_user_register" %} method="POST">
		...
		...
	</form>

	2) url中包括正则表达式时，通过名称引用时需要传递对应的参数
			
	<form action={% url "redis_user_register" 100 %} method="POST">
		...
		...
	</form>		
		
		
	3) 完成引用当前请求相同的url地址，可以通过request请求中的path_info变量

    <form action={{ request.path_info }} method="POST">
		...
		...
	</form>
		
		
		
		
		
示例02：利用reverse反转生成新的url地址 

		
url命名：

    re_path("register/", views.register, name="redis_user_register"),

    re_path("register/(\d+)/(\d+)/", views.register, name="redis_user_register"),

    re_path("register/(?P<id01>\d+)/(?P<id02>\d+)/", views.register, name="redis_user_register"),

		
视图函数中引用生成新的url地址 

redis/views.py 

	def register(request, *args, **kwargs):
		'''
			导入reverse模块
		'''
		from django.urls import reverse
		
		'''
			方式一：直接引用不包括正则表达式的url
		'''
		new_url = reverse("redis_user_register")
		
		'''
			方式二：引用以( )直接分组的正则表达式
			需要通过args=( )传递参数
		'''
		
		new_url = reverse("redis_user_register", args=(11,22))
		
		'''
			方式三：引用以(?<组名>)自定义分组的正则表达式
			需要通过kwargs传递参数
		'''
		
		new_url = reverse("redis_user_register", kwargs={"id01": 11, "id02": 22})
		
		
		print(new_url)

	
