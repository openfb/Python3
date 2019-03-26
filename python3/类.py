类  Class

	编程思想 
	
	类型：
		面向过程的编程语言
			C, C++, C#
			开发周期长
					
		面向对象的编程语言
			Java, Python
			类 class 


类  Class 

	编程的写法
	作用：
		1、实现代码重复用 
		2、一定程度加强代码的安全性
	

1、定义类

1) 新式类

	class 类名称(object)：
		....
		....
		....

	类名称的规范：
		
		全部首字母大写
		
	
属性 ---- 变量
方法 ---- 函数



示例：定义类、实例化

	class Test(object):
		name = "Martin"
		age = 34

		def fun01(self):
			print("这是类Test中的第一个方法")

		def fun02(self):
			print("这是类Test中的第二个方法")


	# 实例化

	p1 = Test()
	print(p1.name)
	p1.name = "Jerry"
	print(p1.name)

	print("---" * 10)

	p2 = Test()
	print(p2.name)



示例02：通过self形参调用类属性


	class Test(object):
		name = "Martin"
		age = 34

		def fun01(self):
			print("名字：%s, 年龄: %s" % (self.name, self.age))

		def fun02(self):
			print("这是类Test中的第二个方法")


	# 实例化

	p1 = Test()
	p1.fun01()

		


属性

	根据定义方式及调用方式不同
	类型：
		公有属性
		私有属性
		内置属性
		

1、公有属性

	通过实例化对象、类名的方式调用 


		class Test(object):

			name = "Martin"
			age = 34

			def fun01(self):
				print("名字：%s, 年龄: %s" % (self.name, self.age))


		# 实例化

		p1 = Test()
		print(p1.name)
		# 只对本实例对象生效
		p1.name = "User01"
		print(p1.name)

		print("---" * 10)

		print(Test.name)
		# 对后续所有实例生效
		Test.name = "Mike"

		p2 = Test()
		print(p2.name)

		print("---" * 10)

		p3 = Test()
		print(p3.name)




2、私有属性 

	定义：
		属性名前加两个下划线 
		
	调用：
		1) 不会分配给具体的某一个实例化对象   
		2) 无法在类外部调用、只能在类内部调用  
		
		import pymysql

		class DB(object):
			ip = "10.100.100.252"
			user = "admin"
			__password = "redhat"
			database = "testdb"


			def dbConn(self):
				conn = pymysql.connect(host=self.ip, user=self.user, password=self.__password, database=self.database)
				return conn


		p1 = DB()
		db_conn = p1.dbConn()
		print(db_conn)
	
	
3、内置属性

	名称: __属性名称__
	
	class Test(object):

		'''
			这是我的第一个类
		'''

		name = "Martin"
		age = 34

		def fun01(self):
			print("名字：%s, 年龄: %s" % (self.name, self.age))


	# 实例化

	p1 = Test()
	print(p1.__module__)
	print(p1.__class__)
	print(p1.__doc__)


		
	
		
方法

	根据定义方式及调用方式不同
	
	类型：
		公有方法
		私有方法
		类方法
		静态方法
		属性方法 
		
1、公有方法 

	通过实例化对象的方式调用 

		class Test(object):

			name = "Martin"

			def fun01(self):
				print("名字：%s" %(self.name))



		p1 = Test()
		p1.fun01()


2、私有方法

	定义：在方法名称前加两个下划线 __方法名称 
	
	调用：只能在类内部调用  
	

		class Test(object):

			name = "Martin"

			# 定义一个私有方法
			def __fun01(self):
				print("fun01为私有方法")

			def fun02(self):
				print("名字：%s" %(self.name))
				# 调用私有方法
				self.__fun01()
				
		p1 = Test()
		p1.fun02()




		import pymysql

		class DB(object):
			ip = "10.100.100.252"
			user = "admin"
			__password = "redhat"
			database = "testdb"


			def __dbConn(self):
				conn = pymysql.connect(host=self.ip, user=self.user, password=self.__password, database=self.database)
				return conn

			def selectData(self):
				db_conn = self.__dbConn()
				cr = db_conn.cursor()
				cr.execute("select * from user_info")
				data = cr.fetchall()
				print(data)
				cr.close()
				db_conn.close()


		p1 = DB()
		p1.selectData()




3、类方法 

	可以通过类名.方法名称的方式调用 
	
	方法1) 通过classmethod函数转换
	
		class Test(object):

			name = "Martin"

			def fun01(self):
				print("名称：%s" % self.name)

			# 将fun01定义为类方法，保存到f1中
			f1 = classmethod(fun01)


		p1 = Test()
		p1.f1()

		print("---" * 10)

		Test.f1()
	
	
	方法2) 通过装饰器

	
		class Test(object):

			name = "Martin"

			# 通过装饰器，将其装饰为一个类方法
			@classmethod
			def fun01(self):
				print("名称：%s" % self.name)



		Test.fun01()




4、静态方法

	定义一个静态方法后，该方法无法再调用类中的其他属性、方法；相当该方法和类失去了关联 

	通过装饰器定义静态方法
	
		class Test(object):

			name = "Martin"

			@staticmethod
			def fun01():
				print("静态方法示例")


		p1 = Test()
		p1.fun01()

		print("---" * 10)

		Test.fun01()
	



