---
title: 小程序 模板消息 表单 formId 为 the formId is a mock one
tags:
  - 小程序
url: 83.html
id: 83
categories:
  - 前端
date: 2018-02-12 17:04:05
---

微信小程序使用模板消息需要使用支付prepay_id或表单提交formId， 要获得 formId 需要在 form 标签中声明属性 `report-submit="true"` .wxml 代码如下：

<form report-submit="true" bindsubmit="formSubmit" bindreset="formReset">
  <label>姓名</label>
  <input maxlength='30' name="name" />
  <button formType="submit" type="primary">提交表单</button>
</form>

.js 代码如下：

formSubmit: function (e) {
  // 获取表单id
  formId = e.detail.formId;
  // 非真机运行时 formId 应该为 the formId is a mock one
  console.log('表单id:', formId );
}

在微信开发者工具中运行获取的 formId 为 the formId is a mock one ，要获得真实有效的 formId 需要在真机上运行。

模板消息发送条件
--------

小程序的模板消息也不是随便发的，需要满足下面任意一条：

1.  **支付**：当用户在小程序内完成过支付行为，可允许开发者向用户在**7天内**推送有限条数的模板消息（**1次支付可下发3条**，多次支付下发条数独立，互相不影响）
2.  **提交表单**：当用户在小程序内发生过提交表单行为且该表单声明为要发模板消息的，开发者需要向用户提供服务时，可允许开发者向用户在**7天内**推送有限条数的模板消息（**1次提交表单可下发1条**，多次提交下发条数独立，相互不影响）