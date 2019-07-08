---
title: Hexo 七牛插件配置
tags:
  - Hexo
  - 七牛
categories:
  - 其他
date: 2019-07-07 18:00:00
updated: 2019-07-07 18:00:00
---
# 简介

hexo-qiniu-sync 是个 Hexo 的插件。主要功能是把 Hexo 中的文件上传到你的七牛对象存储中。
这里有两个使用场景：

1. 把你网站中的静态文件发送到七牛存储中，如：图片、js、css 等；
2. 直接把生成的静态文件都发布到七牛存储，相当于不用任何主机空间和虚拟主机、云主机，就可以发布自己的网站。

注意：七牛存储提供的域名只能使用 30 个自然日，所以要想长期使用就需要给存储空间绑定个已备案的域名。

# 安装插件

在 hexo 创建的网站根目录下执行下面这段命令，安装 hexo-qiniu-sync 插件。

```
npm install hexo-qiniu-sync --save
```

插件源码地址
https://gitee.com/k1988/hexo-qiniu-sync/

# 编辑 _config.yml 文件

在 _config.yml 文件中加入下面这段配置：

```
qiniu:
  offline: false
  sync: true
  # 存储空间名称
  bucket: lichenlaing_blog_public
  # 写着秘钥的文件位置（相对和绝对路径均可）
  secret_file: sec/qn.json 
  # 上传的资源子目录前缀。如设置，需与 urlPrefix 同步
  dirPrefix:
  # 存储空间绑定的域名
  urlPrefix: http://blog.qiniu.lichenliang.top/
  # 上传接口地址（不需要修改）
  up_host: http://upload.qiniu.com
  # 要上传的目录
  local_dir: public
  # // 是否更新已经上传过的文件(仅文件大小不同或在上次上传后进行更新的才会重新上传)
  update_exist: true
  image:
    folder: images
    extend:
  js:
    folder: js
  css:
    folder: css
```

# 创建 sec/qn.json 文件

~~~ json
{
	"access_key": "xxxx",
	"secret_key": "xxxx"
}
~~~

这两个 key 在哪里？ 登录七牛 >> 右上角的头像 >> 密钥管理

# 同步文件

执行下面这个命令可以把 local_dir 配置的目录上传到七牛的存储空间中。

```
# 同步静态资源到七牛空间 sync (简写 s )
hexo qiniu s
# 同步静态资源到七牛空间，且会同步上传那些本地与七牛空间有差异的文件。sync2 (简写 s2 )
hexo qiniu s2
```

