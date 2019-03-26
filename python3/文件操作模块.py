文件操作模块

1、os模块  

1) listdir()

	显示目录下的文件 

示例：统计系统的进程数 

	import os

	process_number = 0

	for file_name in os.listdir("/proc"):
		if file_name.isdigit():
			process_number += 1

	print(process_number)


2) getcwd()
	
	获取当前目录 
	
3) chdir()

	切换目录 
	
	In [6]: os.chdir("/etc")

	In [7]: os.getcwd()
	Out[7]: '/etc'

4) chmod(), chown()


	In [16]: os.chown("/tmp/1.txt", 1000, 1000)

	
5) os.mkdir(), os.makedirs()

	In [18]: os.mkdir("/tmp/bj")

	In [19]: os.makedirs("/tmp/sh/python")


6) os.remove(), os.removedirs() 

	删除文件、删除空目录 
	
	In [20]: os.remove("/tmp/1.txt")

	In [21]: os.removedirs("/tmp/bj")

 
7) os.rename()

	重命名
	
	In [24]: os.rename("/tmp/1.txt", "/tmp/new.txt")

 
8) os.walk()

	默认返回一个生成器，通过for循环遍历 
	
	递归显示目录下所有的文件，目录 
	
递归显示目录名称：

	In [45]: for i in os.walk("/data"):
		...:     print(i[0])

	for i, j, k in os.walk("/data"):
		print(i)
		

显示所有文件名称

In [55]: for dir_name, sub_dir_name, file_list in os.walk("/data"):
    ...:     if len(file_list) > 0:
    ...:         for file_name in file_list:
    ...:             full_file_name = os.path.join(dir_name, file_name)
    ...:             print(full_file_name)
  

		
 
9) os.popen()方法

	用于执行shell命令
	
	In [10]: result = os.popen("ls -l /etc/fstab")

	In [11]: for i in result:
		...:     print(i)

 
 
 
 
 
 
 os.path的方法 
 
1) os.path.exists()

	In [26]: os.path.exists("/etc/fstab")
	Out[26]: True

	In [27]: os.path.exists("/etc/kkk")
	Out[27]: False

 
 
2)

os.path.basename()		获取文件名称
os.path.dirname()		获取文件所在路径 
		
	In [28]: os.path.basename("/etc/sysconfig/network")
	Out[28]: 'network'

	In [29]: os.path.dirname("/etc/sysconfig/network")
	Out[29]: '/etc/sysconfig'

	
3) 
	getsize()
	getmtime()	获取文件的修改时间
	getatime()	获取文件的访问时间
	getctime()	获取文件的创建时间
	
	In [30]: os.path.getsize("/etc/fstab")
	Out[30]: 465

	In [31]: os.path.getmtime("/etc/fstab")
	Out[31]: 1532487820.3579905

	In [32]: os.path.getatime("/etc/fstab")
	Out[32]: 1541584144.378478

	In [33]: os.path.getctime("/etc/fstab")
	Out[33]: 1532487820.38299

 
4)

	In [34]: os.path.isdir("/etc/")
	Out[34]: True

	In [35]: os.path.isfile("/etc/fstab")
	Out[35]: True

	In [36]: os.path.islink("/etc/sysconfig/selinux")
	Out[36]: True

	In [37]: os.path.ismount("/")
	Out[37]: True

	
5) 拼接文件路径 

	In [38]: os.path.join("/etc", "fstab") 
	Out[38]: '/etc/fstab'

 
 
示例： 批量重命名 


	# Author: Martin

	# show all file

	import os

	all_file = []

	for dir_name, sub_dir_name, file_list in os.walk("/data"):
		if len(file_list) > 0:
			for file_name in file_list:
				full_file_name = os.path.join(dir_name, file_name)
				all_file.append(full_file_name)

	# file rename

	for name in all_file:
		if name.endswith("yml"):
			old_file_name = name.split(".")[0]
			new_file_name = old_file_name + ".jpg"
			os.rename(name, new_file_name)




2、shutil模块 

1) copy()   

	拷贝文件 
	
	In [2]: shutil.copy("/etc/fstab", "/tmp")



2) rmtree()

	删除目录 
	
	In [3]: shutil.rmtree("/data")



3、tarfile

1) 创建归档文件

	模式：
		w 	.tar 
		w:gz 	.tar.gz 
		w:bz2	.tar.bz2
		w:xz	.tar.xz 

	In [6]: import tarfile

	In [7]: tar_file = tarfile.open("/data/tmp_01.tar.gz", "w:gz")

	In [8]: tar_file.add("/tmp/1.txt")

	In [9]: tar_file.add("/tmp/2.txt")

	In [10]: tar_file.add("/tmp/3.txt")

	In [11]: tar_file.close()


2) 读取文件 

	In [17]: tar_file = tarfile.open("/data/tmp_01.tar.gz", "r")

	In [18]: tar_file.list()
	?rw-r--r-- root/root          0 2018-11-08 15:40:33 tmp/1.txt 
	?rw-r--r-- root/root          0 2018-11-08 15:40:33 tmp/2.txt 
	?rw-r--r-- root/root          0 2018-11-08 15:40:33 tmp/3.txt 




4、hashlib 

	In [1]: import hashlib
	
	# 创建一个用计算md5校验码的对象
	In [2]: md5_obj = hashlib.md5()

	In [4]: md5_obj.update("ab".encode("utf-8"))

	In [5]: md5_obj.hexdigest()
	Out[5]: '187ef4436122d1cc2f40dc2b92f0eba0'



对文件内容做md5校验(小文件)

	import hashlib

	file_name = "/etc/fstab"

	# 获取文件内容
	f = open(file_name, "rb")
	data = f.read()
	f.close()

	# 对内容做md5校验
	md5_obj = hashlib.md5()
	md5_obj.update(data)

	print(md5_obj.hexdigest())



对文件内容做md5校验(大文件)

	import hashlib

	md5_obj = hashlib.md5()

	file_name = "/etc/fstab"
	f_obj = open(file_name, "rb")

	while True:
		data = f_obj.read(8192)
		if not data:
			break
		md5_obj.update(data)

	f_obj.close()

	print(md5_obj.hexdigest())




5、pickle模块 

	实现数据持久性保存
	
1) dump()

	存储pickle格式的数据
	
	import pickle

	list_01 = [ "11", "22", "33" ]
	
	f_obj = open("/tmp/test.txt", "wb")
	
	pickle.dump(list_01, f_obj)
	
	f_obj.close()


2) load() 

	读取数据 
	
	f2 = open("/tmp/test.txt", 'rb')
	data = pickle.load(f2)
	f2.close()

	print(data)
 
 
 
 
 
 

 
 
 
 
 
 
 


	

