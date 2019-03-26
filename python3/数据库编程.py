数据库编程

	支持数据库类型：
		MySQL, Oracle, sqllite
		
	实现的方式：
		1) 连接数据库，执行原生sql语句  
		2) ORM的方式， 以类的方式
		
	连接MySQL：
		pymysql模块 
		
		> pip install pymysql
		
	操作流程：
	
		1) 连接数据库，返回连接对象 
		2) 创建游标cursor对象
		3) 执行sql语句，返回结果
		4) 关闭游标cursor
		5) 关闭数据库连接
		
	
示例01：执行insert操作 

		# Author: Martin

		import pymysql
		import sys

		# 创建数据库连接
		try:
			conn = pymysql.connect(host="172.16.8.252", user="admin", password="redhat", database="testdb")
		except Exception as e:
			print("数据连接信息不正确")
			sys.exit()

		# 创建游标
		cr = conn.cursor()

		user_dict = {"Jerry": "123", "Tome": "456", "Mike": "798"}

		for k, v in user_dict.items():
			insert_sql = "insert into user_info(name, password) values('%s', '%s')" %(k,v)
			cr.execute(insert_sql)

			# 除了查询select外，所有修改的操作必须提交
			conn.commit()

		cr.close()
		conn.close()




示例02：执行delete操作

	# Author: Martin

	import pymysql
	import sys

	# 创建数据库连接
	try:
		conn = pymysql.connect(host="172.16.8.252", user="admin", password="redhat", database="testdb")
	except Exception as e:
		print("数据连接信息不正确")
		sys.exit()

	# 创建游标
	cr = conn.cursor()

	delete_sql = "delete from user_info where id=2"

	cr.execute(delete_sql)

	# 除了查询select外，所有修改的操作必须提交
	conn.commit()

	cr.close()
conn.close()



示例03：执行select操作：

1)	获取数据的返回条数 

		# Author: Martin

		import pymysql
		import sys

		# 创建数据库连接
		try:
			conn = pymysql.connect(host="172.16.8.252", user="admin", password="redhat", database="testdb")
		except Exception as e:
			print("数据连接信息不正确")
			sys.exit()

		# 创建游标
		cr = conn.cursor()

		select_sql = "select * from user_info where name='martin'"

		result = cr.execute(select_sql)
		'''
			result保存的是返回的数据的条数
		'''
		print(result)
		print("---" * 10)

		cr.close()
		conn.close()



2) 

		# Author: Martin

		import pymysql
		import sys

		# 创建数据库连接
		try:
			conn = pymysql.connect(host="172.16.8.252", user="admin", password="redhat", database="testdb")
		except Exception as e:
			print("数据连接信息不正确")
			sys.exit()

		# 创建游标
		cr = conn.cursor()

		select_sql = "select * from user_info where name='martin'"

		result = cr.execute(select_sql)
			# Author: Martin

		import pymysql
		import sys

		# 创建数据库连接
		try:
			conn = pymysql.connect(host="172.16.8.252", user="admin", password="redhat", database="testdb")
		except Exception as e:
			print("数据连接信息不正确")
			sys.exit()

		# 创建游标
		cr = conn.cursor()

		select_sql = "select * from user_info where name='martin'"

		result = cr.execute(select_sql)
		
		'''
			通过游标的fetchone(), fetchall(), fetchmany()获取数据 
			fetchmany(2)
		'''
		
		print(cr.fetchall())

		cr.close()
		conn.close()




==================================
python虚拟环境 

	作用：避免开发多个项目时，造成python环境混乱，建议不同的项目使用不同的虚拟环境 
	
	进入、离开虚拟环境：
	
		window: 
			运行虚拟环境目录下的scripts目录下的activate
			运行虚拟环境目录下的scripts目录下的deactivate.bat 
			
		Linux:
			进入虚拟环境：  source /opt/project02/p2_venv/bin/activate
			离开虚拟环境：  deactivate
			
	创建虚拟环境：
	
		1) 切换到虚拟环境所在的当前目录
		2) python -m venv 虚拟环境名称
			

==================================






























