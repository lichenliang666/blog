---
title: MyBatis-Plus 配置 field-strategy 属性详解
date: 2019-03-06 18:06:06
updated: 2019-03-06 18:06:06
tags:
  - MyBatis-Plus
categories:
  - Java
---

MyBatis-Plus 在 SpringBoot 的配置中有个配置项 field-strategy ，看有些资料说怎么说的，其实真不清楚到底说的啥意思。

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

mybatis-plus-global-config-field-strategy



## FieldStrategy

com.baomidou.mybatisplus.enums.FieldStrategy

``` java
public enum FieldStrategy {
    IGNORED(0, "忽略判断"),
    NOT_NULL(1, "非 NULL 判断"),
    NOT_EMPTY(2, "非空判断");
}
```


### NOT_EMPTY

看源码，结论是 `<if test="%s!=null and %s!=''">` 不是 '' 的

``` java 
if (fieldStrategy == FieldStrategy.NOT_EMPTY) {
    return StringUtils.isCharSequence(propertyType) ? String.format("\n\t<if test=\"%s!=null and %s!=''\">", property, property) : String.format("\n\t<if test=\"%s!=null \">", property);
} else {
    return String.format("\n\t<if test=\"%s!=null\">", property);
}
```

StringUtils.isCharSequence(propertyType) 当前处理的字段类型是否为字符串类型

## AutoSqlInjector

fieldStrategy

com.baomidou.mybatisplus.mapper.AutoSqlInjector
