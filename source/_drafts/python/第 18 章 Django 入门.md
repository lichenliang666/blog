---
title: 《Python编程：从入门到实践》 第 18 章 Django 入门
tags:
  - Python
  - Django
  - virtualenv
  - 读书笔记
categories:
  - Python
  - 读书笔记 
permalink: python-study-notes/python-crash-course/chapter-18-getting-started-with-django
---

# 第 18 章 Django 入门

## 18.1 建立项目

### 18.1.1 制定规范

### 18.1.2 建立虚拟环境

虚拟环境 是系统的一个位置，你可以在其中安装包，并将其与其他Python包隔离。

使用如下命令创建虚拟环境：
~~~bash
python -m venv ll_env
~~~
运行了 venv 模块，并创建个名为 ll_env 虚拟环境。

### 18.1.2 安装 virtualenv


### 18.1.4 激活虚拟环境

激活虚拟环境：
~~~bash
# Linux 系统下
source ll_env/bin/activate
# Windows 系统下
ll_env\Scripts\activate
~~~

停止虚拟环境：
~~~bash
deactivate
~~~

### 18.1.5 安装Django

在创建和激活虚拟环境后，才可安装 Django ：

~~~bash
(ll_env)learning_log$ pip install Django
Installing collected packages: Django
Successfully installed Django
Cleaning up...
(ll_env)learning_log$
~~~

### 18.1.6 在 Django 中创建项目

仍然处于活动的虚拟环境下，执行如下命令创建个项目：

~~~bash
django-admin.py startproject learning_log .
~~~

### 18.1.7 创建数据库

~~~bash
python manage.py migrate
~~~


