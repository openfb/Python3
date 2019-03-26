函数、模块、包

函数 --- function 

	作用：
		1、实现代码的重用 
		2、方便修改代码 
		

函数类型： 

	自定义函数 
	内置函数 --- id(), type(), int() 
		

自定义函数 

定义函数的语法 

	def func_name():
		代码
		代码
		
	函数名称命名规范：

		1、字母、数字、下划线
		2、从第二个单词首字母大写    copyFile()
		3、不要与内置函数名称冲突    
		

调用函数 

	func_name() 
	
		示例：语法示例 
		
		def func01():
			print("实现文件查找功能")


		print(func01)

		func01()


函数定义的本质，就是在内存中开辟一段空间，保存函数内部的代码，此时所有代码是作为普通字符串存入内存的，代码不会执行；
只有当通过"函数名称()"的方式调用函数时，代码才会运行 

	def fun01():
		print("fun01函数开始")
		fun02()
		print("fun01函数结束")


	def fun02():
		print("这是函数func02")


	fun01()




模块 

	本质就是一个py文件 
	
	*.py 
	
	sys.path    查看模块路径

	方便导入自定义模式, 定义环境变量保存模块路径   PYTHONPATH 
	
		Linux:  /etc/profile
		
		window:  计算机 --- 属性 --- 高级设置 --- 环境变量   
		
		
	通过判断__name__变量的值
		如果值为__main__， 表示文件独立运行 
		如果文件是被作为模块导入，该变量的值为模块名称 
		
		# Author: Martin

		def fun01():
			print("m3文件中的fun01函数")


		if __name__ == '__main__':

			fun01()	

	了解：
	
		.pyc   字节码编译文件 
	
		

包  package 

	本质就是存入py文件的目录
	
	包需要有__init__.py文件 
	
	PYTHONPATH   保存项目目录名称 
	
	

导入模块的方法：

1、import 模块名称 


2、import 模块名称 as 别名 

   import pickle as p

   
3、from 包名 import 模块名称 

	from user_manager import user_login


4、from 包名.模块名称 import 方法名称 

	from user_manager.user_login import fun03, fun01




变量类型：

	全局变量
	
		在函数外部定义的变量 
		在函数内部对全局变量作修改的时候，需要使用global关键字声明全局变量 
		
			number = 10

			def fun01():
				print("数字：%s" % number)

			def fun02():
				print("数字：%s" % number)

			def fun03():
				# 声明全局变量 
				global number
				number += 20
				print(number)


			if __name__ == '__main__':
				fun03()
	
	局部变量 
	
		在函数内部定义的变量，只能在本函数内部调用  
		
		
			def fun01():
				name = "Martin"
				print(name.upper())

			def fun02():
				name = "Jerry"
				print(name[1])

			if __name__ == '__main__':
				fun01()
				print("---" * 10)
				fun02()




		











