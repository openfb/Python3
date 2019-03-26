python数据类型 

	数字、字符串、Bytes、列表、元组、字典、集合
	
	
字符串 

1) 定义字符串

	被引号引起来数据
	

		str_01 = 'Hello'

		str_02 = "Martin"

		str_03 = """11111
		22222
		33333
		"""

		print(type(str_01))
		print(type(str_02))
		print(type(str_03))	


	原始字符串：
		
		作用：避免特殊的字符转义
		正则表达式
	
		win_file_name = r"d:\newdir\1.jpg"
		print(win_file_name)
	
	
	
2) 常规操作符 

	+	拼接字符串
	*	重复
	
		str_01 = "MySQL"
		str_02 = "Redis"

		print(str_01 + str_02)
		print(str_01 * 3)
		print("--" * 10)

	>, <, >=, <=, ==, != 		True  False
	
		print("a" > "b")
		print("a" > "A")
		print("ab" > "abc")
		print("ab" > "ba")


	in, not in    成员关系判断 
	
		file_name = "/etc/sysconfig/network"

		print("net" in file_name)
		print("net" not in file_name)
		print("confg" in file_name)
		
	
	len()
		str_01 = ""
		str_02 = "  "

		print(len(str_01))
		print(len(str_02))


	索引
		根据字符串的下标取单个字符 
		
		
		file_name = "/etc/sysconfig/network"

		print(file_name[0])
		print(file_name[3])
		print(file_name[-1])
		print(file_name[-2])
		
		可变类型、不可变类型
		
			不可变类型：不能通过下标的方式直接修改某个元素的值；
				字符串
				
			可变类型：通过下标的方式直接修改某个元素的值 
			
	切片 
	
		通过下标的方式取多个字符 
		注意：
			终止下标的前一个字符
		
		file_name = "/etc/sysconfig/network"

		print(file_name[0])
		print(file_name[0:2])
		print(file_name[0:3])
		print(file_name[0:4])
		print(file_name[8:14])
		print(file_name[-4:])
		print(file_name[0:10:2])
		print(file_name[::-1])
					
			
	示例：

		str_01 = "Python"
		str_01 = str_01[0:3] + "H" + str_01[-2:]
		print(str_01)	
			
	
	


字符串常用操作方法

1) 实现大小写转换

	str_01 = "mArtin"

	print(str_01.capitalize())
	print(str_01.upper())
	print(str_01.lower())


2) 判断字符串的组成结构

	str_01 = "abc"
	str_02 = "ABC"
	str_03 = "ABC?123"
	
	print(str_03.isalnum())
	print(str_01.isdigit())
	print(str_01.isalpha())
	print(str_01.islower())
	print(str_02.isupper())
	
	
3) 判断字符串开头、结尾 

		file_name = "/etc/fstab"

		print(file_name.endswith("ab"))
		print(file_name.startswith("/"))

	
4) 去除字符串中指定的字符 

		str_01 = "    Martin      "
		print(str_01.strip())
		print(str_01.lstrip())
		print(str_01.rstrip())
	
		
		str_02 = "Martin"
		print(str_02.rstrip("n"))
	
		choice = input("输入你的选择(y/n) ").strip().lower()

	
5) split()   	分割单行字符串

		str_01 = "Python is world nb language."

		print(str_01.split())       # 默认按空白空格分割字符串，返回列表
		print(str_01.split()[2])
		print(str_01.split()[-1].rstrip("."))
		print(len(str_01.split()))
		
		str_01 = "Python"
		print(str_01.split("o"))
		
		file_name = "/etc/sysconfig/network"
		print(file_name.split("/")[-1])
	
	
6) splitlines() 	分割多行字符串 

		返回一个列表，默认按回车符分割每一行 
		
		str_01 = """Python   aaa
		Redis  bbb
		MySQL  cccc
		Django  ddd
		Flask  eee
		"""

		print(str_01.splitlines())

	
7) find() 

		返回字符所在的下标，如果字符不存在， 则返回-1 

		str_01 = "Pythonh"
		print(str_01.find("h"))
		print(str_01.find("K"))
	
			if str_01.find("K") == -1: 

	
8) count( )		计数

		str_01 = "Pythonh"

		print(str_01.count("n"))
		print(str_01.count("h"))

	

9) replace( )	替换 

		str_01 = "python"

		print(str_01.replace("o", "King"))



通过for循环遍历字符串


		str_01 = "python"

		for char in str_01:
			print("字符是：%s" % char)


	示例：统计数字个数
		
		number = 0

		str_01 = "a1b2c3d9king"

		for i in str_01:
			if i.isdigit():
				number += 1

		print("数字个数：%s" % number)





示例： 生成10位随机字符 

		import string
		import random

		all_str = string.digits + string.punctuation + string.ascii_letters
		random_str = ""

		for i in range(10):
			random_str += random.choice(all_str)

		print(random_str)
	
	
	
	

示例：字符统计 

		test_str = """The Apache HTTP Server Project is an effort 
		to develop and maintain an open-source HTTP server for modern operating systems 
		including UNIX and Windows. The goal of this project is to provide a secure, 
		efficient and extensible server that provides HTTP services in sync with the current HTTP standards.
		"""


		line_number = len(test_str.splitlines())
		word_number = 0

		for line in test_str.splitlines():
			# 循环列表，每一行按空格分隔，获取第一行的单词个数
			 word_number += len(line.split())

		print("行数： %s, 单词数：%s" % (line_number, word_number))


	
	
	
	

示例：判断字符串是否为合法的变量名 

		import string

		first_char = string.ascii_letters + "_"
		all_char = string.ascii_letters + string.digits + "_"

		# 定义标志，1表示合法， 0表示不合法
		flag = 1

		test_str = input("输入字符串： ")

		# 判断第一个字符是否不合法
		if test_str[0] not in first_char:
			flag = 0
		else:
			# 从第2个字符开始判断
			for i in range(1, len(test_str)):
			   if test_str[i] not in all_char:
				   flag = 0
				   break

		# 输出结果

		if flag == 0:
			print("不合法！！！！！！！！")
		elif flag == 1:
			print("合法！！！！！！！！！")

			
示例：判断IP地址


		ip_address = input("输入IP地址： ")

		flag = 1

		if len(ip_address.split(".")) != 4:
			flag = 0
		else:
			for i in ip_address.split("."):
				if int(i) < 0 or int(i) > 255:
					flag = 0
					break


		if flag == 0:
			print("不合法！！！！")
		elif flag == 1:
			print("合法！！！！！")

			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			