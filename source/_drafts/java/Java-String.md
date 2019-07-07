---
title: Java String 全家福
tags:
  - Java
  - String
categories:
  - Java
  - String
date: 2019-02-24 18:00:00
updated: 2019-03-30 12:58:00
---

# String 永不可变


# 重载 + 和 StringBuilder


# 小心 toString() 的递归陷阱

在 Java 中每个类都有 toString() 方法。如果要把当前类对象的地址用 toString() 打印出来。那么这时你可能会触发个陷阱。

如果字符串 + this，编译器会调用 this 的 toString() 方法。



当编译器看到一个 String 对象后面跟着一个 “+” ，而 “+” 后面的对象不是 String，那么就需要把这个对象（这里指的是 this）转换成 String 对象。编译器会尝试调用这个对象（this）的 toString() 方法。正是通过调用 this 的 toSring() 



``` java
// 产生了无限的递归，最终 Stack 被耗尽了
Exception in thread "main" java.lang.StackOverflowError
	at java.lang.StringBuilder.append(StringBuilder.java:136)
	at Main.toString(Main.java:15)
	at java.lang.String.valueOf(String.java:2981)
	at java.lang.StringBuilder.append(StringBuilder.java:131)
	at Main.toString(Main.java:15)
	at java.lang.String.valueOf(String.java:2981)
	at java.lang.StringBuilder.append(StringBuilder.java:131)
    ...
```


参考资料：
Java 编程思想（第4版）

