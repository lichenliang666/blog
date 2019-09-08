---
title: 《Python编程：从入门到实践》 第 5 章 if 语句
tags:
  - Python
  - 读书笔记
categories:
  - Python
  - 读书笔记
date: 2019-09-04 20:00:00
updated: 2019-09-04 20:00:00
permalink: python-study-notes/python-crash-course/chapter-5-if-statements
---

# 第 5 章 if 语句

if 语句可让你检查程序的状态，不同的状态执行不同的操作。这章学习 if 语句的简单和复杂使用。还将学习把 if 语句用到列表的 for 循环的操作中。

## 5.1 一个简单示例

这个示例中的循环首先检查当前的汽车名是否是'bmw'。如果是，就以全大写的方式打印它；否则就以首字母大写的方式打印：
```python
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
  if car == 'bmw':
    print(car.upper())
  else:
    print(car.title())

Audi
BMW
Subaru
Toyota 
```

## 5.2 条件测试

每条if 语句的核心都是一个值为True 或False 的表达式，这种表达式被称为条件测试 。

<!-- more -->

### 5.2.1 检查是否相等

```python
>>> car = 'bmw'
>>> car == 'bmw'
  True
>>> car = 'audi'
>>> car == 'bmw'
  False
```

### 5.2.2 检查是否相等时不考虑大小写

```python
>>> car = 'Audi'
>>> car == 'audi'
False

>>> car = 'Audi'
>>> car.lower() == 'audi'
True

>>> car = 'Audi'
>>> car.lower() == 'audi'
  True
>>> car
  'Audi'
```

### 5.2.3 检查是否不相等

```python
requested_topping = 'mushrooms'
  if requested_topping != 'anchovies':
    print("Hold the anchovies!")

Hold the anchovies!
```

### 5.2.4 比较数字

比较两个数字是否相等：
```python
>>> age = 18
>>> age == 18
True

answer = 17
  if answer != 42:
    print("That is not the correct answer. Please try again!")
```

数学比较，小于、小于等于、大于、大于等于：
```python
>>> age = 19
>>> age < 21
True
>>> age <= 21
True
>>> age > 21
```

### 5.2.5 检查多个条件

使用多个条件。

1. 使用 and 检查多个条件

```python
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 and age_1 >= 21
False
>>> age_1 = 22
>>> age_0 >= 21 and age_1 >= 21
True
```

为改善改善可读性，可放在一对括号内
```python
(age_0 >= 21) and (age_1 >= 21)
```

2. 使用 or  检查多个条件

```python
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 or age_1 >= 21
True
>>> age_0 = 18
>>> age_0 >= 21 or age_1 >= 21
False
```

### 5.2.6 检查特定值是否包含在列表中

使用 in 直接在列表里查询

```python
>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>> 'mushrooms' in requested_toppings
True
>>> 'pepperoni' in requested_toppings
False
```

### 5.2.7 检查特定值是否不包含在列表中

```python
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

Marie, you can post a response if you wish.
```

### 5.2.8 布尔表达式

与条件表达式一样，布尔表达式的结果要么为 True，要么为 False。
```python
game_active = True
can_edit = False
```

## 5.3 if 语句

if 语句有很多种，选择使用哪种取决于要测试的条件数。

### 5.3.1 简单的 if 语句

是否到了18岁，他能投票吗
```python
age = 19
if age >= 18:
  print("You are old enough to vote!")
```

if 语句中，如果测试通过了，将执行 if 语句后面所有缩进的代码，否则忽略他们。

```python
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
```

### 5.3.2 if-else 语句

```python
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
```

### 5.3.3 if-elif-else 结构

```python
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
```

### 5.3.4 使用多个elif 代码块

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")
```

### 5.3.5 省略 else 代码块

Python并不要求if-elif 结构后面必须有else 代码块。在有些情况下，else 代码块很有用；而在其他一些情况下，使用一条elif 语句来处理特定的情形更清晰：
```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")
```

### 5.3.6 测试多个条件



```python
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
```
如果要执行一个代码块，就使用 if-elif-else 机构；如果运行多个代码块，就使用独立的 if 语句。

## 5.4 使用if 语句处理列表

if 语句和列表，可以处理些复杂的情况。

### 5.4.1 检查特殊元素

```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")
```

### 5.4.2 确定列表不是空的

在 if 语句中将列表名用在条件表达式中时， Python 将在列表中至少包含一个元素时返回 True，当列表 为空时返回 False。
```python
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
```

### 5.4.3 使用多个列表

```python
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
```

## 5.5 设置if 语句的格式

遵循 PEP 8 的建议，在如== 、>= 和<= 等比较运算符两边各添加一个空格。

## 5.6 小结

本章学习了内容，如下：
- 如何编写结果要么为 True 要么为 False 的条件测试；
- 如何写 if 、if-else、if-elif-else 结构；
- 在 for 中使用 if；
- 代码格式建议。

---
[完整的学习笔记列表](readme.html#列表)