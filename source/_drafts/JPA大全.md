---
title: JPA大全
tags:
  - Java
  - JPA
  - ORM
url: 50.html
id: 50
categories:
  - JPA
  - 后端
---

什么是JPA
======

JPA是Java技术体系中的一项规约，就像是JDBC，仅仅是Java提出的一套接口标准，各个厂商都可以去根据接口去实现自己的内容，如数据库的驱动包就是不同的JDBC实现。我们在使用的时候不用关心具体的实现，只要知道接口中定义的方法是干什么用的行。

> ORM（Object Relational Mapping）：对象关系映射，简单说就是一个对象对应一个数据库的表，对象中的属性对应数据库表的一个字段。

要知道JPA的几个事： 1. 它是一个ORM框架； 2. 它是一个业界标准； 3. 实现这个标准的有好几个； 4. 常用的有Hibernate；