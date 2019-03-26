函数 -- function 

1、形参、实参 

	作用：增强函数的灵活性 
	

示例： 生成指定位数的字符串 

	import string, random

	all_char = string.ascii_letters + string.digits + string.punctuation

	# n: 代表长度； 形参  
	
	def genString(n):
		password = ""
		for i in range(n):
			password += random.choice(all_char)
		print(password)


	if __name__ == '__main__':
		# 实参 
		genString(20)
		genString(40)


		
		
		
		
示例：计算文件的检验值  

	import hashlib

	def fileMD5(file_name):
		md5_obj = hashlib.md5()
		with open(file_name, "rb") as f_obj:
			while True:
				data = f_obj.read(8192)
				if not data:
					break
				md5_obj.update(data)

			print(md5_obj.hexdigest())


	if __name__ == '__main__':
		fileMD5("/etc/fstab")
		fileMD5("/etc/passwd")
		

		
		
		
		
示例：显示指定目录下的所有文件、子目录 

	import os

	# 接受目录名称，显示所有子目录
	
	def listDIR(dir_name):
		for i in os.walk(dir_name):
			print(i[0])

	# 接受目录名称，显示所有文件 
	
	def listFile(dir_name):
		for dir, sub_dir_name, file_list in os.walk(dir_name):
			if len(file_list) > 0:
				for file_name in file_list:
					full_file_name = os.path.join(dir, file_name)
					print(full_file_name)


	if __name__ == '__main__':

		listFile("/data")




形参的类型

	位置参数 
	默认参数
	关键字参数
	可变长参数



1) 默认参数 

	为形参设置一个默认值
		
		import string, random

		all_char = string.ascii_letters + string.digits + string.punctuation

		def genString(n=5):
			password = ""
			for i in range(n):
				password += random.choice(all_char)
			print(password)


		if __name__ == '__main__':
			genString()
			genString(10)



2) 关键字参数

	def userLogin(username, password):
		if username == "admin" and password == "123":
			print("Login ok")
		else:
			print("username or password not correct!!!!!")


	if __name__ == '__main__':

		name = "admin"
		pwd = "123"
		
		# 明确指定形参名称传递参数
		
		userLogin(password=pwd, username=name)


注意： 

	位置参数、默认参数可以同时出现在同一个函数中，要求默认参数必须写在最后
	
		def mysqlConn(ip_address, username, password="", port=3306):
			print("MySQL Server: %s, Port: %s" % (ip_address, port))



3) 可变长参数

实现方法一) 元组 


		def fun01(*args):
			print(args)
			print(type(args))
			print("----" * 10)


		if __name__ == '__main__':

			fun01("martin", "Jerry")


	将元组的元素分别作为参数传递给函数 
	
		def fun01(*args):
		print(args)
		print("----" * 10)


		if __name__ == '__main__':

			tuple_01 = ( "Martin", "Jerry")
			fun01(*tuple_01)
		


实现方法二) 字典 

		def fun01(**kwargs):
			print(kwargs)
			print(type(kwargs))
			print("---" * 10)

		if __name__ == '__main__':
			fun01()
			fun01(
				ip_address=["1.1.1.1", "1.1.1.2", "1.1.1.3"],
				port=3306, 
				username="admin@localhost",
				password="redhat"
			)


	将字典传递给函数 
	
	
		def fun01(**kwargs):
			print(kwargs)
			print(type(kwargs))
			print("---" * 10)

		if __name__ == '__main__':

			dict_01 = { "ip": "1.1.1.1", "port":3306 }

			fun01(**dict_01)


	*args, **kwargs同时使用时注意顺序 
	
			def fun01(*args, **kwargs):
				print(args)
				print(kwargs)
				print("---" * 10)

			if __name__ == '__main__':

				fun01("Martin", "Tome", "Jerry", ip="1.1.1.1", port=3306)
				fun01("Martin", "Tome", ["user01", "user02"])
				fun01(ip="1.1.1.1", port=3306)



