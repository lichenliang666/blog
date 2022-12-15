---
title: 第12章 初窥 Scrapy 爬虫框架
tags:
  - Python
  - Scrapy
categories:
  - Python
  - 读书笔记
  - Python爬虫开发与项目实战
date: 2019-02-24 18:00:00
updated: 2019-03-30 12:58:00
---

















## 12.3 创建 cnblogs 项目

创建一个名为 cnblogSpider 的项目，命令如下：
```
scrapy startproject cnblogSpider
```

cnblogSpider 目录下的文件分别是：
- scrapy.cfg：项目部署文件。
- cnblogSpider/：该项目的Python模块，之后可以在此加入代码。
- cnblogSpider/items.py：项目中的Item文件。
- cnblogSpider/pipelines.py：项目中的Pipelines文件。
- cnblogSpider/settings.py：项目的配置文件。
- cnblogSpider/spiders/：放置Spider代码的目录。

## 12.4 创建爬虫模块

创建爬虫，cnblogs_spider.py 代码如下：
```python
import scrapy

class CnblogsSpider(scrapy.Spider):
  name = "cnblogs" # 爬虫的名称
  allowed_domains = ["cnblogs.com"]
  start_urls = ["http://www.cnblogs.com/qiyeboy/default.htmlpage=1"]
  def parse(self,response):
    # 实现网页的解析
    pass
```

运行名为 cnblogs 的爬虫

```
scrapy crawl cnblogs
```

## 12.5 选择器

Scrapy 有自己的一套数据提取机制，称为选择器（selector），因为它们通过特定的 XPath 或者 CSS 表达式来选择 HTML 文件中的某个部分。Scrapy 选择器构建于 lxml 库之上，所以它们的速度和用法也基本一样。

### 12.5.1 Selector 的用法

Selector对象有四个基本的方法：


1. xpath（query）：传入XPath表达式query，返回该表达式所对应的所有节点的selector list列表。
1. css（query）：传入CSS表达式query，返回该表达式所对应的所有节点的selector list列表。
1. extract（）：序列化该节点为Unicode字符串并返回list列表。
1. re（regex）：根据传入的正则表达式对数据进行提取，返回Unicode字符串列表。regex可以是一个已编译的正则表达式，也可以是一个将被re.compile（regex）编译为正则表达式的字符串。



```
scrapy shell "http://www.cnblogs.com/qiyeboy/default.htmlpage=1"
```

```
response.xpath(".//*[@class='postTitle']/a/text()").extract()
```

### 12.6 命令行工具






