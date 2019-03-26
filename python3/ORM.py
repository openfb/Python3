SQLAlchemy

	SQLAlchemy是python下的一个ORM框架，该框架建立在数据库API之上，使用关系对象映射进行数据库操作，简而言之，即将对象转换成SQL，然后使用数据库API执行SQL并获取执行结果 

	
ORM的优点：

	1) 隐藏与后台数据库交互的细节，由ORM提供的对象方法直接操作数据库
	2) 简化对后台数据库的操作
	
	
安装模块
	1) 切换到项目对应的虚拟环境 
	[root@localhost bin]# pip3 install sqlalchemy
	
	
示例：连接数据库创建用户表 


1) 创建表 
		import sqlalchemy
		from sqlalchemy import create_engine        # 创建与后台数据库的连接
		from sqlalchemy.ext.declarative import declarative_base     # 创建orm类
		from sqlalchemy import Column, Integer, String
		from sqlalchemy.orm import sessionmaker       # 导入类，游标


		'''
			创建与后台数据库的连接
			mysql+pymysql://用户名:密码@数据库服务器IP/数据库名?charset=utf8
			encoding='utf-8'   指定utf-8字符集
			echo=True   代码执行时会显示连接数据库的详细信息
		'''

		db_conn = create_engine("mysql+pymysql://admin:redhat@10.100.100.252/testdb?charset=utf8",encoding="utf-8",echo=True)

		'''
			创建orm基类， 方便后续管理操作
		'''

		Base = declarative_base()


		'''
			以类的方式创建用户表
		'''

		class User(Base):
			__tablename__ = "user"
			id = Column(Integer, primary_key=True)
			name = Column(String(32))
			password = Column(String(128))


		'''
			在db_conn数据库连接上，根据上述User类描述的表结构，创建表
		'''
		Base.metadata.create_all(db_conn)



2) 添加数据 

   核心思想：对类做实例化，生成数据对象
   

		'''
			创建一个生成会话的类，基于类创建一个会话实例对象(游标)
		'''

		sessio_class = sessionmaker(bind=db_conn)
		s1 = sessio_class()


		'''
			添加数据
		'''

		user_01 = User(name="Martin", password="redhat")
		user_02 = User(name="Jerry", password="123")
		user_03 = User(name="Mike", password="456")


		s1.add(user_01)
		s1.add(user_02)
		s1.add(user_03)

		s1.commit()



		
		
		
		
		

3) 数据查询 


方法1) 

		'''
			查询数据时，默认返回的一个包含多个数据对象的列表
			可以理解每个数据对象就是一条实体数据  User Object[id=1, name="martin", password="redhat"]
			通过"数据对象.字段名称"获取数据
		'''

				result_01 = s1.query(User).filter_by(name="Martin").all()

				result_02 = s1.query(User).filter(User.id>4).all()

				result_03 = s1.query(User).filter(User.id>2).all()

				print(result_01)
				print(result_01[0].id)
				print(result_01[0].name)
				print(result_01[0].password)

				print("---" * 10)

				print(result_02)
				print(result_02[1].password)
				print("---" * 10)

				print(result_03)
				for data_obj in result_03:
					print(data_obj.id)
					print(data_obj.name)
					print(data_obj.password)



方法2) 
	在数据表对应的类中定义__repr__(self)的方法，该方法的作用是用于定义返回数据的格式
	有此方法，默认查询返回的就不是数据对象，而是按照__repr__定义的方式返回数据 


			'''
			以类的方式创建用户表
			'''

		class User(Base):
			__tablename__ = "user"
			id = Column(Integer, primary_key=True)
			name = Column(String(32))
			password = Column(String(128))
			
			'''
				定义返回数据的格式；可自定义
			'''
			def __repr__(self):
				return "%s" % self.password

		
		result_01 = s1.query(User).filter_by(name="Martin").all()
		result_02 = s1.query(User).filter(User.id > 4).all()

		print(result_01)
		print(result_02)



****   数据查询时实现过滤的写法

	s1.query(User).filter_by(条件)
	
		等值条件
			filter_by(name="martin")
			filter_by(id=2)
		
		
	s1.query(User).filter(条件)
	
		非等值条件 
		
			filter(User.id > 3)
			filter(类名.属性名称 > 3)
	


