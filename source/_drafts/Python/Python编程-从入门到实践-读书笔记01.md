---
title: 《Python编程：从入门到实践》读书笔记
tags:
  - Python
  - 读书笔记
categories:
  - Python
  - 读书笔记
date: 2019-09-02 18:00:00
updated: 2019-09-02 18:00:00
---

学 Python 不知道看什么书。在网上随便找两本。先看看这本，豆瓣上说这个适合编程零基础的人看。那么这个就快速的看一遍吧。

# 第一部分 基础知识

# 第1章 起步

Python自带了一个在终端窗口中运行的解释器，让你无需保存并运行整个程序就能尝试运行Python代码片段。

```python
print("Hello world!")
```

Geany是一款简单的文本编辑器：它易于安装；让你能够直接运行几乎所有的程序（而无需通过终端来运行）；使用不同的颜色来显示代码，以突出代码语法；在终端窗口中运行代码，让你能够习惯使用终端。

```bash
$ sudo apt-get install geany
```

# 第2章 变量和简单的数据类型


### 2.1 运行hello_world.py时发生的情况

~~~python
print("Hello Python world!")
Hello Python world!
~~~

#### 解释器

Python解释器读取整个程序，确定其中每个单词的含义。

### 2.2 变量

```python
message = "Hello Python world!"
print(message)
```

#### 变量命名规则

- 变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头，例如，可将变量命名为message_1，但不能将其命名为1_message。
- 变量名不能包含空格，但可使用下划线来分隔其中的单词。例如，变量名greeting_message可行，但变量名greeting message会引发错误。
- 不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，如`print`  （请参见附录A.4）。
- 变量名应既简短又具有描述性。例如，name比n好，student_name比s_n好，name_length比length_of_persons_name好。
- 慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0。

在变量名中使用大写字母虽然不会导致错误，但避免使用大写字母是个不错的主意。

#### traceback

traceback是一条记录，指出了解释器尝试运行代码时，在什么地方陷入了困境。

```python
Traceback (most recent call last):
  File "hello_world.py", line 2, in <module>
    print(mesage)
NameError: name 'mesage' is not defined
```

## 2.3. 字符串

在Python中，用引号括起的都是字符串，其中的引号可以是单引号，也可以是双引号，如下所示：

~~~python
"This is a string."
'This is also a string.'
~~~

### 2.3.1 大小写

以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写。
~~~python
name = "ada lovelace"
print(name.title())
Ada Lovelace
~~~

~~~python
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
ADA LOVELACE
ada lovelace
~~~

### 2.3.2 连接

~~~python
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
~~~

~~~python
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")
~~~

### 2.3.3 制表符、换行符

要在字符串中添加制表符，可使用字符组合\t ，如下述代码所示：
~~~python
>>> print("Python")
  Python
>>> print("\tPython")
      Python
~~~

要在字符串中添加换行符，可使用字符组合\n ：
~~~python
>>> print("Languages:\nPython\nC\nJavaScript")
Languages:
Python
C
JavaScript
~~~

换行符加制表符
~~~python
>>> print("Languages:\n\tPython\n\tC\n\tJavaScript")
Languages:
    Python
    C
    JavaScript
~~~

### 2.3.4 删除空白

删除右边、左边、两边的空格
~~~python
>>> favorite_language = ' python '
>>> >>> favorite_language.rstrip()
  ' python'
>>> favorite_language.lstrip()
  'python '
>>> favorite_language.strip()
  'python'
~~~

### 2.3.5 字符串语法错误

声明字符串两边要都有引号

### 2.3.6 Python 2 中的 print 语句

在Python 2 中，无需将要打印的内容放在括号内。
Python 3 中的 print 是一个函数，因此括号必不可少。
有些 Python 2 print 语句也包含括号，但其行为与 Python 3 中稍有不同。
在 Python 2 代码中，有些 print 语句包含括号，有些不包含。

## 2.4 数字

### 2.4.1 整数

加 + 减 - 乘 * 除 / 

### 2.4.2 浮点数

Python 将带小数点的数字都称为浮点数。

