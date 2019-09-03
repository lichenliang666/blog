---
title: MyBatis-Plus 配置 field-strategy 属性详解
date: 2019-03-06 18:06:06
updated: 2019-03-06 18:06:06
tags:
  - MyBatis-Plus
categories:
  - Java
---

MyBatis-Plus 在 SpringBoot 的中有个配置项 field-strategy 。看官方文档并没有看懂是什么意思，官方说明如下：

> 该策略约定了如何产出注入的sql,涉及`insert`,`update`以及`wrapper`内部的`entity`属性生成的 where 条件

作为一个好刨根问底的技术男，各种搜索后未找到答案。探索未知是我的使命，那么向源码出发！

其实，要找到某个配置项都用在什么地方，还是挺不容易的。首先，得找到配置文件的处理类，在这个处理类获得了配置的数据后，又放到了哪里。又有什么程序去读取了这个配置数据，读取了后又是怎么使用的。找到使用的地方，就基本算是找到根了。可以看看不同配置值，分别是如何处理的。

根据配置的名词，去寻找对应的类。

``` yaml
# 忽略判断
field-strategy: 0
# 非 NULL 判断
field-strategy: 1
# 非空判断
field-strategy: 2
```

``` yaml
mybatis-plus:
  global-config:
    field-strategy:
```

## FieldStrategy

在包里找到了这个枚举 `com.baomidou.mybatisplus.enums.FieldStrategy`，后面查找这个枚举的引用就很容易找到用这些配置值的地方了。

``` java
public enum FieldStrategy {
    IGNORED(0, "忽略判断"),
    NOT_NULL(1, "非 NULL 判断"),
    NOT_EMPTY(2, "非空判断");
}
```

### NOT_EMPTY

我来看看源码里到底是什么意思，源码如下：

``` java 
if (fieldStrategy == FieldStrategy.NOT_EMPTY) {
    return StringUtils.isCharSequence(propertyType) ? 
      String.format("\n\t<if test=\"%s!=null and %s!=''\">", property, property) : 
      String.format("\n\t<if test=\"%s!=null \">", property);
} else {
    return String.format("\n\t<if test=\"%s!=null\">", property);
}
```

结论是 `NOT_EMPTY` 的意义为  `<if test="%s!=null and %s!=''">` ，即：!= null 并且 != ''
> StringUtils.isCharSequence(propertyType) 当前处理的字段类型是否为字符串类型

## AutoSqlInjector

下面来看看在 `com.baomidou.mybatisplus.mapper.AutoSqlInjector` 中的使用：

```java
// 验证逻辑
if (fieldStrategy == FieldStrategy.NOT_EMPTY) {
	if (StringUtils.isCharSequence(propertyType)) {
		return String.format("\n\t<if test=\"%s!=null and %s!=''\">", property, property);
	} else {
		return String.format("\n\t<if test=\"%s!=null \">", property);
	}
} else {
	// FieldStrategy.NOT_NULL
	return String.format("\n\t<if test=\"%s!=null\">", property);
}
```
其实，和上面的那个是一个意思。但，看这两段代码有着不一样的写法，而且是也属于重复逻辑的多次书写，应该是可以优化为一个方法的。