函数的返回值 

	作用：接收函数的返回值，再函数的处理结果再次做额外的处理 

		return 结果 
	
	
	示例01：
	
		def fun01():
			print("This is fun01")
			print("END!!!!!!")
			# 定义一个返回值
			return {"name": "martin", "password": "123"}		
	
		if __name__ == '__main__':
			# 接收函数的返回值 
			result = fun01()
			print(result)

			
	示例02：return会终止函数 
	
		def fun01():
			print("This is fun01")
			print("END!!!!!!")
			return {"name": "martin", "password": "123"}
			print("-------" * 2)
			print("-------" * 2)


		if __name__ == '__main__':
			
			fun01()


	示例03：接收系统进程数， 判断 
	
	
		import os

		def procNumber():
			number = 0
			for file_name in os.listdir("/proc"):
				if file_name.isdigit():
					number += 1
			return number


		if __name__ == '__main__':
			result = procNumber()
			if result > 100:
				print("warn")
			else:
				print("ok")
			


		import os

		def procNumber():
			number = 0
			for file_name in os.listdir("/proc"):
				if file_name.isdigit():
					number += 1
			return number


		def showSysState():
			result = procNumber()
			if result > 100:
				print("warn")
			else:
				print("ok")


		if __name__ == '__main__':
			showSysState()



	示例04：获取不同目录下的不同的文件
	
	# Author: Martin

		import hashlib
		import os

		def fileMD5(file_name):
			md5_obj = hashlib.md5()
			with open(file_name, "rb") as f_obj:
				while True:
					data = f_obj.read(8192)
					if not data:
						break
					md5_obj.update(data)

				return md5_obj.hexdigest()

		def listFile(dir_name):
			files = []
			for dir, sub_dir_name, file_list in os.walk(dir_name):
				if len(file_list) > 0:
					for file_name in file_list:
						full_file_name = os.path.join(dir, file_name)
						files.append(full_file_name)
			return files

		if __name__ == '__main__':

			for file_name in listFile("/data_src"):
				dst_same_file = file_name.replace("src", "dst")

				src_file_md5 = fileMD5(file_name)
				dst_file_md5 = fileMD5(dst_same_file)
				
				if src_file_md5 != dst_file_md5:
					print("%s not same %s" % (file_name, dst_same_file))





匿名函数 ---- lambda


定义语法：

	lambda 参数1[,参数2]:返回的结果
	

		fun01 = lambda n:n ** 2

		print(fun01(10))
		print(fun01(20))


示例：sorted() 排序

	sorted(iterable, *, key=None, reverse=False)
	
		iterable：可迭代对象, 表示数据源
		reverse=False：表示升序， reverse=True， 降序
		key=	函数   根据数据里的哪些值进行排序 
		
		示例：对列表排序
		
			>>> list_01 = [ 10, 30, 234, 643, 4323 ]
			>>> sorted(list_01)
			[10, 30, 234, 643, 4323]
			>>> 
			>>> sorted(list_01, reverse=True)
			[4323, 643, 234, 30, 10]

			
		示例：默认使用字典的键排序
			>>> dict_01 = { "name": "Martin", "password": "123", "gender":"F" }
			>>> 
			>>> sorted(dict_01)
			['gender', 'name', 'password']
			>>> 
			>>> sorted(dict_01, reverse=True)
			['password', 'name', 'gender']
		
		示例：使用字典的值排序
		
			>>> sorted(dict_02.values())
			[3, 10, 50]
			>>> sorted(dict_02.values(), reverse=True)
			[50, 10, 3]

		示例：对字典的值进行排序，并返回键值对的组合
		
		>>> dict_02.items()
		dict_items([('1.1.1.1', 10), ('1.1.1.2', 3), ('1.1.1.4', 50)])

		
		# key=lambda x:x[1]， 默认循环处理可迭代对象的每个值，根据匿名函数的返回值进行排序
		
		>>> sorted(dict_02.items(), key=lambda x:x[1])
		[('1.1.1.2', 3), ('1.1.1.1', 10), ('1.1.1.4', 50)]
		
		>>> sorted(dict_02.items(), key=lambda x:x[1], reverse=True)
		[('1.1.1.4', 50), ('1.1.1.1', 10), ('1.1.1.2', 3)]






内置函数

	int(), str(), list(), tuple(), dict(), set(), bytes()
	
	id(), type(), input(), help()
	
	bin(), oct(), hex()
	
	abs() 
	
	dir()	返回一个对象的操作方法 
	
		dir(list)
		
		dir(tuple)
	
	chr(), ord()
	
	    # 将数字转换成ASCII码表中的字符
		>>> chr(97)
		'a'
		>>> chr(65)
		'A'
		>>> chr(10)
		'\n'
		
		# 将字符转换成ASCII码表中对应的数字 
		>>> ord("a")
		97
		>>> ord("A")
		65


	enumerate()
		返回索引与值的对应关系
		
		>>> for i, j in enumerate(list_01):
		...     print("索引：%s, 值: %s" %(i, j))
		... 
		索引：0, 值: king
		索引：1, 值: martin
		索引：2, 值: jerry
		
	
	max(), min(), sum()
	
		>>> list_02 = [ 11, 22, 33 ]
		>>> sum(list_02)
		66

	zip()
		返回多个可迭代对象索引相同的值的组合，数据类型是元组 
		
		>>> list_01 = [ "martin", "Jerry", "Mike" ]
		>>> list_02 = [ "bj", "sh", "wh" ]
		>>> 
		>>> zip(list_01,list_02)
		<zip object at 0x7f56db0d5048>
		>>> 
		>>> for i in zip(list_01,list_02):
		...    print(i)
		... 
		('martin', 'bj')
		('Jerry', 'sh')
		('Mike', 'wh')





