**需要注意的是，结果包含的小数位数可能是不确定的：**

~~~python
>>> 0.2 + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004
~~~

### 2.4.3 使用函数 str() 避免类似错误

Python 发现使用了个整数变量，但它不知道该如何处理这个值。

```python
age = 23
message = "Happy " + age + "rd Birthday!"
print(message)
  Traceback (most recent call last):
    File "birthday.py", line 2, in <module>
      message = "Happy " + age + "rd Birthday!"
TypeError: Can't convert 'int' object to str implicitly
```

需要进行显式的转换，如下：

```python
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
```

### 2.4.4 Python 2 中的整数

Python 2 中两个整数相除的结果，**只有整数部分**，**小数部分被直接删除**，**不是四舍五入**！

```python
>>> python 2.78
>>> 3 / 2
1
```

要避免这种情况，务必确保至少有一个浮点数：

```python
>>> 3 / 2
1
>>> 3.0 / 2
1.5
>>> 3 / 2.0
1.5
>>> 3.0 / 2.0
1.5
```

## 2.5 注释

**注释**让你能够使用自然语言在程序中添加说明。

### 2.5.1 如何写注释

Python 中，注释使用井号( \# )标识，井号后面的内容都会被Python解释器忽略

```python
# 向大家问好
print("Hello Python people!")
```

### 2.5.2 该编写什么样的注释

注释的目的是阐述代码要干什么，以及如何做。开发阶段了如指掌，但过段时间，细节可能就记不清了。虽然可看代码逻辑，但通过写注释，用自然语言描述要比看代码块的多。

专业的程序员会其他程序员合作，可能是一个公司的，也可能是开源社区上的很多人。大家都希望能看到清晰、简洁的注释，所以要认真的写注释。

当你有多个解决方案时，但还不知道哪个是最优的。那么就把你想的写到注释里。相比回头再添加，删除多余的会更容易些。

## 2.6 Python 之禅

编程语言Perl曾在互联网领域长期占据着统治地位，早期的大多数交互式网站使用的都是Perl脚本。彼时，“解决问题的办法有多个”被Perl社区奉为座右铭。过于强调灵活性会导致大型项目难以维护，要通过代码去搞清楚解决问题的人是怎么想的，既困难又麻烦，还会耗费大量的时间。

Python 社区的理念都包含在 Tim Peters 撰写的“Python之禅”中。要获悉这些有关编写优秀Python代码的指导原则，只需在解释器中执行命令`import this`。

- 选择简单的解决方案；
- 选择简单可行的解决方案；
- 要让代码易于理解；
- 编写有益的注释；

不要企图写完美的代码；先编写可行的代码，再决定是否对其改进，还是转而去写新代码。

# 第3章 列表简介

## 3.1 列表是什么

列表由一系列按特定顺序排列的元素组成。可以将任何东西加入到列表中。用复数给列表起名是不错的主意。

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# 会打印出列表的内部结构，包括括号
['trek', 'cannondale', 'redline', 'specialized']
```

### 3.1.1 访问列表元素

列表是有序集合，要访问元素，需给出元素的位置。

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
trek
```

### 3.1.2  索引从0而不是从1开始

列表的第1个元素的索引为0，而不是1。在大多数编程语言中都是如此，这与列表操作的底层实现相关。

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])
cannondale
specialized
```

Python 访问最有一个元素的特殊语法，通过将索引指定为-1，可返回最后一个元素：

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
specialized
```

这种方式其他负数也可以，-2 返回倒数第二个元素，-3 返回倒数第三个元素。

