列表  ---- 可变类型 list 

1) 定义 

	被定义在[ ]的数据，每个数据称为元素，不同元素要使用逗号","隔开 
	
	无数据类型之分 
	
	list_01 = [ 10, 20, 30 ]
	print(type(list_01))


	list_02 = [ 10, "Martin", 3.14, 10+20j, ["user01", "user02"] ]
	print(type(list_02))
	print(len(list_02))

	list_03 = []
	print(type(list_03))

		
	list_04 = [
		10,
		20,
		30
	]
	
	# 列表解析

	list_D = [ x for x in range(0,101) ]
	print(list_D)
	print(type(list_D))

	list_E = [ x ** 2 for x in range(1,11) ]
	print(list_E)

	list_F = [ x for x in range(1,11) if not x % 2 ]
	print(list_F)


2) 列表操作符 

	+, ==, !=
	
	in, not in 
	
		list_02 = [ 10, "Martin", 3.14, 10+20j, ["user01", "user02"] ]

		print("Martin" in list_02)
		print("user02" in list_02)
		print(["user01", "user02"] in list_02)

	len( )
	
	索引
	
		list_02 = [ 10, "Martin", 3.14, 10+20j, ["user01", "user02"] ]

		print(list_02[3])
		print(list_02[-2])
		print(list_02[2])
		print(list_02[-1][0])
			
			
	修改列表中的某个元素 
	
		list_02 = [ 10, "Martin", 3.14, 10+20j, ["user01", "user02"] ]

		list_02[2] = "Jerry"
		list_02[-1][-1] = "Tome"

		print(list_02)


	切片
	
		list_02 = [ 10, "Martin", 3.14, 10+20j, ["user01", "user02"] ]

		print(list_02[0:2])



		
		
列表操作方法 

1) append( )	追加元素


	list_03 = [ 10, 20, 30 ]
	list_03.append("192.168.1.1")
	print(list_03)


2) insert( )		插入元素

	list_03 = [ 10, 20, 30 ]

	list_03.insert(1, "jerry")
	list_03.insert(-1, ["king", "192.168.1.1"])

	print(list_03)


3) clear( )		删除列表所有元素 

	list_03 = [ 10, 20, 30 ]

	list_03.clear()

	print(list_03)


4) remove( )		删除单个元素


	list_03 = [ 10, 20, 30 ]

	list_03.remove(30)

	print(list_03)


5) pop( )		默认删除最后的元素并返回 

 
	list_03 = [ 10, 20, 30, 40 ]

	list_03.pop()

	print(list_03)


6) index()		返回元素所在的下标

	list_03 = [ 10, 20, 30, 40 ]

	print(list_03.index(30))




通过for循环列表 

	list_01 = [ 10, "Martin", "Jerry", "root", ["admin", "redhat"] ]

	for element in list_01:
		print("元素：%s ------- 数据类型： %s" % (element, type(element)))




示例：生成10位数的裴波那契数列

	fiber = [ 0, 1 ]

	for i in range(8):
		fiber.append(fiber[-1] + fiber[-2])

	for j in fiber:
		'''
			end=""	取消print默认的换行 
		'''
		print("%s " % j, end="")


示例：模拟C语言的栈 

	import sys

	stack = []

	menu = """
	a.查看所有值
	b.存储数据
	c.获取数据
	d.退出

	选择：   
	"""

	while True:
		choice = input(menu).strip().lower()

		if choice == "a":
			print(stack)
		elif choice == "b":
			data = input("数据： ")
			stack.append(data)
		elif choice == "c":
			print("获取的数据：%s" % stack.pop())
		elif choice == "d":
			sys.exit()
		else:
			print("输入错误")


示例：人机猜拳

	菜单：

	0.石头
	1.剪刀
	2.布
	3.退出

	机器：随机 
	人：0， 1， 2， 


	[  [石头， 剪刀]， [剪刀， 布]， [布， 石头] ]

	机器随机 ：  石头
	人：石头

	[机器， 人]




==========================================================================================================================

元组   tuple 	-----   不可变类型 

1) 定义 

	使用( )定义的数据，元素， 不同元素要使用逗号

	tuple_01 = ( 10, 20, 30 )
	print(type(tuple_01))

	tuple_02 = ( 10, "Martin", [30, 40], (50, 60) )
	print(type(tuple_02))


	tuple_03 = ( "Martin", )			//定义单个元素的元组 
	print(type(tuple_03))

	
2) 元组操作符 

	+, *, ==, !=
	in, not in  
	索引 
	切片
	
	
>>> tuple_B = (("nginx", "1.11"),("httpd", "2.4"),("zabbix","3.4"))

>>> for i, j in tuple_B:
...     print(i)
... 
nginx
httpd
zabbix
>>> for i, j in tuple_B:
...     print(j)
... 
1.11
2.4
3.4
>>> 
>>> tuple_B = (("nginx", "1.11"),("httpd", "2.4"),("zabbix","3.4"))
>>> 
>>> for i, j in tuple_B:
...    print("软件名称: %s, 版本：%s" %(i, j))
... 
软件名称: nginx, 版本：1.11
软件名称: httpd, 版本：2.4
软件名称: zabbix, 版本：3.4
