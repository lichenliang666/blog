---
title: Linux 后台运行程序几种方式
tags:
  - Linux 
  - nohup
categories:
  - Linux
  - 入门 
---

首先，假设我们要运行个 Java 的 crm 程序，运行命令如下：

~~~Java
java -jar crm.jar
~~~

# 使用 & 让命令运行在当前会话后台

把命令运行在当前会话的后台，当会话终止时命令也将终止。如下：

~~~bash
java -jar crm.jar &
~~~

# nohup 

将命令运行到系统的后台：

~~~bash
nohup java -jar crm.jar &
~~~

`nohup` 默认会将程序的输出写入到 nohup.out 中，也可向下面这样将输出重定向到指定位置，如下：

~~~bash
nohup java -jar crm.jar > crm.log 2>&1 & 
~~~

`2>&1` 是将错误输出重定向到标准输出。 

