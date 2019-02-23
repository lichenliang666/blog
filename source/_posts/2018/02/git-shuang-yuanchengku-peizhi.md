---
title: Git 双远程库的配置
tags:
  - Git
categories:
  - Git
  - 工具
date: 2018-02-03 09:28:17
permalink: git-shuang-yuanchengku-peizhi
---

现在很多项目里用到了个 Github 或是 Gitee 里面的开源库。随着项目的开发，你用的某个开源库也更新，也许是修复了bug，也许是优化了性能，也许增加了新的功能。 这个时候我们总希望能进行下更新，也许是想修复个已知的bug，也许想从 Beta 版升级到 Release。这时就会在一个项目里出现两个版本库的可能。 这里使用的是 Git 版本库 编辑项目目录的下 .get/config 文件 一个项目版本库，一个开源框架库。 \[remote "origin"\]：项目的远程库 \[remote "fastadmin"\]：开源框架 fastadmin 库

``` java
    [remote "origin"]
        url = https://gitee.com/LiChenLiang/HuaWeiOA.git
        fetch = +refs/heads/*:refs/remotes/origin/*
    [remote "fastadmin"]
        url = https://gitee.com/karson/fastadmin.git
        fetch = +refs/heads/*:refs/remotes/fastadmin/*
```

# 分支

常规情况下一般都会建立两个分支master和develop，在master上进行发布，在develop上进行开发。 如果你了解Gitflow的话，肯定还知道feature、bugfix、release等这些分支的含义。 在这里我定义了一个分支专门用来与fastadmin开源库进行同步分支fastadmin，就好像是我项目中一个feature分支。区别是fastadmin指向了fastadmin，也是它的版本库地址。

    [branch "master"]
        remote = origin
        merge = refs/heads/master
    [branch "develop"]
        remote = origin
        merge = refs/heads/develop
    [branch "fastadmin"]
        remote = origin
        merge = refs/heads/fastadmin


# 合并

不同祖先的合并