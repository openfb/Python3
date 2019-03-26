正则表达式 

	作用：
		1) 过滤符合条件的数据 
		2) 匹配数据是否符合规范   

	re模块实现正则表达式的使用  


正则表达式的元字符：

1、匹配单个字符

	. 
	
	[abt]	[0-9]	[a-z]	[A-Z]	[a-zA-Z0-9]		[^a-z]
	
	\d	单个数字
		\D 

	\w 	单个字符或者数字 
		\W 
		
	\s 	单个空白字符 
		\S 	
		
		
2、匹配字符出现的次数		

	*	任意次 
	+	至少一次
	?	0次或者1次  可有可无 
	{3}	精确3次
		{3,}	{3,7}
		


	?：
		1) 前一个字符出现0次或者1次     ab? 
		2) ?如果跟在一个表示次数的字符后面时，表示的意思非贪婪模式匹配  
		
			匹配模式：
				贪婪模式，默认，按最长匹配
				非贪婪模式，按最短匹配


				
	分组    ( )	

		(ab){2}
				

3、匹配字符出现的位置 

	^string 
	string$
	^$
	
	\bXXXX\b 		匹配XXXX是否为一个单词 
	

			
			
re模块的方法 


1、match(pattern, string, flags=0)
	
	按照正则表达式从字符串的第一个字符开始匹配，如果匹配不成功，返回None, 否则返回一个Match Object；
	通过调用Match Object的group()可以显示正则表达式匹配的字符 

			>>> test_str = "This is regex demo"
			>>> regex_01 = r"d..o"
			>>> 
			>>> result = re.match(regex_01, test_str)
			>>> 
			>>> print(result)
			None



			>>> test_str = "demo regex python"
			>>> result = re.match(regex_01, test_str)
			>>> 
			>>> print(result)
			<_sre.SRE_Match object; span=(0, 4), match='demo'>

			>>> print(result.group())
			demo

	
	
2、search(pattern, string, flags=0)

	扫描整个字符串，查找被正则表达式匹配的数据 
	
			>>> test_str_01 = "This is python regex demo"
			>>> test_str_02 = "This is python demo regex"
			>>> test_str_03 = "demo python regex"
			>>> 
			>>> regex_01 = r"d..o"
			>>> 
			>>> result_01 = re.search(regex_01, test_str_01)
			>>> print(result_01)
			<_sre.SRE_Match object; span=(21, 25), match='demo'>
			>>> 
			>>> print(result_01.group())
			demo
		
			>>> result_02 = re.search(regex_01, test_str_03)
			>>> print(result_02)
			<_sre.SRE_Match object; span=(0, 4), match='demo'>
			>>> 
			>>> print(result_02.group())
			demo



3、显示被正则表达式的数据 

	Match Object对象 
	
		group()
		groups()		
		groupdict()

1) group()	返回字符串 


2) groups()	返回元组 

	把正则表达式分组中的数据放入元组，通过groups()方法返回 
	
	>>> test_str = '172.25.4.67 - - [17/Sep/2018:20:41:39 +0800]'

	>>> regex_01 = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s-\s\[(.*)\]"     

	>>> print(result.group())
	172.25.4.67 - - [17/Sep/2018:20:41:39 +0800]
	>>> 
	>>> print(result.groups())
	('172.25.4.67', '17/Sep/2018:20:41:39 +0800')
	>>> 
	>>> print(result.groups()[0])
	172.25.4.67
	>>> print(result.groups()[1])
	17/Sep/2018:20:41:39 +0800
	>>> 


