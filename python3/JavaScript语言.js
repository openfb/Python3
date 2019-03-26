JavaScript

	独立的语言，浏览器具有JavaSript解释器，可以执行该代码。实现页面的前端动态效果
	
JavaScript代码存放位置：

1、html文件中的<body>标签的最下面


    <script type="text/javascript">
        alert(123)
    </script>



2、保存在独立的文件中，在html中导入 

    <script src="commons.js">

    </script>
	

	
注释：

	单行注释		//
	多行注释 		/* .... */
	

	
	
JavaScript代码写的位置：
	1) html文件 
	2) 浏览器 --- 右键 ---- 检查  ---- console 
	
	
	
变量 

	全局变量定义 
	
		name = "martin"
		
	局部变量定义 
	
		var name = "martin"		// var关键字 
		
		
	
	
	
基本数据类型

1、数字 

	parseInt()		将字符串转换为数字
	parseFloat()	转换为浮点数 


2、字符串 


操作方法：


1) charAt		索引操作 

name = "martin"
"martin"
name.charAt(0)
"m"
name.charAt(1)
"a"
name.charAt(2)
"r"
name.charAt(3)
"t"
name.charAt(4)
"i"



2) substring		切片 

name.substring(1,3)
"ar"
name.substring(1,)
"artin"



3) length 	获取字符串长度  

name.length
6



4) trim(), trimLeft(), trimRight()  去除空白 

5) concat()   字符串拼接

6) indexOf()   获取子串在原始字符串的位置 

7) lastIndexOf

8) substring()  获取子串 

9) slice( )   切片 

10) toLowerCase(), toUpperCase()   

11) split()

12) search()

13) match()

14) replace()





创建定时器 

    <script>
	
        function f1() {
			//在浏览器的console控制台输出信息
            console.log("hello log")
        }
		
		//创建定时器 
        setInterval("f1()", 2000);
    </script>




滚动文字效果 


    <div id="d_01">滚动文字效果</div>

    <script type="text/javascript">
        function f1() {
			
			//根据ID获取指定的标签
            var tag = document.getElementById("d_01");
			//获取标签中的内容，字符串
            var content = tag.innerText;

            var first_char = content.charAt(0);
            var last_char = content.substr(1, content.length);

            var new_content = last_char + first_char;

            tag.innerText = new_content;

        }

        setInterval("f1()", 500);

    </script>




数组

	类似python中的列表 
	
	数组名称 = [ 值1, 值2 ]
	
a = [ "martin", "tome", "jerry" ]

a[1]
"tome"




	
Dom操作 

1、获取标签 

直接查找


	document.getElementById(标签ID)

	document.getElementsByTagName(标签名称)

	document.getElementsByClassName()
	
	document.getElementsByName()




间接查找 

	tag = document.getElementById("c3")
	tag.parentElement
	tag.parentElement.previousElementSibling
	tag.parentElement.nextElementSibling
	tag.parentElement.lastElementChild
	tag.parentElement.previousElementSibling.lastElementChild




2、获取标签中的内容 

1) 获取标签内的字符

	标签.innerText

2) 管理样式

	tag.className = ""
	tag.classList
	tag.classList.add()
	tag.classList.remove()



示例01：弹出框

<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>

        .hide {
            display: none;
        }

        .c1 {
            position: fixed;
            left: 0;
            top: 0;
            right: 0;
            bottom: 0;
            background-color: black;
            opacity: 0.5;
            z-index: 9;
        }

        .c2 {
            width: 500px;
            height: 400px;
            background-color: white;
            position: fixed;
            left: 50%;
            top: 50%;
            margin-left: -250px;
            margin-top: -200px;
            z-index: 10;
        }
    </style>
</head>
<body style="margin: 0">

    <div>
        <input type="button" value="添加" onclick="showMenu()"/>
        <table>
            <thead>
                <tr>
                    <th>主机名</th>
                    <th>端口</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1.1.1.1</td>
                    <td>90</td>
                    <td>1.1.1.2</td>
                    <td>90</td>
                    <td>1.1.1.3</td>
                    <td>90</td>
                </tr>
            </tbody>
        </table>
    </div>

    <!-- 遮罩层 -->
    <div id="i1" class="c1 hide"></div>

    <!-- 弹出框 -->
    <div id="i2" class="c2 hide">
        <p> <input type="text" /> </p>
        <p> <input type="text" /> </p>
        <p>
            <input type="button" value="确定"/>
            <input type="button" value="取消" onclick="hideMenu()"/>
        </p>

    </div>

    <script>
        function showMenu() {
            document.getElementById("i1").classList.remove("hide");
            document.getElementById("i2").classList.remove("hide");
        }

        function hideMenu() {
            document.getElementById("i1").classList.add("hide");
            document.getElementById("i2").classList.add("hide");
        }
        
    </script>
</body>





示例02：全选、取消、反选

        <input type="button" value="全选" onclick="selectAll()"/>
        <input type="button" value="取消" onclick="cancleAll()"/>
        <input type="button" value="反选" onclick="reverseAll()"/>
		
		<table>
            <thead>
                <tr>
                    <th>选择</th>
                    <th>主机名</th>
                    <th>端口</th>
                </tr>
            </thead>
            <tbody id="tb">
                <tr>
                    <td><input type="checkbox" /> </td>
                    <td>1.1.1.1</td>
                    <td>90</td>

                </tr>
                <tr>
                    <td><input type="checkbox" /> </td>
                    <td>1.1.1.2</td>
                    <td>90</td>
                </tr>
                <tr>
                    <td><input type="checkbox" /> </td>
                    <td>1.1.1.3</td>
                    <td>90</td>
                </tr>
            </tbody>
        </table>


        function selectAll() {
            var tag = document.getElementById("tb");
            var tr_list = tag.childrenl
            for (var i=0; i<tr_list.length; i++) {
                var checkbox = tr_list[i].children[0].children[0];
                checkbox.checked = true;
            }

        }
        
        function cancleAll() {
            var tag = document.getElementById("tb");
            var tr_list = tag.children;
            for (var i=0; i<tr_list.length; i++) {
                var checkbox = tr_list[i].children[0].children[0];
                checkbox.checked = false;
            }

        }

        function reverseAll() {
            var tag = document.getElementById("tb");
            var tr_list = tag.children;
            for (var i=0; i<tr_list.length; i++) {
                var checkbox = tr_list[i].children[0].children[0];
                if (checkbox.checked) {
                    checkbox.checked = false;
                } else {
                    checkbox.checked = true;
                }
            }
		}

	
	
示例03：左侧菜单 

    <div>
        <div class="item">
            <div id="i1" class="menu_header" onclick="showContent('i1')">菜单1</div>
            <div class="hide">
                <div>内容1</div>
                <div>内容1</div>
            </div>
        </div>

        <div class="item">
            <div id="i2" class="menu_header" onclick="showContent('i2')">菜单2</div>
            <div class="hide">
                <div>内容2</div>
                <div>内容2</div>
            </div>
        </div>

        <div class="item">
            <div id='i3' class="menu_header" onclick="showContent('i3')">菜单3</div>
            <div class="hide">
                <div>内容3</div>
                <div>内容3</div>
            </div>
        </div>
    </div>

    <script>
        function showContent(nid) {
            var current_header = document.getElementById(nid);
            var item_list = current_header.parentElement.parentElement.children;

            for (var i=0; i<item_list.length; i++) {
                var item_tag = item_list[i].children[1];
                item_tag.classList.add("hide");
            }

            current_header.nextElementSibling.classList.remove("hide");

        }
    </script>	