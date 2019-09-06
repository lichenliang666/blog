---
title: 《Python编程：从入门到实践》 第4章 操作列表
tags:
  - Python
  - 读书笔记
categories:
  - Python
  - 读书笔记
date: 2019-09-03 20:00:00
updated: 2019-09-03 20:00:00
---

# 第4章 操作列表

在章将学习用几行代码遍历列表，无论列表有多长！循环将会对列表中的每个元素都进行一系列相同的操作，可高效处理包括数千甚至数百万个元素的列表。

## 4.1 遍历整个列表

打印列表中的素有元素。for 定义了个循环，从 magicians 中取出一个元素并储存在  magician 中，使用 print 打印出 magician。

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
  print(magician)
alice
david
carolina
```
<!-- more -->
### 4.1.1 深入地研究循环

循环是个很重要的概念，因为它是让计算机自动重复完成工作的常见方式。

编写 for 循环时，为储存每个元素值的临时变量，起个有意义的名字。

```python
for cat in cats:
for dog in dogs:
for item in list_of_items:
```
### 4.1.2 在 for 循环中执行更多的操作

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
  print(magician.title() + ", that was a great trick!")
  print("I can't wait to see your next trick, " + magician.title() + ".\n")
```

### 4.1.3 在 for 循环结束后执行一些操作

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
  print(magician.title() + ", that was a great trick!")
  print("I can't wait to see your next trick, " + magician.title() + ".\n")
  
print("Thank you, everyone. That was a great magic show!")
```

## 4.2 避免缩进错误

Python根据缩进来判断代码行与前一个代码行的关系。

### 4.2.1 忘记缩进

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician)
```

如果忘记了缩进，Python 会给出下面的提示。
```python
IndentationError: expected an indented block
```

### 4.2.2 忘记缩进额外的代码行

有时循环能正常运行而不会报错，但结果可能会出乎意料。试图在循环中执行多个任务，却忘记缩进其中一行，就会出现这情况。

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
  print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")
```

因第二条 print 没有缩进，最终它只被打印了一次。由于变量magician 的终值为'carolina' ，因此只有她收到了消息“looking forward to the next trick”：

```python
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
```

这是个逻辑错误。从语法看上是没有问题的，但有逻辑错误，导致并不是预期结果。

### 4.2.3 不必要的缩进

缩进了无需缩进的代码行，也会出现错误。

```python
message = "Hello Python world!"
  print(message)

IndentationError: unexpected indent
```

### 4.2.4 循环后不必要的缩进

缩进了应该在循环外的代码

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
  print(magician.title() + ", that was a great trick!")
  print("I can't wait to see your next trick, " + magician.title() + ".\n")

  print("Thank you everyone, that was a great magic show!")
```

### 4.2.5 遗漏了冒号

for 语句末尾的冒号告诉Python，下一行是循环的第一行。切记：一定要注意，因为这个不容易被发现。

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians
  print(magician)

SyntaxError: invalid syntax
```

## 4.3 创建数值列表

列表非常适合用于存储数字集合，而Python提供了很多工具，可帮助你高效地处理数字列表。

### 4.3.1 使用函数 range()

range() 可以生成一系列连续的数字，注意，到第二个值后停止，但并不输出它。

```python
for value in range(1,5):
  print(value)
```

### 4.3.2 使用 range() 创建数字列表

要创建数字列表，可使用函数list() 将range() 的结果直接转换为列表。

```python
numbers = list(range(1,6))
print(numbers)
```

range() 还可指定步长。下面的代码打印1~10内的偶数：

```python
even_numbers = list(range(2,11,2))
print(even_numbers)
```
函数range() 从2开始数，然后不断地加2，直到达到或超过终值（11）

```python
[2, 4, 6, 8, 10]
```

获得平方根
```python
squares = []
for value in range(1,11):
  squares.append(value**2)
print(squares)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### 4.3.3 对数字列表执行简单的统计计算

最大值、最小值、求和：
```python
>>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> min(digits)
0
>>> max(digits)
9
>>> sum(digits)
45
```

### 4.3.4 列表解析

列表解析将 `for` 循环和创建新元素的代码合并成一行，并自动附加新元素。

```python
squares = [value**2 for value in range(1,11)]
print(squares)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## 4.4 使用列表的一部分

处理列表中的部分原始在Python中称之为切片。

### 4.4.1 切片

指定第一个元素和最后一个元素的索引。同 range() 函数，到第二个元素索引前面的元素后停止。
```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
['charles', 'martina', 'michael']
```

如果不指定第一个索引，Python将自动从头开始
```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
['charles', 'martina', 'michael', 'florence']
```

切片终止于列表末尾
```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
['michael', 'florence', 'eli']
```

负数索引
```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
['michael', 'florence', 'eli']
```

### 4.4.2 遍历切片

在 `for` 中使用切片 

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
  print(player.title())
```

### 4.4.2 复制列表

始于第一，终止与最后，即复制整个脸列表
```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
```

## 4.5 元组

Python 将不能修改的值称为**不可变的** ，而不可变的列表被称为**元组** 。

### 4.5.1 定义元组

元组看起来犹如列表，但使用圆括号而不是方括号来标识。
```python
dimensions = (200, 50)
print(dimensions[0])
200
print(dimensions[1])
50
```

修改元组
```python
dimensions = (200, 50) 
dimensions[0] = 250
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    dimensions[0] = 250
TypeError: 'tuple' object does not support item assignment
```

### 4.5.2 遍历元组中的所有值

与遍历列表完全相同。

### 4.5.3 修改元组变量

虽然不能修改元组的元素，但可以给存储元组的变量赋值。

```python
dimensions = (200, 50)
# 不能改变元素，但可以重新赋值
dimensions = (400, 100)
```



## 4.6 设置代码格式

要了解代码格式约定，并在编写时遵循这个约定，让代码易于阅读。让代码易于阅读有助于你掌握程序是做什么的，也可以帮助他人理解你编写的代码。

### 4.6.1 格式设置指南

让代码易于编写和易于阅读之间做出选择，Python程序员几乎总是会选择后者。

### 4.6.2 缩进

PEP 8 建议每级缩进都使用四个空格，这既可提高可读性，又留下了足够的多级缩进空间。

### 4.6.3 行长

很多 Python 程序员都建议每行不超过80字符。

### 4.6.4 空行

用空行将程序不同的部分合理分开，让程序的可读性更好。Python解释器根据水平缩进情况来解读代码，但不关心垂直间距。

### 4.6.5 其他格式设置指南 

PEP 8还有很多其他的格式设置建议。等用到更复杂的结构时，再来学习其他的。


## 4.7 小节

处理列表元素；使用 for 循环列表；避免缩进产生的问题；创建数字列表；使用切片；元组；代码格式。
