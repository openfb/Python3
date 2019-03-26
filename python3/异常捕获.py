异常捕获 

	NameError, IndexError, TypeError, IOError, OSError

语法：

try:
	关键性代码
except 异常名称 as 变量：
	操作语句 
except 异常名称 as 变量:
	操作语句
....

变量： 用于保存抛出异常的原因


示例：捕获单个异常

	import sys

	file_name = input("文件名： ")

	try:
		f_obj = open(file_name)
	except FileNotFoundError:
		print("文件不存在！！！！")
		sys.exit()


	data = f_obj.read()

	print(data)

	f_obj.close()
	
	
示例：捕获多个异常


	# Author: Martin

	import sys
	#
	file_name = input("文件名： ")
	file_mode = input("文件打开模式： ")

	try:
		f_obj = open(file_name, file_mode)
	except FileNotFoundError:
		print("文件不存在！！！！  " + str(e))
		sys.exit()
	data = f_obj.read()

	print(data)

	f_obj.close()


示例：保存异常信息 

	# Author: Martin

	import sys
	#
	file_name = input("文件名： ")
	file_mode = input("文件打开模式： ")

	try:
		f_obj = open(file_name, file_mode)
	except FileNotFoundError as e:
		print("文件不存在！！！！  " + str(e))
		sys.exit()
	data = f_obj.read()

	print(data)

	f_obj.close()



注意两点:

	1、try....except捕获异常
	
		KeyboardInterrupt
			ctrl + c强制中断  无法捕获 
			
	2、
	
	  Exception 	产生所有其他具体的异常
		NameError
		ValueError
		TypeError
		KeyError
	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	


