# libedit<a name="ZH-CN_TOPIC_0000001106844024"></a>

- [简介](#section11660541593)
- [目录结构](#section367519246426)
- [编译构建](#section137768191623)
- [许可证](#section126611612164217)

## 简介<a name="section11660541593"></a>

libedit是一个提供通用行编辑、历史和分词功能的命令行编辑库，类似于Readline。它是NetBSD Editline库的一个自动化工具和libtool化的移植版本，它的主要接口和功能包括
- readine(): 从标准输入读取一行，并返回一个指向动态分配缓冲区的指针，该缓冲区包含输入行。
- parse_and_bind(): 执行给定字符串中初始化命令，可以用来设置键绑定和其他选项。
- read_init_file(): 执行一个readline初始化文件，可以用来自定义readline的行为。
- get_line_buffer()： 返回当前行缓冲区的内容。
- insert_text(): 在光标位置插入文本到行缓冲区。
- redisplay(): 更新屏幕上显示的内容，以反映行缓冲区的当前内容。

在Openharonmy引入后，在lldb构建中开启编译可选依赖选项LLDB_ENABLE_LIBEDIT，lldb.so会依赖libedit编译生成的动态库libedit.so，支持lldb调试器在命令行调试时使用libedit库支持自动补齐和gui功能。
## 目录结构<a name="section367519246426"></a>
```
- COPYING                       版权文件
- OAT.xml                       OAT.xml过滤配置文件
- README.OpenSource             项目README.OpenSource文件
- README.md                     英文说明
- README_zh.md                  中文说明
- libedit-20210910-3.1.tar.gz   libedit源码压缩tar包
- libedit.spec                  上游更新记录说明
- libedit.yaml                  yaml文件
```
## 编译与安装<a name="section137768191623"></a>

```
- ./configure：用于配置软件的脚本，会根据系统环境检测和设置一些变量，生成对应的Makefile和一些头文件。其中运行configure脚本的时候指定一些参数来改变配置选项，如--prefix指定安装目录，--libdir指定库文件目录，--bindir指定可执行文件目录。
- make: 用于安装libedit软件，根据Makefile中的规则执行一系列的操作，编译源代码，运行测试，检查外部依赖等。
- make install: 将编译好的libedit.so文件安装到配置时指定的目录中。
```
## libedit使用文档
官方文档  https://www.thrysoee.dk/editline/


## 许可证<a name="section126611612164217"></a>

本项目遵从BSD-3-Clause许可证。
