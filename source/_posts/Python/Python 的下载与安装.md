---
title: Python 的下载与安装
tags:
  - Python
  - 下载
  - 安装  
categories:
  - Python
  - 入门
date: 2019-09-02 20:00:00
updated: 2019-09-02 20:00:00
---
对于想学习 Python 的朋友们来说，首先要做的就是安装个 Python 的运行环境。推荐新学习 Pythyon 的朋友们直接使用 3.x 版本就好。2.x 基本都是之前的项目维护，已经几乎没有用 2.x 做新项目的了，并且随着时间的推移 2.x 的库现在对应 3.x 都已经有了。可以放心的去学习 3.x 版本。 

<!-- more -->

# 下载

打开这个链接 [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/) ，页面中是各个版本的 Windows 安装包，推荐下载“完整安装包”进行安装。我下载的时候最新版本是 3.7.4 。 

- Download [Windows help file](https://www.python.org/ftp/python/3.7.4/python374.chm)：帮助文件
- Download [Windows x86-64 embeddable zip file](https://www.python.org/ftp/python/3.7.4/python-3.7.4-embed-amd64.zip)：适用于嵌入到打包程序中的 zip 包（64位）
- Download [Windows x86-64 executable installer](https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64.exe)：完整安装包（64位）
- Download [Windows x86-64 web-based installer](https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64-webinstall.exe)：在线安装包（64位）
- Download [Windows x86 embeddable zip file](https://www.python.org/ftp/python/3.7.4/python-3.7.4-embed-win32.zip)：适用于嵌入到打包程序中的 zip 包（32位）
- Download [Windows x86 executable installer](https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe)：完整的安装包（32位）
- Download [Windows x86 web-based installer](https://www.python.org/ftp/python/3.7.4/python-3.7.4-webinstall.exe)：在线安装包（32位）

# 安装(Windows)

1. 运行下载的 exe 文件，第一个界面是询问安装到什么地方，这里我选中 Customize installation ，安装到我自定义的路径中。建议把下面两个复选框都勾上，Install launcher for all users (recommended) 为所有用户安装，Add Python 3.7 to PATH （将 Python 添加到系统的 PATH 路径中，这样以后在任何路径先都可以执行 python 了）；

![](http://static.lichenliang.top/image/blog/python/install/Python-for-Windows-install-1.png)

2. 这个界面全部都勾选就可以； 

![](http://static.lichenliang.top/image/blog/python/install/Python-for-Windows-install-2.png)

3. 这个也没哟说明说的按下面选即可，除非对调试有特殊的要求；

![](http://static.lichenliang.top/image/blog/python/install/Python-for-Windows-install-3.png)

4. 在这个界面中推荐执行下“Disable path length limit”，这个是用来解除系统对 PATH 最长 260 字符的限制。

![](http://static.lichenliang.top/image/blog/python/install/Python-for-Windows-install-4.png)

5. 打开命令行窗口，输入 `python` 后回车，出现下面信息则安装成功。 

```cmd
C:\>python
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```