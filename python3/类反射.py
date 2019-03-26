反射器  Reflactor

	作用：
		将用户输入的字符串与类中的属性或者方法映射，实现根据用户输入的字符串实现调用、添加、删除属性或方法
		

		hasattr(obj, str_name)：用于判断类中是否有用户所输入字符串所对应的属性或者方法
		getattr(obj, str_name): 获取用户所输入的字符串与obj对象内部对应的属性或者方法的内存地址
		setattr(obj, "x", v): 用于向类中动态添加属性或者方法
		delattr(obj, str_name)：用于删除用户所输入的字符串与obj对象内部对应的属性和方法


示例01

	根据hasattr()判断是否存在对应的对象，根据getattr()获取对象的内存地址调用 
	
		class Test(object):

			def __init__(self, name):
				self.name = name

			def get_password(self,password):
				print("用户%s的密码是%s" % (self.name, password))


		p1 = Test("Martin")

		choice = input(">>> ")

		# 判断类中是否存在与字符串同名的属性或者方法
		if hasattr(p1, choice):
			# 获取与字符串同名的类属性、方法的内存地址
			result = getattr(p1, choice)
			result("redhat")
		else:
			print("无此方法或属性")




	
示例02：

	通过setattr()方法向类中动态添加方法，用户输入的字符串作为最后的方法名调用 
	

		def get_age(self, age):
			print("%s的年龄是%s" % (self.name, age))


		class Test(object):

			def __init__(self, name):
				self.name = name

			def get_password(self,password):
				print("用户%s的密码是%s" % (self.name, password))


		p1 = Test("Martin")

		choice = input(">>>> ")

		if hasattr(p1, choice):
			result = getattr(p1,choice)
			result("redhat")
		else:
			# 先通过setattr()将方法添加到类，再调用
			'''
				假设用户输入的字符串为king
				setattr(p1, "king", get_age)  
				属性名：king   值：get_age函数       
			'''
			setattr(p1, choice, get_age)
			print("---" * 10)

			# 直接使用用户输入的字符串作为方法名调用方法
			# p1.king(p1, "20")

			result_02 = getattr(p1, choice)
			result_02(p1,"20")





	
	
	
示例03：

	根据delattr()删除类中对象现有的属性
	


		class Test(object):

			def __init__(self, name):
				self.name = name

			def get_password(self,password):
				print("用户%s的密码是%s" % (self.name, password))


		p1 = Test("Martin")
		print(p1.name)
		print("---" * 10)

		choice = input(">>> ")
		if hasattr(p1, choice):
			# 删除p1对象与字符串同名的属性
			delattr(p1, choice)
			print(p1.name)