查询其他写法：

	1) all() 返回所有数据

		result_01 = s1.query(User).filter(User.id > 3).all()
		print(result_01)
		print(result_01[2])


	2) first()

		result_02 = s1.query(User).filter(User.id > 3).first()
		print(result_02)


	3) 多条件查询 

		并且  and

			result_01 = s1.query(User).filter(User.id >= 2).filter(User.id <= 4).all()
			print(result_01)
		
		
		或者  or 

			result_01 = s1.query(User).filter(User.name.in_(["Martin", "Mike"])).all()
			print(result_01)


	4) 模糊查询 
	
		result_01 = s1.query(User).filter(User.name.like("%user%")).all()
		print(result_01)
	
	
	5) 查询所有数据
	
		result_01 = s1.query(User.id, User.name, User.password).all()
		print(result_01)
	
	
	6) 统计 
	
		result_01 = s1.query(User).filter(User.name.like("%user%")).count()
		print(result_01)
	
	
	
	
	

4) 更新数据

	result_01 = s1.query(User).filter_by(name="Martin").first()
	result_01.password = "abc123"
	s1.commit()


5) 删除数据 

	result_01 = s1.query(User).filter_by(name="Martin").first()

	s1.delete(result_01)

	s1.commit()



	
	
==================================================================
	
外键关系 

1、创建外键关系，添加数据 


		import sqlalchemy
		from sqlalchemy import create_engine        
		from sqlalchemy.ext.declarative import declarative_base   
		from sqlalchemy import Column, Integer, String, ForeignKey
		from sqlalchemy.orm import sessionmaker 


		db_conn = create_engine("mysql+pymysql://admin:redhat@10.100.100.252/testdb?charset=utf8",encoding="utf-8",echo=True)

		Base = declarative_base()


		class Worker(Base):
			__tablename__ = "worker"
			id = Column(Integer, primary_key=True)
			name = Column(String(20))
			age = Column(Integer)
			gender = Column(String(10))


		class Salary(Base):
			__tablename__ = "salary"
			id = Column(Integer, primary_key=True)
			level = Column(String(10))
			salary = Column(Integer)
			# 创建外键关联关系
			worker_id = Column(Integer, ForeignKey("worker.id"))

		Base.metadata.create_all(db_conn)


		sessio_class = sessionmaker(bind=db_conn)
		s1 = sessio_class()

		# 保存数据

		worker_01 = Worker(name="Martin", age=30, gender="F")
		worker_02 = Worker(name="Jerry", age=20, gender="F")
		worker_03 = Worker(name="Tome", age=40, gender="M")
		worker_04 = Worker(name="Mike", age=32, gender="M")


		salary_01 = Salary(level="T1", salary=10000, worker_id=1)
		salary_02 = Salary(level="T2", salary=20000, worker_id=2)
		salary_03 = Salary(level="T3", salary=30000, worker_id=4)
		salary_04 = Salary(level="T4", salary=40000, worker_id=3)


		s1.add_all([worker_01, worker_02, worker_03, worker_04])
		s1.add_all([salary_01, salary_02, salary_03, salary_04])

		s1.commit()



2、为方便数据管理，建立引用关系  

	class Salary(Base):
		__tablename__ = "salary"
		id = Column(Integer, primary_key=True)
		level = Column(String(10))
		salary = Column(Integer)
		# 创建外键关联关系
		worker_id = Column(Integer, ForeignKey("worker.id"))

		'''
			创建关系，方便数据管理 
			格式：relationship("类名", backref="自定义名称")
			"Worker"：表示与woker表建立关系，可以让工资对象通过关系r获取员工表中所有数据
			"worker_to_salary"： 可以让员工对象通过该名称获取所有的工资数据
		'''
		r = relationship("Worker", backref="woker_to_salary")



3、获取数据 

