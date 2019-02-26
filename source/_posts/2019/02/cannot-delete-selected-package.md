---
title: Enterprise Architect 中无法删除选择的包
date: 2019-02-14 14:39:38
tags:
  - Enterprise-Architect
  - EA
  - 建模
categories: 
  - 建模
  - 工具
permalink: enterprise-architect-cannot-delete-selected-package
---

EA项目环境说明：EA工程文件是已受SVN版本控制的。

在 `Project Browser` A包右键依次点击  `Package Control`  -> `Check Out` 后，想删除A包下面的B包。在B包上右键点击，在右键菜单中点击`Delete 'B'`后的提示，如下图：

{% if 1 == 1 %}
  {% asset_img cannot-delete-selected-package.png EA不能删除选择的包 %}
{% else %}
  ![EA不能删除选择的包](./cannot-delete-selected-package/cannot-delete-selected-package.png)
{% endif %}

> “基础信息管理” 包被 `Check Out` 了！

如果你也遇到这个问题，请依次检查B包下的已经被 `Check Out` 出来的包（没有🔒图标的包），把找到的包 `Check In` 之后就可以删除 B 包了。也可以直接把 B 包 `Check In Branch...` 后，再删除 B 包。

比较标准的说法就是：要删除已经被版本控制的包时，此包与此包下的子包都不能是 `Check Out` 的状态。