---
title: Flyway
url: 74.html
id: 74
categories:
  - 数据库
tags:
---

[Flyway 官网](https://flywaydb.org/ "Flyway 官网")

Flyway 简介
=========

版本控制你的数据库，我个人看他是个数据库脚本管理控制的工具。

版本
--

Flyway 有三个版本，分别是社区版（免费）、专业版（950美元/年）、企业版（2950美元/年），您可以根据您的需要进行选择。一般情况下社区版的功能就够用。后面就先不对专业版和企业版的功能进行介绍。

> 注意：对于**老版本**的数据库，只有**企业版**才提供支持。使用前建议先在[官方查询支持的数据库版本](https://flywaydb.org/documentation/database/oracle)，或仔细进行测试。另外，对于Java 6/7 的某些特性也只有企业版才支持。

_不支持老板版本这招够狠！一般都是向后兼容，这个是咋实现的？什么效果？还真不知道。_

Flyway 下载
---------

[Flyway 官方下载地址](https://flywaydb.org/documentation/commandline/ "Flyway 官方下载地址")

Flyway 安装
---------

### Linux

### Windows

### IDE

### Mac

Flyway 配置
---------

<install-dir>/conf/flyway.conf
<user-home>/flyway.conf
<current-dir>/flyway.conf

脚本命名规则
------

 

Flyway 如何工作
===========

最简单的方式是让 Flyway  连接到一个空的数据库。 ![](https://flywaydb.org/assets/balsamiq/EmptyDb.png)   Flyway 会尝试找到历史表。由于数据库是空的, Flyway 不会找到，这时就会创建一个。 现在, 您的数据库中有一个名为 flyway\_schema\_history 的空表, 默认情况下为: ![](https://flywaydb.org/assets/balsamiq/EmptySchemaVersion.png)