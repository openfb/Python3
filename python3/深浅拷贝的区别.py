浅拷贝、深拷贝的区别 

	可变数据类型

1、浅拷贝 

	通过对象自身的copy()方法实现 
	
	浅拷贝只会拷贝对象的首层内存空间
	
	浅拷贝，如果直接修改对象内部的值，原对象会改变，拷贝对象不会随之修改
	浅拷贝，对象中包括其他的子对象, 如果修改子对象内部的值，原对象会改变，拷贝对象也会随之修改
	

	示例01)
		
		list_01 = [ "user01", "user02" ]
		list_02 = list_01.copy()

		print(list_01)
		print(list_02)

		print("----" * 10)

		# 修改list_01的数据
		list_01[-1] = "Martin"
		print(list_01)
		print(list_02)


	示例02)
	
		list_01 = [ "user01", "user02", ["user03", "user04"] ]

		list_02 = list_01.copy()

		print(list_01)
		print(list_02)

		print("----" * 10)

		# 修改list_01的值

		list_01[0] = "Martin"
		print(list_01)
		print(list_02)

		print("----" * 10)

		# 修改list_01内部列表的值

		list_01[-1][0] = "Tome"
		print(list_01)
		print(list_02)




2、深拷贝 	copy.deepcopy( )

	深拷贝会拷贝所有数据， 原数据做任何修改，拷贝的数据也不会随之修改 
	
		import copy

		list_01 = [ "user01", "user02", ["user03", "user04"] ]

		list_02 = copy.deepcopy(list_01)

		print(list_01)
		print(list_02)

		print("----" * 10)

		# 对list_01做修改

		list_01[0] = "Martin"
		list_01[-1][-1] = "King"

		print(list_01)
		print(list_02)


		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		