1) 通过工资对象获取员工表中数据


		salary_obj = s1.query(Salary).filter_by(level="T3").first()
		print(salary_obj)
		print(salary_obj.r)
		print(salary_obj.r.name)
		print(salary_obj.r.age)
		print(salary_obj.r.gender)


		print("姓名: %s, 级别：%s, 工资: %s" % (salary_obj.r.name, salary_obj.level, salary_obj.salary))

		# 显示所有员工的工资信息

		salary_all_obj = s1.query(Salary).all()

		for s_obj in salary_all_obj:
			print("姓名: %s, 级别: %s, 工资: %s" % (s_obj.r.name, s_obj.level, s_obj.salary))



2) 通过员工对象获取工资数据


		worker_obj = s1.query(Worker).filter_by(name="Martin").first()
		print(worker_obj.name)
		print(worker_obj.age)
		print(worker_obj.gender)
		print(worker_obj.woker_to_salary)
		print(worker_obj.woker_to_salary[0].level)
		print(worker_obj.woker_to_salary[0].salary)


		worker_all_obj = s1.query(Worker).all()

		for w_obj in worker_all_obj:
			print("姓名: %s, 级别： %s, 工资: %s" % (w_obj.name, w_obj.worker_to_salary[0].level,w_obj.worker_to_salary[0].salary))



====================================================

多对多关系 

	书籍、 作者
	
	服务器	应用
	
	通过建立第三张关系表，维护数据的多对多关系 
	
	



		import sqlalchemy
		from sqlalchemy import create_engine
		from sqlalchemy.ext.declarative import declarative_base
		from sqlalchemy import Column, Integer, String, ForeignKey, Table
		from sqlalchemy.orm import sessionmaker, relationship



		db_conn = create_engine("mysql+pymysql://admin:redhat@10.100.100.252/testdb?charset=utf8",encoding="utf-8",echo=False)

		Base = declarative_base()


		'''
			创建关系表，用于保存服务器到应用的多对多关系
			server_id字段为服务器表id的外键
			app_id字段为应用表id的外键
		'''
		server_m2m_app = Table("server_m2m_app", Base.metadata,
							   Column("server_id", Integer, ForeignKey("server.id")),
							   Column("app_id", Integer, ForeignKey("application.id")))


		class Server(Base):
			__tablename__ = "server"
			id = Column(Integer, primary_key=True)
			ip = Column(String(128))
			hostname = Column(String(128))

			'''
				secondary=server_m2m_app参数指定关系表的名称
			'''
			r = relationship("Application", secondary=server_m2m_app, backref="app_to_server")


		class Application(Base):
			__tablename__ = "application"
			id = Column(Integer, primary_key=True)
			app_name = Column(String(128))



		Base.metadata.create_all(db_conn)



		sessio_class = sessionmaker(bind=db_conn)
		s1 = sessio_class()

		# server_01 = Server(ip="1.1.1.1", hostname="node01.linux.com")
		# server_02 = Server(ip="1.1.1.2", hostname="node02.linux.com")
		# server_03 = Server(ip="1.1.1.3", hostname="node03.linux.com")
		#
		#
		# app_01 = Application(app_name="Tomcat")
		# app_02 = Application(app_name="Nginx")
		# app_03 = Application(app_name="Zabbix")
		# app_04 = Application(app_name="Ansible")
		#
		#
		# '''
		#     说明服务器与应用的对应关系
		# '''
		#
		# server_01.r = [app_01, app_03]
		# server_02.r = [app_04]
		# server_03.r = [app_01, app_02,app_03]
		#
		#
		# s1.add_all([server_01, server_02, server_03, app_01, app_02, app_03, app_04])
		#
		# s1.commit()



		# 查询服务器1.1.1.3运行的业务


		# server_01 = s1.query(Server).filter_by(ip="1.1.1.3").first()
		# print(server_01)
		# print(server_01.r)
		#
		# print("服务器%s业务列表：" % server_01.ip)
		#
		# for app_obj in server_01.r:
		#     print(app_obj.app_name)



		# 查询所有服务器应用列表

		server_all_obj = s1.query(Server).all()

		for server_obj  in server_all_obj:
			print("服务器%s的业务列表：" % server_obj.ip)
			for app_obj in server_obj.r:
				print(app_obj.app_name)








	
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			

