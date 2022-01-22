---
created: 20220122023054853
title: Entry Conversion and Compatibility维基条目格式转换与兼容性
modified: 20220122140217995
type: text/x-markdown
tags:
    -meta
---
# 目标

- 尽量与[[Obsidian|Obsidian.md]]的markdown条目兼容。

# 兼容的实现方法

思路有二：

- 全部条目用markdown语法，依赖[[Markdown插件|https://tiddlywiki.com/plugins/tiddlywiki/markdown/index.html]]；
- Tiddly WikiText 语法，再通过导出html，最终由pandoc转换成markdown。

由于复杂图表用处有限，应该用主要Markdown格式来写条目，少用Tiddly原生格式。然后可以直接在 Tiddly Markdown 和 Obsidian Markdown 之间转换。

# 导出条目

由于 GitHub Pages 上只能使用单文件版本的 Tiddlywiki，转换前需要把`index.html`文件中的条目提取出来。

## 网页导出
在此网页上选择`Tools>export all`可以把所有条目导出为`html`，`csv`，或`json`格式。

## 文件搜索
直接匹配`'{"created":"[0-9]+".*"title":"[^\$]'`大致可以得到所有非隐藏条目。

# 转换方法

- [ ] Markdown to Tiddlers: 用这则[[lua脚本|https://github.com/jeffrey4l/pandoc-addons/blob/master/md2tid.lua]]。

- [ ] Tiddlers to Markdown: 先导出，再转换。参考[[davidalfonso|https://davidalfonso.es/posts/migrating-from-tiddlywiki-to-markdown-files]]。

- [x] Between Markdown Formats: 根据[[Markdown插件|https://tiddlywiki.com/plugins/tiddlywiki/markdown/index.html]]网站上的介绍转换。


## Tiddly Markdown 与普通 Markdown 格式的对比

|                 |                       Tiddly Markdown                        |                  （Obsidian） Markdown                  |
| :-------------: | :----------------------------------------------------------: | :-----------------------------------------------------: |
|    WikiLinks    |                `[link text](#Test%20Tiddler)`                |              `[[link text｜Test Tiddler]]`               |
|       URL       |           `[Wikipedia](https://en.wikipedia.org)`            |                     （相同/不转换）                     |
|     Images      | `![Don't Panic](/home/stormy/tmp/wiki/docs/img/dont_panic.jpg "Title")` |                     （相同/不转换）                     |
| Embedded Images |         `![Purple Hills](purple_hills.jpeg "Title")`         |                需要嵌入图片的base64文本                 |
|     RefCite     |                  `<<ref agamben1995idea>>`                   |                   `[an example][id]`                    |
|     RefList     |              `<<showrefs title:"References">>`               |   `[id]: http://example.com/  "Optional Title Here"`    |
|    Footnote     |            `<<fnote "This is a small footnote">>`            |                        `[^fn1] `                        |
|  Footnote List  |              `<<showfnotes title:"Footnotes">>`              | `[^fn1]: Here is the *text* of the first **footnote**.` |

# 兼容策略

内链的语法相同。

为了方便不同语法的相互转换，应当尽量：

- 使用最简单的语法
- 少插入内嵌图表
  - 可以用外链图表代替


# 参见
- [[Markdown插件|https://tiddlywiki.com/plugins/tiddlywiki/markdown/index.html]]
- [[davidalfonso: tiddlers html to md by pandoc|https://davidalfonso.es/posts/migrating-from-tiddlywiki-to-markdown-files]]