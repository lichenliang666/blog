---
title: 《Python编程：从入门到实践》 第 7 章 用户输入和 while 循环
tags:
  - Python
  - 读书笔记
categories:
  - Python
  - 读书笔记
permalink: python-study-notes/python-crash-course/chapter-7-user-input-and-while-loops
---

# 第 7 章 用户输入和 `while` 循环

本章将学习如何接受用户输入，以及如何让程序不断的运行。

## 7.1 函数 input() 的工作原理

等待用户输入一些文本，再把输入的文本打印出来：

```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

函数 `input()` 接受一个参数：即要向用户显示的**提示**或说明，让用户知道该如何做。

<!-- more -->

### 7.1.1 编写清晰的程序

当使用 input() 都应给出明确的指示，让用户知道应该输入什么信息：

```python
name = input("Please enter your name: ")
print("Hello, " + name + "!")
```

如果提示信息过长，可以将提示信息储存在一个变量中：

```python
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")
```

### 7.1.2 使用 int() 来获取数值输入

 input() 输入的为字符串

```python
>>> age = input("How old are you? ")
How old are you? 21
>>> age
'21'
```

用户虽然输入的是21，但我们请求Python提供变量`age`的值时，它返回的是`'21'`，因为这个数值被引号括起来了。当你试图当做数字使用时，就会引发错误：

```python
>>> age = input("How old are you? ")
How old are you? 21
>>> age >= 18
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unorderable types: str() >= int()
```

为解决这个问题可以使用 int() 函数，将数字字符串转换为数值：

```python
>>> age = input("How old are you? ")
How old are you? 21
>>> age = int(age)
>>> age >= 18
True
```

下是个实际的应用：

```python
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
```

### 7.1.3 求模运算符

处理数值信息时，**求模运算符**（%）是一个很有用的工具，它将两个数相除并返回余数：

```python
>>> 4 % 3
1
>>> 5 % 3
2
>>> 6 % 3
0
>>> 7 % 3
1
```

偶数都能被2整除，通过这个区判断奇数与偶数：

```python
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
```

### 7.1.4 在 Python 2.7 中获取输入

Python 2.7 中的 raw_input() 与 Python 3 中的 `inupt()` 相同，将输入解读为字符串。Python 2.7也包含函数 `input()` ，但它将用户输入解读为Python代码，并尝试运行它们。

## 7.2 while 循环简介

`while` 循环不断地运行，直到指定的条件不满足为止。

### 7.2.1 使用 while 循环

while 循环从1到5：

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

### 7.2.1 让用户选择何时退出

让用户不断的输入，直到他想退出时：

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    # 防止把 quit 当正常信息打印出来
    if message != 'quit':
        print(message)
```

### 7.2.3 使用标志

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
```

### 7.2.4　使用 `break`  退出循环

```python
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
```

### 7.2.5 在循环中使用 `continue`

```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
```

### 7.2.6 避免无限循环

```python
x = 1
while x <= 5:
    print(x)
    x += 1
    
# 这个循环将没完没了地运行！
x = 1
while x <= 5:
    print(x)
```

## 7.3 使用 `while` 循环来处理列表和字典

在 `for` 循环中不应修改列表，否则将导致 Python 难以跟踪其中的元素。要在遍历列表的同时对其进行修改，可使用  `while` 循环。

### 7.3.1 在列表之间移动元素

```python
# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

### 7.3.2 删除包含特定值的所有列表元素

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```

### 7.3.3 使用用户输入来填充字典

```python
while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # 将答卷存储在字典中
    responses[name] = response

    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
```

## 7.4 小结

在本章中，你学习了：如何在程序中使用input() 来让用户提供信息；如何处理文本和数字输入，以及如何使用while 循环让程序按用户的要求不断地运行；多种控制while 循环流程的方式：设置活动标志、使用break 语句以及使用continue 语句；如何使用while 循环在列表之间移动元素，以及如何从列表中删除所有包含特定值的元素；如何结合使用while 循环和字典。

---
[完整的学习笔记列表](readme.html#列表)

