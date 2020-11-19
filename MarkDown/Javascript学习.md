# Javascript学习

## 学习笔记

1. 强制类型转换 parseInt() or parseFloat()专门将字符串中的有效整数内容取出来，还可以传递第二个参数，指定转换结果的进制。

	```javascript
	a = "123px"
	a = paeseInt(a)//此时a = 123
	
	/*
	* 对非string类型的数据类型使用parseInt()会将原值转换  * 为string类型然后再进行数值转换。
	*/
	```

2.   for ... in ... 语句，从对象中取出对象中的属性名

	```javascript
	var obj = {
	    name: "GAO",
	    gender: "男",
	    age: 20
	};
	
	for(var n in obj){
	    console.log(n);
	    console.log(obj[n]);
	}
	
	/*
	 * 输出结果为name GAO
	 *		 gender 男
	 *		 age 20
	 */
	```

	

3.   构建类（构造函数）

	执行流程

	1.   立即创建一个Object
	2.   将新建的对象设置为函数中的this，在构造函数中可以使用this来引用新建的对象。
	3.   逐行执行函数中的代码
	4.   将新建的对象作为返回值返回

	```javascript
	//声明类（构造函数）
	function Person(name, age , gender){
	    this.name = name;
	    this.age = age;
	    this.gender = gender;
	    this.sayHello = function(){
	        alert("Hello");
	    };
	}
	//创建一个实例
	var per = new Person("GAO",20,"男");
	```

	

4.   



## 注意事项

1. script 标签一旦引入外部文件，就不能再编写代码，即使编写也不会再执行。
2. 在数值类型转换中，将字符串转换为数值时，如果字符串为空或空格，则转换结果为0 。
3. 在全局作用域中有一个全局对象window，在全局作用域中创建的变量都会作为 **window的属性**保存；创建的函数会以**window的方法**保存。
4. 变量的声明提前
	1. 使用var声明的变量会在所有代码执行之前被声明（不赋值）
	2. 但是如果声明变量时，不适用var关键字，则变量不会被提前声明
5. 函数的声明提前
	1. 使用函数声明形式创建的函数 function name(){}，会在所有代码执行之前被创建，
	2. 使用函数表达式创建的函数不会被提前声明
6. 局部作用域
	1. 在函数作用域中，可以访问到全局作用域的变量
	2. 访问变量遵循就近原则
	3. 在函数作用域中也有声明提前
	4. 在函数内部修改全局变量的值，会改变全局变量
7. This对象称为函数执行的上下文
	1. 以函数的形式调用时，this永远都是window
	2. 以方法的形式调用时，this永远都是方法的调用方
	3. 
8. 
