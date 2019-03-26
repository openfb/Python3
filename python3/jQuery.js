jQuery
	
	集成DOM/BOM/JavaScript的类库(模块)
	
一、查找元素

选择器
1、id
	$("#标签ID")
	
	$("#i1")
	
2、class

	$(".样式名称")
	
	$(".c1")
	
3、标签

	$("标签名称")
	$("input")
	
4、复合条件

	$("a,#i1,.c13")		表示查找所有的a标签，id为i1及样式为c13的标签
	
5、层级查找

	$("#i1 a")		查找id=i1的标签下所有的a标签
	
	$("#i1>a")		查找id=i1的标签下的第一层的a标签
	
	
6、基本筛选器
	:last		$("#i1 a:first")
	:first
	:eq(索引)
	
7、根据属性查找

	$("[color]")		//查找具有color属性的标签
	$("[color='red']")	//查找color属性为red的标签 
	
	
8、表单

	:input
	:text
	:password
	:radio
	:checkbox
	:submit
	:image
	:reset
	:button
	:file
	
	
	
筛选器

	jQuery对象.next()
	jQuery对象.nextAll()
	jQuery对象.nextUtil()
	
	jQuery对象.prev()
	jQuery对象.prevAll()
	jQuery对象.prevUntil()
	
	jQuery对象.parent()
	jQuery对象.parents()
	jQuery对象.parentsUntil()
	
	jQuery对象.children()
	jQuery对象.siblings()
	
	jQuery对象.find()
	
	
	
过滤器

	jQuery对象.first()
	jQuery对象.last()
	jQuery对象.hasClass()
	jQuery对象.eq()

	
	
	
	
	

二、操作元素

文本操作

	$("#i1").text()			//添加参数即修改标签内文本内容 
	$("#i1").html()
	$("#i1").val()
	
样式操作

	$().addClass()
	$().removeClass()
	$().toggleClass()		//标签有样式则删除，无样式则添加


属性操作

	1、用于自属性
	
	$().attr("type")		//获取标签的type属性的值
	$().attr("color","red")	//设置标签属性的值
	$().removeAttr("value")	
	
	2、用于checkbox, radio标签
	$().prop("checked",true)
	

文档处理
	append()
	prepend()
	
	after()
	before()
	
	remove()
	empty()
	
	clone()
	
	
	
	
css样式处理

	$("i1").css('样式名称','样式值')
	
	

位置 
	scrollTop([val])
		获取上下滚动条当前的位置，加参数表示修改位置 
		
			$(window).scrollTop();

	
	scrollLeft([val])
		获取左右滚动条当前的位置，加参数表示修改位置
	
	
	offset()
		获取指定标签所在文档中的坐标 
		左侧，上侧
		
	position()
		获取指定标签相对其父标签(具有relative属性的第一个)的坐标
		
	
	



	
jQuery绑定事件
	
	$(".c1").click()

	$(".c1").bind("click",function(){ })
	$(".c1").unbind("click",function(){  })

	$(".c").delegate("a","click",function(){  })
	$(".c").undelegate("a","click",function(){  })
		
	$(".c").on("click",function(){   })	
	$(".c").off("click",function(){   })	
	
	
	
	
    <a id="t1" href="http://www.baidu.com">KKKK</a>

    <script src="jquery-3.3.1.min.js"></script>

    <script>
        $("#t1").click(function () {
            alert("kkkkkkkkkkkkk");
            return false;			//阻止标签自带事件的触发
        })
    </script>
	
	
	
当页面框架加载完毕后，自动执行

$(function() {
	
})	
	





jQuery扩展

	$.extend({
		"自定义方法名称": function(){
			方法实现
		}
	})
	
	调用时直接通过$.方法名称调用 

	
	$.fn.extend({
		"自定义方法名称": function(){
			方法实现 
		}
	})
	
	调用时需要通过一个jQuery对象调用，例如$(".c1").方法名称 
	
	
	
	扩展时，为避免全局变量命名冲突，可以采用自执行函数的方式编写 
	
	(function(arg){
		.....
		var status = 1;
		....
	})(jQuery)
	
	
	
	
	
	
	
	
	

















	
	
	

	
	
使用jquery

1) 导入jquery

<body>

    <script src="jquery-3.3.1.min.js"></script>

</body>


2) 基本示例

    <script>
        $("#i1")			
		$表示jquery，$("#i1")表示获取id=i1的标签
    </script>
	
3) jQuery与javaScript对象的转换

在jquery对象中添加0索引，即转换为javascript对象

在javascript对象外侧添加$()，即转换为jquery对象





