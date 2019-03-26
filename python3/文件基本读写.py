文件I/O操作 


1、创建文件对象

	处理文件内容时，将文件内容作为bytes的方式的处理 

	f_obj = open(文件名称, 模式, encoding="utf-8")
	
		模式：
			r 	默认    读取内容 
			
				rb   
					读取的数据类型为bytes 
					非文本文件
				
			
			w   写入 
				如果文件中有数据，数据会被清空
				新建文件 
				
				wb 
				
			r+  读写操作
			a   追加
		
	
	
读取文件内容 

1) read() 

	默认读取所有文件内容，返回字符串
	
	read(4096)
	
		f = open("E:/testdir/test.txt", mode="rb")

		data = f.read()

		print(type(data))
		print(data)
		
		f.close()
	
	
	
2) seek(offset, whence)

		whence：
			0	文件开头位置 
			1	文件当前位置 
			2	文件末尾 
			
		offset：
			正数：向后移动
			负数：向前移动
		
		f.seek(-2, 2)
		f.seek(3, 0)
		f.seek(-3, 1)
	
	tell( )方法
		返回光标当前的位置 
	
	
3) readline()

	返回bytes类型，一次读取一行 
	
4) readlines()

	返回列表，列表中每个元素是文件的一行



写入文件内容 

	写入文件内容，默认不带换行，需要手工加换行符\n 

1) write( )

			In [4]: f = open("/tmp/new.txt", "w")

			In [5]: f.write("python\n")
			Out[5]: 7

			In [6]: f.write("Java\n")
			Out[6]: 5

			In [7]: f.close()


		flush( )	刷新buffer中的数据到硬盘 
		
		写入bytes格式的数据
		
			In [1]: f = open("/tmp/test.txt", "wb")

			In [2]: test_str = "python"

			In [4]: f.write(test_str.encode("utf-8"))
			Out[4]: 6

			In [5]: f.flush()

		
2) writelines( )


示例：接收用户的输入数据，保存到文件 

	# Author: Martin


	content = []

	# 提示用户输入数据，quit表示结束

	while True:
		data = input("数据： ")
		if data == "quit":
			break
		content.append(data)


	# 打开文件，保存数据

	f_obj = open("e:/project01/new.txt", "wb")

	for line in content:
		f_obj.write((line + "\n").encode("utf-8"))

	f_obj.close()



示例：文件内容替换 

	# Author: Martin


	old_file = open("e:/project01/test.txt", "rb")

	new_file = open("e:/project01/test_new.txt", "w")

	for line in old_file:
		# 判断行内有python，执行替换，写入新文件
		if "python" in line.decode():
			new_line = str(line).replace("python", "Java")
			new_file.write(new_line + "\n")
		else:
			new_file.write(str(line) + "\n")

	old_file.close()
	new_file.close()



示例：监控文件输出，将带有error的数据保存到新文件 

import time

filename = "/tmp/1.txt"

fobj = open("/tmp/1.txt")
fobj.seek(0,2)

old_position = fobj.tell()

while True:
    fobj.seek(0,2)
    new_position = fobj.tell()

    if new_position > old_position:
        offset = old_position - new_position
        fobj.seek(offset,2)
        old_position = new_position
        print fobj.read()

    time.sleep(3)



打开文件另外的方式：

	文件内容处理完毕后，会自动关闭文件

	with open("e:/project01/test.txt") as f:
		for line in f:
			print(line.upper())

	print(f.closed)

















