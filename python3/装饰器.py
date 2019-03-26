装饰器：
	本质上也是函数，用于装饰其他函数
	实际作用是为其他函数添加额外的功能
	
	
原则：
	1、不能修改被装饰函数的源代码
	2、不能修改被装饰函数的调用方式 
	
	
装饰器 = 高阶函数 + 嵌套函数 
	
	
	
1、函数的本质
	
	定义函数时，像定义变量一样，在内存中开辟一段空间，在该空间中保存形成函数体的字符串，在变量名后加()的方式可以实现调用 

In [1]: def fun01():
   ...:     print("This is fun01")
   ...:     
           
In [3]: print(fun01)
<function fun01 at 0x7f6dcc4dd8c8>

In [4]: fun01()
This is fun01

可以理解为fun01只是一段内存空间的标识， fun01()在调用这段内存空间里的代码
定义时只是在内存中保存内容，内容不会真正运行，只有通过()的方式调用时，内存中的代码才会运行



def foo():
    print("This is in foo")
    bar()

def bar():
    print("This is in bar")

foo()




2、高阶函数

1) 把函数名作为实参传递给另一个函数

	def fun01():
		print("运行函数fun01的功能")

	# func_name  要求是函数名
	def fun02(func_name):             # func_name = fun01
		print("函数fun02功能开始")
		func_name()                   # fun01()   
		print("函数fun02功能结束")

	if __name__ == '__main__':
		
		fun02(fun01)
		
		
		
2) 函数返回值是另一个函数名
	
	def fun01():
		print("函数fun01实现的功能")


	def fun02(func_name):
		print("函数fun02的功能开始")
		print("函数fun02的功能结束")
		return func_name

	if __name__ == '__main__':

		'''
			1) 执行fun02()
			2) 将fun02()的返回值保存到result变量
		'''
		result = fun02(fun01)
		'''
			相当于执行fun01()函数
		'''
		result()
			
		
以上示例通过定义和原函数同样的名称的变量接收返回值，实现不改变函数的调用方式，再次运行原函数

		def fun01():
			print("显示后台管理功能")


		def fun02(func_name):
			print("用户认证功能")
			return func_name


		if __name__ == '__main__':

			fun01 = fun02(fun01)
			fun01()		

上述示例按照python语法糖的标识写：

		def fun02(func_name):
			print("用户认证功能")
			return func_name


		@fun02          #相当于执行 fun01 = fun02(fun01)     
		def fun01():
			print("显示后台管理功能")


		if __name__ == '__main__': 
			fun01()

		

3、嵌套函数 

	def fun01():
		print("fun01执行")
		def fun02():
			print("fun02执行")
		return fun02
		
		
		

	if __name__ == '__main__':

		result= fun01()
		print(result)
		result()




装饰器

示例01：为函数fun01记录执行时间

		# Author: Martin

		import time


		def logg_time(func_name):
			def wrapper():
				start_time = time.time()
				func_name()
				stop_time = time.time()
				print("函数%s的执行时间是：%s" % (func_name.__name__, stop_time - start_time))

			return wrapper

		'''
			1) 将fun01传递给logg_time,    func_name = fun01
			2) 定义函数wrapper
			3) 返回wrapper，    fun01 = wrapper
		'''

		@logg_time              # fun01=logg_time(fun01)
		def fun01():
			print("fun01开始")
			time.sleep(2)
			print("fun01结束")


		if __name__ == '__main__':
			fun01()         # 调用wrapper() 


上述示例中，fun01函数如果有参数，则在对应的装饰器内部也要定义参数接收；但由于参数个数不确定，为增加适用性，装饰器内部函数一般都采用变长参数的方法接收 


		# Author: Martin

		import time


		def logg_time(func_name):
			def wrapper(*args, **kwargs):			#  变长参数
				start_time = time.time()
				func_name(*args, **kwargs)            # 真正执行fun01()函数中的代码
				stop_time = time.time()
				print("函数%s的执行时间是：%s" % (func_name.__name__, stop_time - start_time))

			return wrapper

		'''
			1) 将fun01传递给logg_time,    func_name = fun01
			2) 定义函数wrapper
			3) 返回wrapper，    fun01 = wrapper
		'''

		@logg_time              # fun01=logg_time(fun01)            # fun01 = wrapper()
		def fun01(n):
			print("fun01开始")
			time.sleep(n)
			print("fun01结束")


		if __name__ == '__main__':
			fun01(3)         # 调用wrapper()
			
			
			
			


示例02：为函数添加用户认证功能

		# Author: Martin

		import sys

		name = "martin"
		password = "redhat"


		def authUser(func_name):
			def wrapper(*args, **kwargs):
				username = input("输入用户名： ")
				pwd = input("输入密码： ")
				if username == name and pwd == password:
					func_name()
				else:
					print("用户名或密码不正确！！！！")
					sys.exit()
			return wrapper


		def index():
			print("显示网站首页")

		@authUser
		def admin():
			print("显示管理界面")


		if __name__ == '__main__':

			admin()
			
	
	
	
示例04：当被装饰函数有返回值时的处理， 以admin函数为例


		# Author: Martin

		import sys

		name = "martin"
		password = "redhat"

		def authUser(func_name):
			def wrapper(*args, **kwargs):
				username = input("输入用户名： ")
				pwd = input("输入密码： ")
				if username == name and pwd == password:
					result = func_name()		# 接收admin()函数的返回值
					return result				# 让wrapper()函数将admin()的返回值返回 
				else:
					print("用户名或密码不正确！！！！")
					sys.exit()
			return wrapper


		def index():
			print("显示网站首页")

		@authUser
		def admin():
			print("显示管理界面")
			return "admin_page"

		if __name__ == '__main__':

			test = admin()			# 实际上调用的是wrapper()， 通过接收wrapper的返回值来接收admin()函数值 
			print(test)