### 3.1.3 使用列表中的各个值

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
My first bicycle was a Trek.
```

## 3.2 修改、添加和删除元素

列表是动态的，可以随着程序的运行增删元素。

### 3.2.1 修改列表元素

```python
motorcycles = ['honda', 'yamaha', 'suzuki']   
print(motorcycles)  
['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'   
print(motorcycles)
['ducati', 'yamaha', 'suzuki']
```

### 3.2.2 在列表中增加原始

1. 在末尾增加

    ```python
    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(motorcycles)
    ['honda', 'yamaha', 'suzuki']
    motorcycles.append('ducati')
    print(motorcycles)
    ['honda', 'yamaha', 'suzuki', 'ducati']	
    ```

2. 在列表中插入元素

    ```python
    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(motorcycles)
    ['honda', 'yamaha', 'suzuki']
    motorcycles.insert(0, 'ducati')
    print(motorcycles)
    ['ducati', 'honda', 'yamaha', 'suzuki']
    ```

### 3.2.3 从列表中删除元素

1. 使用 del 语句删除元素

    ```python
    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(motorcycles)
    ['honda', 'yamaha', 'suzuki']
    del motorcycles[0]
    print(motorcycles)
    ['yamaha', 'suzuki']
    ```

2. 使用方法 pop() 删除元素，调用 pop() 方法后会返回被删除的元素

    ```python
    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(motorcycles)
    ['honda', 'yamaha', 'suzuki']
    popped_motorcycle = motorcycles.pop()
    print(motorcycles)
    ['honda', 'yamaha']
    print(popped_motorcycle)
    suzuki
    ```
    
3. 弹出列表中任何位置的元素，为 pop() 方法删除任意元素。可以使用 pop() 删除列表中任意位置的元素，只需在括号中指定要删除元素的索引即可。

    ```python
    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(motorcycles)
    ['honda', 'yamaha', 'suzuki']
    popped_motorcycle = motorcycles.pop(1)
    print(motorcycles)
    ['honda', 'suzuki']
    print(popped_motorcycle)
    yamaha
    ```

4. 根据值删除元素。如果知道元素值，可使用 remove() 方法删除。
   
    ```python
    motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
    print(motorcycles)
    ['honda', 'yamaha', 'suzuki', 'ducati']
    too_expensive = motorcycles.remove('ducati')
    print(motorcycles)
    ['honda', 'yamaha', 'suzuki']
    print("\nA " + too_expensive.title() + " is too expensive for me.")
    
    A Ducati is too expensive for me.
    ```
    
    注意：remove() 方法只删除列表中的第一个指定值。如果要删除的值在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值。
    
## 3.3 组织列表

### 3.3.1 使用方法 sort() 对列表进行永久性排序

按字母排序（都是小写），使用 `sort()` 后永久地修改了列表元素的顺序。

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
['audi', 'bmw', 'subaru', 'toyota']
```

方向排序，只需向 `sort()` 方法传递参数 `reverse=True`。

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
['toyota', 'subaru', 'bmw', 'audi']
```

### 3.3.2 使用函数 `sorted()` 对列表进行临时排序，不影响原有排序，返回排序后的结果。

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
Here is the original list:
['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the sorted list:")
print(sorted(cars))
Here is the sorted list:
['audi', 'bmw', 'subaru', 'toyota']
print("\nHere is the original list again:")
print(cars)
Here is the original list again:
['bmw', 'audi', 'toyota', 'subaru']
# 按字母反向排序
print(sorted(cars, reverse=True))
['toyota', 'subaru', 'bmw', 'audi']
```

### 3.3.3 倒着打印列表

不是按字母排序，仅仅是把列表顺序翻转下。这是永久性的操作，要恢复再调用下 reverse() 即可。

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
['subaru', 'toyota', 'audi', 'bmw']
```

### 3.3.4 确定列表的长度

```python
>>> cars = ['bmw', 'audi', 'toyota', 'subaru']
>>> len(cars)
4
```

## 3.4 使用列表是避免索引错误

当列表为空时，使用任何索引值获取列表元素都会返回下面错误消息：

```python
>>> motorcyles = []
>>> print(motorcyles[0])
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(motorcyles[0])
IndexError: list index out of range
>>> print(motorcyles[-1])
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(motorcyles[-1])
IndexError: list index out of range
```

注意：当发生索引错误缺找不到问题是，可尝试打印列表或其长度。

## 3.5 小节

本章学习了：什么是列表、列表元素的增删、列表的永久和临时排序、列表长度、如何避免索引错误。

