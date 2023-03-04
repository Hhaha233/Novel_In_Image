# Novel_In_Image

## 1.功能介绍

这是一个可以让文字和图片互相转换的便利工具。它可以用来隐藏小说之类的文本内容。

原理及视频教程：
https://www.bilibili.com/video/BV1Ai4y1V7rg/

## 2.用法

### 文字转图片

```python
python nii.py -e xxx.txt
```

其中`xxx.txt`是要转换的文本路径。(记得把文本转化为utf-8编码)

### 图片转文字

```python
python nii.py -d xxx.bmp
```

其中`xxx.bmp`是要转换的图片路径。

### 输入/输出

输入和输出的文件对应放在"Input"/"Output"文件夹中

### 简单模式

有的时候不想打开cmd
不使用命令行也可以直接启动，按照说明操作就行

## 4.注意事项

在开始使用之前，请确保您的设备已经安装了Python 3.6或更新版本，和`pillow`库。
