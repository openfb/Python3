python基础语法 


1、输出语句的使用 

1) 引号的使用 

	print("Hello, martin")

	print('Hello, martin')

	# 使用三引号，
	#     输出多行内容
	#     注释

	print("""first line
	two line
	three line""")


	print('''Hello, Martin!!!!''')
	print("""Hello, Martin!!!!""")

	print("It's a python demo")

	print('It is a "python" demo')

	print("我爱北京天安门！！！！！！！！！！！！！！")


python2与python3的区别：

	1) print语法不同，python3需要加()
	2) python2默认使用的字符集ASCII码,  # encoding: utf8
	   python3默认使用的字符集Unicode 
	   
	   
	
2) 输出变量的值 

	username = "root"
	password = "redhat"

	print(username)

	print("my name is ", username, "my password is", password)
	print("my name is " + username + "my password is " + password)		
	
	
3) 格式化输出 

		
	username = "root"
	password = "redhat"

	print("my name is %s" % username )
	print("my name is '%s'" % username)
	print("my name is %s, my password is %s" % (username, password))
	
	
	常用的格式化字符：
		%s    字符串 	通用 
		%d	  数字，整数 
		
			number_01 = 123
			number_02 = "456"
			number_03 = 3.9415

			print("It is %d" % number_01)
			print("It is %d" % number_03)
		
		%f 	  浮点数，小数 
		
			number_01 = 123
			number_02 = 3.948915
			number_03 = 3.9489151111111111

			print("It is %f" % number_01)
			print("It is %f" % number_02)
			print("It is %f" % number_03)


			print("It is %.2f" % number_02)

		
		
		%%		输出%本身
		
			number = 50

			# This is 50%

			print("This is %d%%" % number)  
		
		
		
		username = "root"
		password = "redhat"

		sql_01 = "select * from tb01 where username='%s' and password='%s'" % (username, password)
		print(sql_01)
	
	
	
	
2、注释 

	1) 单行注释 
	
		# username = "root"		ctrl + / 
	
	2) 多行注释   三引号 
	
		'''
			以下是连接MySQL数据库
		'''
	
	
	
	
3、变量的定义 

	name = "Martin"
	
	变量名称规范：
		1) 字母、数字、下划线_ 
		2) 只能以字母、下划线_开头
		3) 不能与python关键字冲突      print   if  for   while   else 
	
			number_01, number_02 = 10, 20

			print(number_01)
			print(number_02)	
						
			a = 10
			b = 20

			a, b = b, a
			print(a)
			print(b)
	
	交互式变量赋值
		
		username = input("输入用户名： ")
		
		注意：
			返回的结果是字符串

		print("用户名： %s" % username)
	
	
	python2与python3的区别：
		input("提示信息")
		raw_input("提示信息")
			>>> username = raw_input("用户名>>> ")

			
删除变量

	name = "Martin"
	print(name)

	del name
	print(name)

			
		
python变量与其他语言不同之处：

	1) 弱类型
	2) 地址引用类型 
		
		number_01 = 10
		number_02 = 10

		print(id(number_01))
		print(id(number_02))

		number_01 = 100
		number_02 = number_01
		
		print(id(number_01))
		print(id(number_02))


内置函数：
	id()		返回变量的内存地址 
	type()		返回变量的类型 
	
	
		
内存使用机制 

	每个变量定义后，会在内存中开辟一段空间，这段空间对应存在一个引用计数器，变量被调用一次，引用计数器会自动增加；
	当python解释器检测到一段内存的引用计数器为0后，会自动清理该内存
	



4、变量的类型：

	数字、字符串、列表、元组、字典、集合、Bytes


数字 

	number_01 = 100
	print(type(number_01))

	number_02 = 3.14
	print(type(number_02))

	number_03 = 10+20j
	print(type(number_03))	


数学运算符 

	>>> a = 10
	>>> b = 4
	>>> a + b
	14
	>>> a - b
	6
	>>> a * b
	40
	>>> a ** b
	10000
	>>>
	>>> a / b
	2.5
	>>> a // b
	2
	>>> a % b
	2


	>>> a = 10
	>>> a = a + 1
	>>> a
	11
	>>> a += 1
	>>> a
	12
	>>>


