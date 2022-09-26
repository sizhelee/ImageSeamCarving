# ImageSeamCarving

 Course Project for Introduction to Computation

 Proposed by TA Sizhe Li

## 1. 引言

生活中我们时常遇到需要调整图片比例的场景，例如将横板图片调整为竖版。两种常用的方法分别为直接进行裁剪，以及进行图片的拉伸。但在实际应用中，前者往往会丢失图片中的部分内容，而后者则容易使得图像失真。

在本次项目中，你将复现一个经典的图像“接缝剪裁”（Seam Carving）算法。Seam Carving算法是由以色列的两位教授Shai Avidan和Ariel Shamir于2007年提出，算法本身基于动态规划处理图像，实现了在随意改变图像比例的同时，保证图像中重要部分大小不变。简单来说，图片缩放后仍然能够维持整体的完整性。

![teaser](teaser.png)

如上图所示，左侧为原始图片，算法的目标为更改图片的比例至横板，右侧上半部分展示了直接拉伸和剪裁之后的效果图，右下图为采用Seam Carving算法处理后的效果图。在内容完整性和真实性方面，Seam Carving算法明显优于前述两种方法。

## 2. 算法
