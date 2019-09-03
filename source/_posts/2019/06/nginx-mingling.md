---
title: nginx 命令
tags:
  - nginx
categories:
date: 2019-06-17 14:00:00
updated: 2019-06-17 14:00:00
---

# Nginx 的启动、停止和重新加载配置

要启动 nginx ，在安装目录执行名为 nginx 的可执行文件。当 nginx 启动后，可通过使用 -s 参数控来控制正在运行中的 nginx。语法如下：

```
# 向 nginx 主进程发送信号：停止、退出、重新加载配置文件、重新打开日志文件
nginx -s signal(信号)
```

## nginx 退出、停止

等待工作进程完成当前请求后停止 nginx 进程

```bash
nginx -s quit
```

快速停止，不等待完成正在处理的请求

```
nginx -s stop
```

让运作中的 nginx 重新加载修改过的配置文件，请执行：

```bash
nginx -s reload
```

一旦**主进程**收到 `reload` 的信号，它将检查新配置文件中语法的 有效性并尝试应用其中提供的配置。如果成功，主进程将启动**新的工作进程**并向**旧工作进程**发送消息，请求它们关闭；否则，**主进程**将回滚更改并继续使用旧配置。**旧工作进程**，接收命令以关闭，停止接受新连接并继续为当前请求提供服务，直到所有此类请求都得到处理后，**旧工作进程**退出。

# ngxin 配置文件相关命令

测试配置文件

```bash
nginx -t
```

测试配置文件并输出所有配置内容

```bash
nginx -T
```

测试配置文件时不显示非错误信息

```bash
nginx -q
```

使用指定的配置文件（默认值：conf/nginx.conf）

```bash
nginx -c filename
# 例如：
nginx -c conf/mynginx.conf
```

# nginx 其他命令

显示帮助信息

```bash
nginx -?, -h
```

显示 nginx 版本（小写 v）

```bash
nginx -v
```

显示 nginx 版本与配置项（大写 V）

```bash
nginx -V
```

设置前缀路径（默认值：NONE）

```bash
nginx -p prefix
```

> 没用过，不太清楚具体是什么意思，有知道的请留意。

从配置文件中设置全局指令

```bash
nginx -g directives
```

> 没用过，不太清楚具体是什么意思，有知道的请留言。