比较运算符 

	==, !=, >, >=, <=, < 
	
逻辑运算符 

	and, or, not  

	>>> a = 10
	>>>
	>>>
	>>> a > 20 and 1 < 2
	False
	>>>
	>>> a > 20 or 1 < 2
	True
	>>>
	>>> not a > 20
	True
	>>>


数制转换

	>>> a = 10
	>>> bin(a)
	'0b1010'
	>>> oct(a)
	'0o12'
	>>> hex(a)
	'0xa'
	>>>



生成随机数的模块 

	>>> import random
	>>> random.randint(0, 10)
	7
	>>> random.randint(0, 10)
	9
	>>> random.randint(0, 10)
	2
	>>> random.randint(0, 10)
	3
	>>> random.randint(0, 10)
	6	
	
	

示例：四则运算 


	number_01 = int(input("输入第1个数字： "))
	number_02 = int(input("输入第2个数字： "))

	print("%s + %s = %s" % (number_01, number_02, number_01 + number_02))
	print("%s - %s = %s" % (number_01, number_02, number_01 - number_02))
	print("%s * %s = %s" % (number_01, number_02, number_01 * number_02))
	print("%s / %s = %s" % (number_01, number_02, number_01 / number_02))
	print("%s // %s = %s" % (number_01, number_02, number_01 // number_02))
		
	
	
	
	
5、逻辑控制语句 

	同级代码要有相同缩进，默认4个空格 
	
	

条件判断 --- if

1) 

if 条件:
    操作语句
	操作语句 
	
	

	if 1 < 2:
	    print("AAA")
	    print("BBB")


	# 只要数字不等于0，条件为真

	number = 10
	if number:
	   print("AAA")
	   print("BBB")


	number = 10
	if not number:
	    print("AAA")
	    print("BBB")


	# True, False 首字母全是大写

	if True:
		 print("AAA")



2) if .... else 

	number = 100

	if number < 20:
		print("AAAA")
	else:
		print("BBBB")


		
3) if ... elif ... elif .... else 


	number = int(input("Enter number: "))

	if number > 10:
		print("AAA")
	elif number > 30:
		print("BBBB")
	elif number > 40:
		print("CCCC")
	else:
		print("DDDD")


4) 嵌套if 

	age = int(input("输入你的年龄： "))

	if age <= 18:
		gender = input("输入你的性别： ")
		if gender == "M":
			print("准备入队")
		else:
			print("睡吧")
	else:
		print("回家洗洗睡吧")
		
	
	
	
	
	

循环
	for 
	while 

	
for循环：

	for 变量 in 取值:
		操作语句
		操作语句
	

	for i in range(5):
		print("第%s次循环开始" % i)
		print("第%s次循环结束" % i)
		print("-----------------")


中断循环：

	break		中断整体循环

		for i in range(5):
			print("第%s次循环开始" % i)
			if i == 3:
				break
			print("第%s次循环结束" % i)
			print("-----------------")

	
	continue	中断本次循环

		for i in range(5):
			print("第%s次循环开始" % i)
			if i == 3:
				continue
			print("第%s次循环结束" % i)
			print("-----------------")



while循环

	while 条件:
		操作语句
		操作语句
		
			i = 1

			while i <= 4:
				print("第%s次循环开始" % i)
				print("第%s次循环结束" % i)
				print("-----------------")
				i += 1


	while True:
		操作语句
		操作语句



示例： 实现数制转换 


	import sys

	number = int(input("输入数字： "))

	menu = """
	1、二进制
	2、八进制
	3、十六进制
	4、退出

	输入你的选择：d
	"""

	'''
		循环判断用户的选择，根据不同的选择做不同的响应 
	'''

	while True:
		choice = int(input(menu))

		if choice == 1:
			print("数字%s的二进制形式：%s" % (number, bin(number)))
		elif choice == 2:
			print("数字%s的八进制形式：%s" % (number, oct(number)))
		elif choice == 3:
			print("数字%s的十六进制形式：%s" % (number, hex(number)))
		else:
			print("谢谢")
			sys.exit()




作业：

1、人机猜数 	[3]





	

















	

		
	
	






