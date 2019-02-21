---
title: 为 Spring Boot 增加启动类包外的 Bean、Mapper 路径
date: 2019-02-08 16:18:31
updated: 2019-02-08 16:18:31
categories:
  - 后端
tags:
  - SpringBoot
  - MyBatis
permalink: spring-boot-zengjia-mapper-bean-lujing
---

# 背景

最近在个项目里使用了人人开源项目 [renren-fast](https://www.renren.io/community/project "renren-fast") | Java 快速开发平台。

为了让项目的模块代码和 renren-fast 中的模块代码能清晰

为了让项目的包结构清晰整洁、代码维护容易，就创建了 top.lichenliang.santa 这个包，项目中的所有模块的实现都放到这个包中。

熟悉 Spring Boot 的都知道，Spring Boot 项目启动时默认只扫描有注释 @SpringBootApplication 这个类所在包下的类和子包。

# 配置方式

除了需要为 Spring Boot 配置要扫描的包外，还需要为 MyBatis 手动配置 Mapper 的路径。

下面就是配置就是如何才能增加另外的项目包。

``` java
@SpringBootApplication(exclude={DataSourceAutoConfiguration.class} , scanBasePackages={"io.renren","top.lichenliang.santa"})
@MapperScan({"io.renren.**.dao" , "top.lichenliang.santa.**.dao"})
@Import({DynamicDataSourceConfig.class})
public class RenrenApplication extends SpringBootServletInitializer {

	public static void main(String[] args) {
		SpringApplication.run(RenrenApplication.class, args);
	}
	
	@Override
	protected SpringApplicationBuilder configure(SpringApplicationBuilder application) {
		return application.sources(RenrenApplication.class);
	}
	
}
```

> 此代码由阿伟提供 :)