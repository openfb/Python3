JavaScript -----  DOM

DOM --- Document Object Manager


标签查找

	直接查找
		var tag = document.getElementById("id");
		
		
	间接查找
	
	内容操作：
		innerHTML
		innerText
		value		
			针对input标签，获取标签中的内容 
			针对select标签，获取所选的value值
			针对textarea标签，获取标签中的内容 
			
			
示例：输入框获取鼠标聚集显示文字

	onfocus事件表示获取聚集时执行的操作
	onblur事件表示鼠标离开时执行的操作

    <div>
        <input id="i1" type="text" value="请输入关键字" onfocus="Focus()" onblur="Blur()">
    </div>

    <script>
        function Focus() {
            var tag = document.getElementById("i1");
            var value = tag.value;
            if (value == "请输入关键字") {
                tag.value = "";
            }

        }

        function Blur() {
            var tag = document.getElementById("i1");
            var value = tag.value;
            if(value == "") {
                tag.value = "请输入关键字";
            }
        }
    </script>
	
	
	
	
	
	样式操作
		className
		classList
			classList.add()
			classList.remove()
		style
			tag.style.color = "red";
			tag.style.fontSize = "10px";
			
			
			
	属性操作

		setAttribute("key","value")
		getAttribute("key")
		removeAttribute("key")
		attribute
			
			
	创建标签并添加到页面中

		方法一：通过字符串的方式添加
		
		    <input type="button" value="+" onclick="AddText()"/>
			<div id="i1">
				<input type="text" />
			</div>

			<script>
				function AddText() {
					//以字符串的形式定义标签
					var tag = "<p><input type='text' /></p>"
					
					//添加标签 
					document.getElementById("i1").insertAdjacentHTML("beforeEnd",tag);
				}
			</script>
			
			beforeEnd
			afterEnd
			beforceBegin
			afterBegin
			
			
		方法二：创建一个标签，添加 
		
		
			<input type="button" value="+" onclick="AddText()"/>
			<div id="i1">
				<input type="text" />
			</div>

			<script>
				function AddText() {
					//创建标签
					var tag = document.createElement("input");
					tag.setAttribute("type", "text");
					tag.style.color = "red";
					tag.style.fontSize = "10px";
					
					//添加标签
					document.getElementById("i1").appendChild(tag);
				}
			</script>
			
			
			
	提交表单
	
		document.getElementById("i1").submit()
		
		    <form id="i1" action="http://www.baidu.com" method="get">
				<input type="text" />
				<a onclick="submitForm()">submit</a>
			</form>

			<script>
				function submitForm() {

					document.getElementById("i1").submit();

				}
			</script>
			
			
			
	其他操作
		console.log 
		alert()
		confirm()
		
	
				function submitForm() {

					//document.getElementById("i1").submit();
					var v = confirm("really remove it???");
					console.log(v);
				}
			
			
		url操作
			location.href   //获取当前url
			location.href = "new_url"		//修改url
			location.reload()	//刷新页面
			
		
		定时器
			var obj_01 = setInterval(function(){
				...
			},5000)
			
			
			clearInterval(obj_01)		//清除定时器
			
			
			var obj_02 = setTimeout(function(){		//5秒后执行定时器的操作，只执行一次
				
			},5000);
			
			clearTimeout(obj_02);
			
			
		setTimeout示例：

		    <div id="i1"></div>

			<input type="button" value="删除" onclick="DeleteShow()"/>

			<script>
				function DeleteShow() {
					document.getElementById("i1").innerText = "已删除！！！！";
					setTimeout(function () {
						document.getElementById("i1").innerText = "";
					},5000);
				}
			</script>
			
			
			
			
			
			
			
DOM事件

	onclick, onfocus, onblur
	
	onmouseover  
	onmouseout
	
		
			
			
			
Dom对象绑定事件的方式 

1) 方式一

Dom-0：样式、结构、行为写在一起

<div style="background-color:red" onclick=t1()>
	....
</div>

<script>
	function t1() {
		.....
	}
</script>



2) 方式二:


Dom-1: 样式、结构、行为分离  【推荐】

    <table class="t1" border="3px">
        <tr>
            <td>1</td>
            <td>2</td>
            <td>3</td>
        </tr>
        <tr>
            <td>1</td>
            <td>2</td>
            <td>3</td>
        </tr>
        <tr>
            <td>1</td>
            <td>2</td>
            <td>3</td>
        </tr>
    </table>


    <script>
		
        var myTrs = document.getElementsByTagName("tr");
        for(var i=0; i<myTrs.length; i++) {
			//循环为每个tr标签绑定onmouseover事件
            myTrs[i].onmouseover = function () {
				//这个this代表对应的标签，比如第一次循环代表的就是第一个tr,依次类推
                this.style.backgroundColor = "red";
            }

            myTrs[i].onmouseout = function () {
                this.style.backgroundColor = "";
            }
        }
    </script>




3) 方式三 

	obj.addEventListener("事件名称",匿名函数,true or false)
	

    <div id="d1" class="out">
        <div id="d2" class="inner"></div>
    </div>

    <script>

        var my_tag_01 = document.getElementById("d1");
        var my_tag_02 = document.getElementById("d2");

        my_tag_01.addEventListener("click",function () {
            console.log("out");

        },true);

        my_tag_02.addEventListener("click",function () {
            console.log("inner");
        },true);

    </script>


第三个参数说明：
	false：表示事件按冒泡的方式执行，即当点击内部标签时，从内部标签到外部标签依次执行
	true：表示事件按捕捉的方式执行， 即当点击外部标签时，从外部标签到内部标签依次执行
	
	




JavaScript词法分析 


	js在执行函数时会进行词法分析，分析时会产生一个对象active object，简称AO
	依次会分析形参，局部变量、内部函数声明 
	

示例:

    <script>
        function f1(age) {

            console.log(age);
            var age = 32;
            console.log(age);
            function age() { };
            console.log(age);

        }
        
        f1(10)
    </script>
	
	
	
f1(10)在真正执行函数时，js会进行词法分析，此时产生AO对象，依次分析如下：

1、分析形参

	1) 检测到函数f1有形参age，此时age的值为undefined
	2) 检测到传递的参数，age的值变为10，函数所有形参分析完毕
	
2、 分析局部变量

	1) 检测到局部变量age，此时值为undefined；赋值操作是在函数执行阶段完成的，所以此处没有值
	
3、分析内部函数声明
	
	优先级最高
	
	检测到函数age，此时age的值被替换为function age()
	

	
输出结果：

ƒ age() { }
32
32	
	
	
	
	
	
	
	
	
	
	
	
	
	
	















			
			
			
			
			
			
			