5、属性方法 

	相当于把方法定义为类中的一个属性，调用时不需要加()可直接调用 
	
	class Test(object):

		@property
		def fun01(self):
			print("fun01为属性方法")


	p1 = Test()
	p1.fun01



	
	
构造方法/构造函数 

	1) 名称固定为__init__(self)
	2) 类实例化自动执行 
	
	作用：
		实现为类的中属性动态赋值
		
	class Test(object):

		def __init__(self, name, age):
			self.name = name
			self.age = age

		def fun01(self):
			print("名称：%s, 年龄: %s" %(self.age, self.age))


	p1 = Test("Martin", 32)
	p1.fun01()

	p2 = Test("Mike", 100)
	p2.fun01()




	class DB(object):

		def __init__(self,host,user,password,database):
			self.host = host
			self.user = user
			self.password = password
			self.database = database

		def dbConn(self):
			import pymysql
			conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
			return conn


	p1 = DB("10.100.100.252", "admin", "redhat", "testdb")
	db_conn = p1.dbConn()
	print(db_conn)





继承、方法重写 

1、继承 

语法：

class 类名称(父类):
	....
	
			
		class Test_01(object):

			ip = "1.1.1.1"
			password = "redhat"

			def fun01(self):
				print("ssh远程连接%s" % (self.ip))


		class Test_02(Test_01):

			def fun02(self):
				print("IP地址：%s, 密码：%s" % (self.ip, self.password))


		p1 = Test_02()
		p1.fun02()
	
	
2、方法重写 

		class Test_01(object):

			ip = "1.1.1.1"
			password = "redhat"

			def fun01(self):
				print("基于密码认证ssh远程连接%s" % (self.ip))


		class Test_02(Test_01):

			def fun01(self):
				print("基于密钥认证SSH远程连接%s" % (self.ip))



		p1 = Test_02()
		p1.fun01()

		print("---" * 10)

		p2 = Test_01()
		p2.fun01()
	
	
	
	


super()函数的使用 


方法1):

		class Test_01(object):

			def __init__(self, username, password):
				self.username = username
				self.password = password

			def fun01(self):
				print("用户名：%s, 密码:%s" % (self.username, self.password))


		class Test_02(Test_01):

			def __init__(self, username, password, role):
				'''
					通过super()函数调用父类的构造函数为username, password赋值
					super(子类名称,self).__init__(参数1，参数2)
				'''
				super(Test_02, self).__init__(username, password)
				self.role = role


		p1 = Test_02("king", "123", "ZhanShi")

		p1.fun01()






方法2) 

	class Test_01(object):

		def __init__(self, username, password):
			self.username = username
			self.password = password

		def fun01(self):
			print("用户名：%s, 密码:%s" % (self.username, self.password))


	class Test_02(Test_01):

		def __init__(self, username, password, role):
			'''
				调用父类的构造函数为username, password赋值
			'''
			Test_01.__init__(self, username, password)
			self.role = role


	p1 = Test_02("king", "123", "ZhanShi")

	p1.fun01()	
		
	
	



示例：用户管理(登录、注册、密码修改功能)功能 

		import pymysql
		import sys

		class UserManager(object):

			# 为数据库连接参数赋值
			def __init__(self, ip, user, password, database):
				self.ip = ip
				self.user = user
				self.password = password
				self.database = database

			# 连接数据库返回数据库连接对象
			def dbConn(self):
				conn = pymysql.connect(host=self.ip, user=self.user, password=self.password, database=self.database)
				return conn

			def userLogin(self):
				username = input("用户名：")
				password = input("密码： ")

				# 获取连接，创建游标
				db_conn = self.dbConn()
				cr = db_conn.cursor()
				user_login_sql = "select * from user_info where name='%s' and password='%s'" % (username, password)

				result = cr.execute(user_login_sql)

				if result == 1:
					print("登录成功")
				else:
					print("用户名或密码错误")

				cr.close()
				db_conn.close()



			def userRegister(self):

				# 获取连接，创建游标
				db_conn = self.dbConn()
				cr = db_conn.cursor()

				# 获取用户名

				while True:
					username = input("用户名： ")
					select_user_sql = "select name from user_info where name='%s'" % username

					result = cr.execute(select_user_sql)
					if result > 0:
						print("用户名%s存在" % username)
						continue
					else:
						break

				# 获取密码

				while True:
					pwd1 = input("密码： ")
					pwd2 = input("再次输入密码： ")
					if pwd1 == pwd2:
						break
					else:
						print("密码不一致！！！！")
						continue

				# 向后台数据库保存用户名、密码

				save_user_sql = "insert into user_info(name, password) values('%s','%s')" % (username, pwd1)

				cr.execute(save_user_sql)
				db_conn.commit()

				print("用户%s注册成功！！！" % username)

				cr.close()
				db_conn.close()

		if __name__ == '__main__':

			p1 = UserManager(ip="10.100.100.252", user="admin", password="redhat", database="testdb")


			menu = """
			1、用户登录
			2、用户注册
			3、退出
			
			选择》》》》  
			"""

			while True:
				choice = input(menu)
				if choice == "1":
					p1.userLogin()
				elif choice == "2":
					p1.userRegister()
				elif choice == "3":
					sys.exit()
				else:
					print("输入有误")






