迭代器  Iterator

	特殊对象, 节省内存
 
	迭代器：通过__next__()方法可获取下一个值的的对象称为迭代器，数据取完后，返回StopIteration异常 
	
	可迭代对象：
		能够作用于循环的取值的对象
		字符串、列表、元组、字典、文件对象
	
判断一个对象是否为可迭代对象 

In [1]: from collections import Iterable

In [2]: isinstance([], Iterable)
Out[2]: True

In [3]: isinstance((), Iterable)
Out[3]: True

In [4]: isinstance(123, Iterable)
Out[4]: False



判断一个对象是否为迭代器

In [6]: from collections import Iterator

In [7]: isinstance([], Iterator)
Out[7]: False

In [9]: isinstance((x for x in range(10)), Iterator)
Out[9]: True




将一个可迭代对象转换为迭代器

In [12]: alist = [ "martin", "jerry", "mike" ]

In [13]: a = iter(alist)

In [14]: print(a)
<list_iterator object at 0x7f5eea3ccc88>

In [15]: a.__next__()
Out[15]: 'martin'

In [16]: a.__next__()
Out[16]: 'jerry'

In [17]: a.__next__()
Out[17]: 'mike'

In [18]: a.__next__()
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-18-d34d2a8c0899> in <module>()
----> 1 a.__next__()

StopIteration: 




python2、python3 range()区别：

	python2:
		range()	返回列表，数据量大时，占用内存
		xrange()	返回迭代器，通过for循环遍历取值
		
	python3：
		range()		返回迭代器，通过for循环遍历取值
		
		
