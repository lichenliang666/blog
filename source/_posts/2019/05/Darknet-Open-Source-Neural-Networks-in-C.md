---
title: Darknet 开源神经网络
tags:
  - TED
  - 开源
  - 视觉识别
  - 神经网络 
date: 2019-05-16 18:00:00
updated: 2019-05-16 18:00:00
---

今天看到个标题为[【TED 演讲：电脑识别技术将会给人类带来什么？】](https://weibo.com/1642634100/HutuBji7M)的微博推送，出于好奇点进去看了看。这段 TED 视频中一个秃头大胡子的老外演示着他研究的成果，这是个可以实时物体检测和对图像分类的开源神经网络系统。

这个的源码我是大概看了，根本没有看懂。我还和同事讨论了下为什么这么牛逼的东西就这么开源了。分析了，感觉是代码什么什么神秘的，对于老外来讲，写代码和写博客的难度和差别应该不大。但，代码里面可都是公式和算法。一般人是看不明白的，想要改改更是不可能的事了。

## Darknet 简介
[Darknet](https://pjreddie.com/darknet/) 是一个用 C 和 CUDA 编写的开源神经网络框架。它快速、易于安装，并支持 CPU 和 GPU 计算。源码在 [GitHub](<https://github.com/pjreddie/darknet>) 上。

> 先多了不说了，先搬点原网站的内容过来吧。
>

#### YOLO: Real-Time Object Detection
You only look once (YOLO) is a state-of-the-art, real-time object detection system.

#### ImageNet Classification
Classify images with popular models like ResNet and ResNeXt.

#### Nightmare
Use Darknet's black magic to conjure ghosts, ghouls, and wild badgermoles. But be warned, ye who enter here: no one is safe in the land of nightmares.

#### RNNs in Darknet
Recurrent neural networks are all the rage for time-series data and NLP. Learn how to use them in Darknet!

#### DarkGo: Go in Darknet
Play Go using a policy network trained with Darknet