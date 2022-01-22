---
created: 20220122023054853
title: Entry Conversion and Compatibility维基条目格式转换与兼容性
modified: 20220122124822132
tags:
    -meta
---
! 目标

* 尽量与[[Obsidian|Obsidian.md]]的markdown条目兼容。

! 兼容的实现方法

思路有二：

* 全部条目用markdown语法，依赖`Markdown插件`
* 格式转换

! 导出条目

由于 GitHub Pages 上只能使用单文件版本的 Tiddlywiki，转换前需要把`index.html`文件中的条目提取出来。

!! 网页导出
在此网页上选择`Tools>export all`可以把所有条目导出为`html`，`csv`，或`json`格式。

!! 文件搜索
直接匹配`'{"created":"[0-9]+".*"title":"[^\$]'`大致可以得到所有非隐藏条目。

! 转换方法

!! Markdown to Tiddlers

!! Tiddlers to Markdown

! 兼容策略

内链的语法相同。

为了方便不同语法的相互转换，应当尽量：

* 使用最简单的语法
* 少插入内嵌图表
** 可以用外链图表代替


! 参见
* [[davidalfonso|https://davidalfonso.es/posts/migrating-from-tiddlywiki-to-markdown-files]]