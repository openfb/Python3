集合  set 

	作用：去重 
	
	类型：
		可变集合
			
			工厂函数  set()
			
		不可变集合
		
			工厂函数  fronzenset()


1、创建可变集合


	test_str = "hello python"
	set_A = set(test_str)
	print(type(set_A))
	print(set_A)


	test_data = (11, 22, 33, 44, 11, 22, 55)
	set_A = set(test_data)
	print(type(set_A))
	print(set_A)


2、创建不可变集合 

	test_data = (11, 22, 33, 44, 11, 22, 55)

	set_A = frozenset(test_data)

	print(type(set_A))

	print(set_A)


3、通过for循环遍历集合

	>>> set_A = set("hello")
	>>> set_A
	{'e', 'o', 'h', 'l'}
	>>> 
	>>> for i in set_A:
	...    print(i)
	... 
	e
	o
	h
	l

	
示例：统计字符个数

	data = "aaaabbbbbcccccccdddddddddddeffffff"

	for i in set(data):
		print("字符：%s, 次数：%s" % (i, data.count(i)))	
	
	
	
	
	
Bytes 

	python 3.X 
	
	特殊字符串 
	
	
1、定义bytes类型数据 


data = b"hello python"

print(data)
print(type(data))
	

2、字符串 ---> bytes 

方法1) encode()  编码

	data_01 = "hello python"
	print(type(data_01))
	
	data_02 = data_01.encode("utf8")
	print(type(data_02))
	print(data_02)
	
	
	
	data_01 = "我爱北京天安门，天安门上太阳升"
	print(type(data_01))

	data_02 = data_01.encode("utf8")
	print(type(data_02))
	print(data_02)


方法2) 工厂函数  bytes() 

	data_01 = "我爱北京天安门，天安门上太阳升"
	print(type(data_01))

	data_02 = bytes(data_01.encode("utf8"))
	print(type(data_02))

	print(data_02)


3、bytes ---- 字符串

方法1) 解码  decode() 

	data_01 = b"xjs handsome"

	print(type(data_01))
	print(data_01)

	data_02 = data_01.decode("utf8")
	print(type(data_02))
	print(data_02)


方法2) 工厂函数   str() 

	data_01 = b"xjs handsome"

	print(type(data_01))
	print(data_01)

	data_02 = str(data_01)
	print(type(data_02))
	print(data_02)




数据类型：

	数字、字符串、列表、元组、字典、集合、bytes 
	
	
		可变类型
			列表、字典
			
		不可变类型
			数字、字符串、元组


	
		可迭代
			字符串、列表、元组、字典、集合 
			
		不可迭代
			数字 