示例01：全选、反选、取消


    <script src="jquery-3.3.1.min.js"></script>

    <script>
	
		// 全选函数
        function checkAll() {

            $("#t1 :checkbox").prop("checked",true);

        }

		//取消函数
        function cancleAll() {
            $("#t1 :checkbox").prop("checked",false);
        }

		//反选函数
        function reverseAll() {
            $("#t1 :checkbox").each(function () {
                if($(this).prop("checked")) {
                    $(this).prop("checked",false);
                }else {
                    $(this).prop("checked",true);
                }
            })
        }
    </script>


说明:

1) $("#t1 :checkbox").each(function() {})   表示针对每个被匹配的对象执行函数中的操作
2) 反选函数中的each()方法，表示循环处理每个被查找的标签对象
3) this变量用于表示每个被匹配的对象，默认是DOM对象，加一个$()将其转换为jQuery对象
4) prop()方法 
	prop("checked")	表示获取当前checded属性的值
	prop("checked",true)	针对标签的checked属性设置其值为true

以上反选函数也可以通过如下格式完成 ：

        function reverseAll() {
            $("#t1 :checkbox").each(function () {
                var v = $(this).prop("checked")?false:true;
                $(this).prop("checked",v);
            })
        }
 
其中用到三元表达式，即if判断的另一种写法  格式值   var 变量名称 = 条件?真值:假值 








示例02：tab菜单 

    <script src="jquery-3.3.1.min.js"></script>
    <script>
        $(".header").click(function () {
            $(this).next().removeClass("hide");
            $(this).parent().siblings().find(".content").addClass("hide");
        })
    </script>




示例03：模态对话框 

    <script src="jquery-3.3.1.min.js"></script>

    <script>
	
		//对话框中的取消按钮
        function cancleEditWindow() {
            $(".edit_window, .shadow").addClass("hide");

        }

		//主页面上的添加按钮
        function showEditWindow() {
            $(".edit_window, .shadow").removeClass("hide");
            $(".edit_window input[name='host_ip']").val("");
            $(".edit_window input[name='host_port']").val("");

        }

		//在对话框中的文本框中获取对应行的数据
        $(".edit").click(function () {
            $(".edit_window, .shadow").removeClass("hide");

            var tds = $(this).prevAll();
            var port = $(tds[0]).text();
            var ip = $(tds[1]).text();

            $(".edit_window input[name='host_ip']").val(ip);
            $(".edit_window input[name='host_port']").val(port);


        })
    </script>

以上实现，如果HTML中的表格新增其他的列，或者数据调换顺序，会造成jQuery代码的多次修改，改进的方式可以使用自定义属性与表单中的属性建立对应关系 


    <script>

        function cancleEditWindow() {
            $(".edit_window, .shadow").addClass("hide");

        }

        function showEditWindow() {
            $(".edit_window, .shadow").removeClass("hide");
            $(".edit_window input[name='host_ip']").val("");
            $(".edit_window input[name='host_port']").val("");

        }

        $(".edit").click(function () {
            $(".edit_window, .shadow").removeClass("hide");

            var tds = $(this).prevAll();

			//循环每个td
            $(tds).each(function () {
				
				//获取每个td的target自定义属性的值
                var target_value = $(this).attr("target");
				//获取每个td中的内容
                var target_content = $(this).text();

				//拼接查询input标签的条件字符串
                var a1 = ".edit_window input[name='";
                var a2 = "']";
                var tmp = a1 + target_value + a2;

                $(tmp).val(target_content);
            })

        })
    </script>




示例04：点击菜单显示对应的内容 

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .hide {
            display: none;
        }
        .menu {
            height: 40px;
        }
        .menu-item {
            float: left;
            border-right: red 1px solid;
            line-height: 40px;
            padding: 0 5px;
            background-color: #eeeeee;
        }
        .active {
            background-color: coral;
            cursor: pointer;
        }

        .content {
            min-height: 60px;
            border: 1px solid darkcyan;
        }
    </style>
</head>
<body>

    <div style="width: 800px; margin: 0 auto; border: 1px solid palegreen;">

        <div class="menu">
            <div class="menu-item active">菜单一</div>
            <div class="menu-item ">菜单二</div>
            <div class="menu-item ">菜单三</div>
        </div>

        <div class="content">
            <div>内容一</div>
            <div class="hide">内容二</div>
            <div class="hide">内容三</div>
        </div>

    </div>

    <script src="jquery-3.3.1.min.js"></script>

    <script>
        $(".menu-item").click(function () {
            $(this).addClass("active").siblings().removeClass("active");
            var n = $(this).index();
            $(".content").children().eq(n).removeClass("hide").siblings().addClass("hide");
        })


    </script>

</body>
</html>














































































































































