3) groupdict()  返回字典 

	正则表达式中有自定义分组时， 以自定义组名为键，以对应的组匹配到的数据为值 
	
	
	>>> test_str = '172.25.4.67 - - [17/Sep/2018:20:41:39 +0800]'
	
	'''
		(?P<自定义组名>)	---->   groupdict() 
	'''
	>>> regex_01 = r"(?P<client_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s-\s\[(?P<access_time>.*)\]"     
	>>> 
	>>> result = re.search(regex_01, test_str)
	>>> print(result)
	<_sre.SRE_Match object; span=(0, 44), match='172.25.4.67 - - [17/Sep/2018:20:41:39 +0800]'>
	>>> 


	>>> print(result.groupdict())
	{'client_ip': '172.25.4.67', 'access_time': '17/Sep/2018:20:41:39 +0800'}
	>>> 




4、findall(pattern, string, flags=0)

	在字符串查找被匹配的到的所有的数据，返回一个列表 
	
		>>> str_01 = "like python regex demo love"
		>>> test_regex = r"l..e"
		>>> 
		>>> result = re.findall(test_regex, str_01)
		>>> 
		>>> print(type(result))
		<class 'list'>
		>>> 
		>>> print(result)
		['like', 'love']



5、finditer(pattern, string, flags=0)

	扫描整个字符串，返回多个匹配对象，通过调用匹配对象的group()方法显示匹配数据 

		>>> str_01 = "like python regex demo love"
		>>> 
		>>> test_regex = r"l..e"
		>>> 
		>>> result = re.finditer(test_regex, str_01)
		>>> 
		>>> for i in result:
		...     print(i.group())
		... 
		like
		love



6、split(pattern, string, maxsplit=0, flags=0)

	使用正则表达式匹配字符，使用匹配到的字符作为分隔符分割字符串 
	
		>>> str_01 = "root     pts/0        2018-11-14 09:51 (10.0.224.251)"

		>>> re.split(r"\s{2,}", str_01)
		['root', 'pts/0', '2018-11-14 09:51 (10.0.224.251)']
		>>> 

	示例：
		import os, re

		cmd_result = os.popen("who")

		for line in cmd_result:
			result = re.split(r"\s{2,}", line)
			print("用户名：%s, 终端名称: %s, 登录时间及IP：%s" % (result[0], result[1], result[2]))



7、sub(pattern, repl, string, count=0, flags=0)

	根据正则表达式替换字符 
	
		>>> str_01 = "demo demo demo"
		>>> 
		>>> re.sub(r"d..o", "Example", str_01)
		'Example Example Example'
		>>> 
		>>> 
		>>> re.sub(r"d..o", "Example", str_01, count=2)
		'Example Example demo'

	
	
		>>> url01 = "http://192.168.1.1/vedio/test.mp3"
		>>> 
		>>> url02 = "http://192.168.1.2/audio/test01.mp3"
		>>> 
		>>> test_regex = r"(http://)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(/.*)"

		>>> re.sub(test_regex, r"\1media.linux.com\2", url01)
		'http://media.linux.com/vedio/test.mp3'
		>>> 
		>>> re.sub(test_regex, r"\1media.linux.com\2", url02)
		'http://media.linux.com/audio/test01.mp3'
		>>> 

	
	
8、compile( )

	编译正则表达式，使用正则表达式另外一种写法
	
	适用于处理大文件 
	
		>>> str_01 = "python regex demo"
		>>> 
		>>> regex_01 = r"d..o"
		>>> 
		>>> re_obj = re.compile(regex_01)
		>>> 
		>>> print(re_obj)
		re.compile('d..o')
		>>> 
		>>> re_obj.search(str_01)
		<_sre.SRE_Match object; span=(13, 17), match='demo'>
		>>> 
		>>> re_obj.search(str_01).group()
		'demo'

	
	示例：
		
		# Author: Martin

		import re

		file_name = "/tmp/access_log"
		ip_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
		re_obj = re.compile(ip_regex)

		ipv4_count = 0

		with open(file_name) as f_obj:
			for line in f_obj:
				if re_obj.search(line):
					ipv4_count += 1

			print(ipv4_count)

		[root@localhost re_demo]# time python3 ipv4_count_01.py 

	
	
	
	
	
	
	
	
	
	
	
	
	





