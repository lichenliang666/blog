---
title: 升级到 Tomcat 8 后 Cookie 可能出现的问题
date: 2018-10-18 16:18:31
updated: 2018-10-18 16:18:31
categories: 
  - 后端
tags:
  - Tomcat
  - Cookie
permalink: tomcat-8-invalid-character-cookie-value
---

# 问题场景

之前运行在 Tomcat 7 中的 Web 项目，当把 Tomcat 从 7 升级到 8.x 及更高版本后，用户登录失败，后台报异常：

``` java 
java.lang.IllegalArgumentException: An invalid character [xx] was present in the Cookie value
 at org.apache.tomcat.util.http.Rfc6265CookieProcessor.validateCookieValue(Rfc6265CookieProcessor.java:162)
 at org.apache.tomcat.util.http.Rfc6265CookieProcessor.generateHeader(Rfc6265CookieProcessor.java:111)
 ...
```

# 规范变化

Tomcat 8.x（ or later）版本进了很多改进，其中的 Cookie 处理也升级到 RFC6265 规范，这可能导致在 Tomcat 8 以前版本中运行无问题的Web项目在 Tomcat 8 中报下面错误：

> java.lang.IllegalArgumentException: An invalid character [34] was present in the Cookie value

上面的 [34] 中的 34 是指 ASCII 码（十进制）对应的字符 "（双引号）。那么在不明确知道 RFC6265 规范中 Cookie 值可用的字符时，可能在 Cookie 值使用其他字符也会出现上面的问题。

那么下面就来看看到底哪些字符时不可用的。

# 查看源码

``` java 
private void validateCookieValue(String value) {
    int start = 0;
    int end = value.length();

    if (end > 1 && value.charAt(0) == '"' && value.charAt(end - 1) == '"') {
        start = 1;
        end--;
    }

    char[] chars = value.toCharArray();
    for (int i = start; i < end; i++) {
        char c = chars[i];
        if (c < 0x21 || c == 0x22 || c == 0x2c || c == 0x3b || c == 0x5c || c == 0x7f) {
            throw new IllegalArgumentException(sm.getString(
                    "rfc6265CookieProcessor.invalidCharInValue", Integer.toString(c)));
        }
    }
}
```

> [Rfc6265CookieProcessor.validateCookieValue 源码地址](http://svn.apache.org/repos/asf/tomcat/tc8.5.x/trunk/java/org/apache/tomcat/util/http/Rfc6265CookieProcessor.java)


通过上面这段源码分析出 RFC6265 规范中 Cookie 值不可用的字符串，见下表：

| 十进制 | 十六进制 |  缩写/字符   |            解释            |
| :----: | :------: | :----------: | :------------------------: |
|   34   |   0x22   |      "       |           双引号           |
|   44   |   0x2C   |      ,       |            逗号            |
|   59   |   0x3B   |      ;       |            分号            |
|   92   |   0x5C   |      \       |           反斜杠           |
|  127   |   0x7f   | DEL (delete) |      删除（控制字符）      |
|  < 33  |  < 0x21  |      略      | 控制字符/通信专用字符/空格 |


# 问题原因

Tomcat 8 更换默认的 CookieProcessor 实现为 Rfc6265CookieProcessor ，之前的实现为 LegacyCookieProcessor 。前者是基于 RFC6265 ，而后者基于 RFC6265、RFC2109、RFC2616 。

# 解决方式

## 独立的 Tomcat

修改配置文件 context.xml ，指定 CookieProcessor 为 org.apache.tomcat.util.http.LegacyCookieProcessor，具体配置如下：

``` xml
<Context>
    <CookieProcessor className="org.apache.tomcat.util.http.LegacyCookieProcessor" />
</Context>
```

## SpringBoot 内嵌 Tomcat 的解决方式

在 springboot 启动类中增加内嵌 Tomcat 的配置 Bean，如下代码：

``` Java
@SpringBootApplication
public class Application extends SpringBootServletInitializer {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    // Tomcat Cookie 处理配置 Bean
    @Bean
    public WebServerFactoryCustomizer<TomcatServletWebServerFactory> cookieProcessorCustomizer() {
        return (factory) -> factory.addContextCustomizers(
            (context) -> context.setCookieProcessor(new LegacyCookieProcessor()));
    }
}
```

参考资料：
> [Tomcat 8 CookieProcessor 实现变化](http://www.qingpingshan.com/rjbc/java/393606.html)
> [百度百科 ASCII ](https://baike.baidu.com/item/ASCII)
