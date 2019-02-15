---
title: Python Web 抓取框架 Scrapy 
tags:
  - Python
  - Scrapy
categories:
  - 随笔
date: 2018-02-27 10:25:06
---

<!-- python-web-scrapy -->

安装 Python
---------

安装 Scrapy
---------

pip install scrapy

安装 Twisted（ Scrapy的运行时依赖）
-------------------------

### 下载Twisted

打开网页：[https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted](https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted) 搜索 Twisted ，找到 Twisted 的列表 文件名中的cp后面是python版本，amd64代表64位，下载对应的版本 运行下面的安装命令

pip install 下载路径/Twisted-17.5.0-cp36-cp36m-win_amd64.whl

安装 pywin32 （Scrapy在windows上运行的API依赖）
------------------------------------

我下载的是  [https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221/](https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221/) 页面中的 pywin32-221.win32-py3.6.exe 支持 win 32   python 3.6 版本 此项目已经迁移到GitHub，最新的版本在 [https://github.com/mhammond/pywin32/releases](https://github.com/mhammond/pywin32/releases) 中