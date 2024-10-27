# MyCookBookTest

#### 介绍

本项目基于Hypium对《香辣菜谱》应用进行了UI测试。

运行前请先安装《香辣菜谱》应用到测试设备上。

#### 项目特点

// TODO

#### 安装教程

##### 开发环境配置

开发工具下载地址：[https://developer.huawei.com/consumer/cn/download/deveco-testing-hypium](https://developer.huawei.com/consumer/cn/download/deveco-testing-hypium)。

上述开发工具以插件的方式提供，您需要PyCharm来安装这些插件，PyCharm使用社区版即可，下载地址：[https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/)。

目前阶段Hypium插件限定Python3.10运行环境，因此您需要下载3.10版本的Python，官网只提供了3.10.11版本的安装包，下载地址：[https://www.python.org/downloads/release/python-31011/](https://www.python.org/downloads/release/python-31011/)。

安装Python3.10.11，安装PyCharm，下载Hypium开发工具解压备用。

##### 获取代码

执行以下命令将工程代码下载到本地：

```text
git clone https://gitee.com/greatleghair/MyCookBookTest.git
```

并在PyCharm中打开。

在PyCharm中指定Python Interpreter，此处使用Python3.10。一般在屏幕右下角就可以切换。

在PyCharm中安装Deveco Testing Hypium插件，使用本地安装的方式，安装DevecoTesting-Hypium-5.0.7.200.zip(不需要解压)。

在PyCharm中打开Terminal，依次执行hypium插件中的以下两个脚本：

```text
sh hypium-5.0.7.200/install.sh
sh hypium_perf-5.0.7.200/install.sh
```

##### 配置模拟器

在DevEco Studio中创建模拟器(应用适配了Phone、Foldable、Tablet三种设备，可以创建三个模拟器来查看运行效果)。

##### 启动项目

启动刚才创建好的模拟器，然后点击PyCharm右上方绿色的播放按钮，即可开始进行UI测试。

#### 使用说明

// TODO

#### 更新日志

| 版本号    | 内容 |
|--------|----|
| 1.0.0  | 初版 |