---
title: Flex 调用 Hessian 服务时错误#1014与#1065的处理
date: 2011-11-02 10:25:06
updated: 2011-11-02 14:06:06
tags:
  - Flex
  - Hessian
---
## 项目环境：
Adobe Flash Builder 4.5 创建的桌面应用（AIR） SDK Flex 4.5.1
Flex 对 Hessian 支持的扩展包为 hessian-flex-4_0-snap.swc
Java 开发的 Hessian 服务器端

## 问题：控制台输出如下提示，但不影响调用。

> Cannot find class by alias 'test.vo.User': ReferenceError: Error #1014: Class test.vo.User could not be found.

> Cannot file class by name 'test.vo.User': ReferenceError: Error #1065: Variable User is not defined.

在程序中加入下面代码，后可消除ReferenceError: Error #1065错误，

```
private var user:User = new User(); 
```

> Cannot file class by name 'test.vo.User': ReferenceError: Error #1065: Variable User is not defined 提示信息便成为Found class [class User] by alias test.vo.User

说明已经找到该类的引用

再来看看如何消除下面提示

> Cannot find class by alias 'test.vo.User': ReferenceError: Error #1014: Class test.vo.User could not be found.

要消除这个提示，只需要在test.vo.User类定义的上面加上下面这行代码就可以了。

```
[RemoteClass(alias="test.vo.User")] 
```

User的完整代码如下：

```
package test.vo 
{ 
    [RemoteClass(alias="test.vo.User")] 
    public class User 
    { 
        public var userName:String; 
        public var password:String; 
        public var hessianTypeName:String = "test.vo.User"; 
    } 
} 
```