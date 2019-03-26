字典 --- dict 	可变类型 

1) 定义 

	被定义在{  }的数据， 以key-values键值对存储数据，值可以是任何类型
	
		key键：惟一 
		值：可以是任意类型 

	dict_01 = { "id":"001", "username": "admin", "password": "redhat" }
	print(type(dict_01))
	print(len(dict_01))


	dict_02 = {
		"web": [ "1.1.1.1", "1.1.1.2", "1.1.1.3" ],
		"mysql": [ "1.1.1.4", "1.1.1.5" ]
	}

	print(type(dict_02))
	print(len(dict_02))


	dict_03 = {
		1: {"id":"001", "name":"root@localhost"},
		2: {"id":"002", "name":"admin@localhost"},
		3: {"id":"002", "name":"admin@%"}
	}

	print(type(dict_03))
	print(len(dict_03))



2) 获取数据 --- 通过key获取


		dict_01 = { "id":"001", "username": "admin", "password": "redhat" }

		print(dict_01["username"])
		print(dict_01["password"])

		print("---" * 10)


		dict_02 = {
			"web": [ "1.1.1.1", "1.1.1.2", "1.1.1.3" ],
			"mysql": [ "1.1.1.4", "1.1.1.5" ]
		}

		print(dict_02["mysql"][-1])
		print(dict_02["web"][1])

		print("---" * 10)



		dict_03 = {
			1: {"id":"001", "name":"root@localhost"},
			2: {"id":"002", "name":"admin@localhost"},
			3: {"id":"002", "name":"admin@%"}
		}

		print(dict_03[3]["name"])



3) 修改字典中的数据 

		dict_01 = { "id":"001", "username": "admin", "password": "redhat" }

		dict_01["username"] = "King"

		print(dict_01)

		print("---" * 10)



4) 添加数据 

		dict_01 = { "id":"001", "username": "admin", "password": "redhat" }
		
		'''
			不存在的键，表示添加数据 
		'''
		dict_01["role"] = "管理员"

		print(dict_01)


		dict_01 = {}

		dict_01["id"] = 1

		print(dict_01)


5) 删除单个元素

		dict_04 = {
			1: ("admin", "king"),
			2: ("user01", "user02")
		}

		del dict_04[1]

		print(dict_04)
		
		
字典操作方法：

1、get( )	获取单个数据 

	如果key不存在， 默认返回None

	dict_01 = { "id":"001", "username": "admin", "password": "redhat" }


	print(dict_01.get("username", "未知"))

	print(dict_01.get("king", "未知"))
		
		
		
2、keys(), values(), items()

	dict_01 = { "id":"001", "username": "admin", "password": "redhat" }


	print(dict_01.keys())			# 以列表的形式返回所有的key
	print(dict_01.values())			# 以列表的形式返回所有的values
	print(dict_01.items())			# 以列表的形式返回所有key-values的组合
			
		

3、pop( )

	删除并返回指定key的值 
	
	In [12]: dict_01 = { "id":"001", "username": "admin", "password": "redhat" }

	In [13]: 

	In [13]: dict_01.pop("password")
	Out[13]: 'redhat'

	In [14]: print(dict_01)
	{'id': '001', 'username': 'admin'}



通过for循环遍历的4种方法 

方法1)

	for k in dict_01:
		print("键是%s, 值是%s" % (k, dict_01.get(k)))
    		
方法2) 

	for k in dict_01.keys():
		print("键：%s" % k)

方法3) 

	for v in dict_01.values():
		print("值：%s" % v)

			
方法4) 

	for i in dict_01.items():
		print("键是: %s, 值是: %s" % (i[0], i[1]))

	for k,v in dict_01():
		print("key is : %s , value is : %s" % (k,v))
		
		
		
示例：统计IP出现的次数 		
		
	ip_count = {}

	ip_address = """1.1.1.1
	1.1.1.1
	1.1.1.1
	1.1.1.2
	1.1.1.2
	1.1.1.3
	1.1.1.3
	1.1.1.3
	1.1.1.3
	1.1.1.3
	"""

	for ip in ip_address.splitlines():
		# IP地址在字典中没有，赋默认值为1
		if ip not in ip_count.keys():
			ip_count[ip] = 1
		# IP存在，次数加1
		else:
			ip_count[ip] = ip_count[ip] + 1

	# 输出结果

	for k, v in ip_count.items():
		print("IP： %s, 次数：%s" % (k ,v))




示例： 实现用户登录、注册功能 	{ "用户名": "密码" }

	# Author: Martin

	import sys

	user_info = {}

	menu = """
	1、注册
	2、登录
	3、退出

	选择>>>>  
	"""

	while True:
		choice = input(menu)
		if choice == "1":
			# 用户名，存在重新输入；不存在
			while True:
				username = input("输入用户名： ")
				# 判断用户名存在
				if username in user_info.keys():
					print("用户名己注册")
					continue
				else:
					break

			# 提示输入密码，判断密码是否一致
			while True:
				pwd_01 = input("输入密码: ")
				pwd_02 = input("再次输入密码: ")
				if pwd_01 == pwd_02:
					# 保存用户数据
					user_info[username] = pwd_01
					print("用户%s注册成功！！！" % username)
					break
				else:
					print("密码不一致！！！！！！")
					continue
		elif choice == "2":
			username = input("用户名： ")
			password = input("密码：　")
			if password == user_info.get(username):
				print("登录成功！！！！")
			else:
				print("用户名、密码错误！！！！")
		elif choice == "3":
			sys.exit()
		else:
			print("输入错误！！！！！！！！！")


