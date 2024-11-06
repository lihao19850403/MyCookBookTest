# MyCookBookTest

#### 介绍

本项目基于Hypium对《香辣菜谱》应用进行了UI测试。

运行前请先安装《香辣菜谱》应用到测试设备上。

《香辣菜谱》应用的项目地址是：[https://gitee.com/greatleghair/MyCookBook](https://gitee.com/greatleghair/MyCookBook)

#### 项目特点

本项目是基于DevEco Testing Hypium开发的测试工程，使用的主要语言是Python。

#### 安装教程

##### 开发环境配置

开发工具下载地址：[https://developer.huawei.com/consumer/cn/download/deveco-testing-hypium](https://developer.huawei.com/consumer/cn/download/deveco-testing-hypium)。

上述开发工具以插件的方式提供，您需要PyCharm来安装这些插件，PyCharm使用社区版即可，下载地址：[https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/)。

目前阶段Hypium插件限定Python3.10运行环境，因此您需要下载3.10版本的Python，官网只提供了3.10.11版本的安装包，下载地址：[https://www.python.org/downloads/release/python-31011/](https://www.python.org/downloads/release/python-31011/)。

以上就是所有的开发资料，接下来您需要：

- 安装Python3.10.11。
- 安装PyCharm。
- 下载Hypium开发工具解压备用。

Hypium开发工具解压后的目录结构为：

```text
devecotesting-hypium-5 文件夹
    ┣━━━ DevecoTesting-Hypium-5.0.7.200.zip Hypium插件，直接安装进Python，不需要解压
    ┣━━━ hypium-5.0.7.200 文件夹，需要将hypium-5.0.7.200.zip解压，之后要执行里面的install.sh
    ┗━━━ hypium_perf-5.0.7.200 文件夹，需要将hypium_perf-5.0.7.200.zip解压，之后要执行里面的install.sh
```

##### 获取代码

执行以下命令将工程代码下载到本地：

```text
git clone https://gitee.com/greatleghair/MyCookBookTest.git
```

并在PyCharm中打开。

在PyCharm中指定Python Interpreter，此处使用Python3.10。一般在屏幕右下角就可以切换。

或者新建一个Python Interpreter，使用刚才安装好的Python3.10，新建的时候需要勾选“继承全局站点软件包”。

在PyCharm中安装Hypium插件，使用本地安装的方式，安装DevecoTesting-Hypium-5.0.7.200.zip(不需要解压)。

在PyCharm中打开Terminal，依次执行hypium插件中的以下两个脚本：

```text
sh hypium-5.0.7.200/install.sh
sh hypium_perf-5.0.7.200/install.sh
```

到此开发环境已准备完毕。

##### 配置模拟器

在DevEco Studio中创建模拟器(应用适配了Phone、Foldable、Tablet三种设备，可以创建三个模拟器来查看运行效果)。

之后请在模拟器中安装《香辣菜谱》应用。

推荐使用带arm架构CPU的电脑运行本项目，x86架构CPU的电脑会有连接不上模拟器的问题。如果没有合适的模拟器，您也可以用真机进行测试。

##### 启动项目

启动刚才创建好的模拟器（上面要提前安装好应用），然后点击PyCharm右上方绿色的播放按钮，即可开始进行UI测试。

#### 使用说明

在项目的main.py文件中有一些启动命令，分别对应各种模块的测试，您可以单独运行一条命令，或者全部放开注释，运行所有模块的测试命令。

测试结束后，会在项目的reports文件夹中生成测试报告。测试报告以测试时间命名，按文件夹组织，您可以查看对应时间的测试报告，了解测试结果。

#### 更新日志

| 版本号   | 内容                                          |
|-------|---------------------------------------------|
| 1.0.0 | 初版                                          |
| 1.1.0 | 改进代码，去除冗余id属性设置，解耦测试代码与产品代码，并适配折叠屏与Pad屏幕的测试 |