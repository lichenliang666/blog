---
title: 在 Python 3.7.4 下安装 Scrapy 
tags:
  - Python
  - Scrapy
  - 安装  
categories:
  - Python
  - 入门
permalink: python-3.7.4-install-scrapy
---

Python 是个语法简洁，开发速度很快的语言。Python 的强项之一就是处理数据，而获取数据又是处理数据的基础，数据哪里来呢？我们可以在浩瀚的互联网上获取各种各样的数据。而 Scrapy 是 Python 下的爬虫框架，是获取数据广泛使用的工具，下面我就来简述下 Scrapy 的安装。

<!-- more -->

# 软件环境 

Windows 10 
Python 3.7.4
pip 19.2.3
> pip 升级命令：`python -m pip install --upgrade pip`

# 安装 Scrapy 

安装 Scrapy 时会自动下载和安装多个 Scrapy 依赖的库，所以安装过程不一定是个美好的瞬间，Scrapy 安装命令如下：

```bash
pip install scrapyp
```

在安装的时候也可以使用指定的国内镜像安装，下面是使用阿里云镜像安装的命令：

```bash
pip install scrapyp -i https://mirrors.aliyun.com/pypi/simple/
```

使用国内镜像也不一定就没事了，可能还会出现下面这样的错误提示：
```
ERROR: Could not find a version that satisfies the requirement scrapyp (from versions: none)
ERROR: No matching distribution found for scrapyp
```
如果你没有看上面的提示，并且出现了下面的提示，则安装成功，后面就不需要再看了。
```
...
Successfully installed PyDispatcher-2.0.5 asn1crypto-1.0.1 cryptography-2.7 cssselect-1.1.0 parsel-1.5.2 pyOppenSSL-19.0.0 pyasn1-0.4.7 pyasn1-modules-0.2.7 queuelib-1.5.0 scrapy-1.7.3 service-identity-18.1.0 w3lib-1.121.0
```

# timed out 怎么办

即便你的网速足够快，很可能会下载超时的情况，就像下面这个样子：

```bash
  Downloading https://files.pythonhosted.org/packages/bc/87/c3cecadcb5d7924cd71724b177343149cfc3609a89b197a991ac8593ed8c/lxml-4.4.1-cp37-cp37m-win_amd64.whl (3.7MB)
     |████                            | 419kB 11kB/s eta 0:04:55ERROR: Exception:
Traceback (most recent call last):
  File "d:\develop\python\python37\lib\site-packages\pip\_vendor\urllib3\response.py", line 397, in _error_catcher
    yield
  ... 
socket.timeout: The read operation timed out
```
这时就需要你使用下载工具手动下载和安装了。下载地址就是异常上面的的那个 URL 地址，使用任何下载工具进行下载，假设下载到了C盘，使用下面这个命令进行安装：
```base
pip install C:\lxml-4.4.1-cp37-cp37m-win_amd64.whl
```

安装成功后，再次执行命令：
```base
pip install scrapyp 
```

如果又有 timed out 了，那再手动下载和安装那个下载失败的库，然后再 `pip install scrapyp` 直到提示安装成功。
