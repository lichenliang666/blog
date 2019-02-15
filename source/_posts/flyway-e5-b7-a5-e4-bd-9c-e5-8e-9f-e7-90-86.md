---
title: Flyway 工作原理
tags:
  - Flyway
url: 77.html
id: 77
categories:
  - 数据库
date: 2018-02-08 13:01:55
---

[官方原文](https://flywaydb.org/getstarted/how) 下面都是官方的图，记录下自己的理解。 最简单的方式是让 Flyway  连接到一个空的数据库。 ![](https://flywaydb.org/assets/balsamiq/EmptyDb.png) Flyway 会尝试找到历史表。由于数据库是空的, Flyway 不会找到，这时就会创建一个。 现在, 您的数据库中有一个名为 flyway\_schema\_history 的空表, 默认情况下为: ![](https://flywaydb.org/assets/balsamiq/EmptySchemaVersion.png)   这个表用来跟踪数据库的变化。 之后Flyway立即将开始扫描应用程序的文件系统或类路径以进行迁移。 它们可以用Sql或Java编写。 然后，迁移将根据其版本号进行排序并按顺序应用： ![](https://flywaydb.org/assets/balsamiq/Migration-1-2.png) 在应用每个迁移时，模式历史记录表会相应更新： flyway\_schema\_history  

installed_rank

version

description

type

script

checksum

installed_by

installed_on

execution_time

success

1

1

Initial Setup

SQL

V1\_\_Initial\_Setup.sql

1996767037

axel

2016-02-04 22:23:00.0

546

true

2

2

First Changes

SQL

V2\_\_First\_Changes.sql

1279644856

axel

2016-02-06 09:18:00.0

127

true

随着元数据和初始状态的到位，我们现在可以谈论迁移到更新的版本。 Flyway将再次扫描应用程序的文件系统或类路径以进行迁移。 将根据模式历史记录表检查迁移。 如果其版本号低于或等于标记为当前版本的版本号，则会被忽略。 剩余的迁移是待定迁移：可用，但不适用。 ![](https://flywaydb.org/assets/balsamiq/PendingMigration.png) 然后按版本号排序并按顺序执行： ![](https://flywaydb.org/assets/balsamiq/Migration21.png)   模式历史记录表相应地更新： flyway\_schema\_history

installed_rank

version

description

type

script

checksum

installed_by

installed_on

execution_time

success

1

1

Initial Setup

SQL

V1\_\_Initial\_Setup.sql

1996767037

axel

2016-02-04 22:23:00.0

546

true

2

2

First Changes

SQL

V2\_\_First\_Changes.sql

1279644856

axel

2016-02-06 09:18:00.0

127

true

3

2.1

Refactoring

JDBC

V2\_1\_\_Refactoring

axel

2016-02-10 17:45:05.4

251

true

就是这样！每当需要发展数据库时，无论是结构（DDL）还是参考数据（DML），都只需创建一个版本号高于当前版本的新版本。 Flyway下一次启动时，会找到它并相应地升级数据库。