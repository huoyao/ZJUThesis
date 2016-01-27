# ZJUThesis
Master thesis template of college of Computer Science, Zhejiang University, can easily be extended to the doctoral thesis and engineering papers

-----

本模板适用于计算机学院硕士论文。当然，应该也可以轻易的推广到博士论文和其他工科类专业的论文

# 适用平台与环境
本模板基于`XeTeX+xeCJK+ctex`，在`Windows 7`, `Linux Mint 13（Ubuntu）`以及`OS X Mountain Lion`上测试通过，建议在`Windows`下使用`CTeX`套装，其他平台使用`TeXLive 2012`，不过需要对`ctex-xecjk-winfonts.def`这个文件作一些修改（Linux和OS X下还需要安装Windows下的一些对应字体，比如SimSun等），本文件夹下有对应的改好的文件。

- `CTeX`发行版这个文件在`%CTEXDIR%/MiKTeX/tex/latex/ctex/fontset`下 
   其中`%CTEXDIR%`是`CTeX`的安装目录。**`CTex`安装前请备份好系统环境变量`path`路径。**
- `TeXLive`下这个文件在这里：
	`/usr/local/texlive/2012/texmf-dist/tex/latex/ctex/fontset/`（linux和OS X）下，
   Windows下的类似于这个目录
- 建议使用TexLive

# 如何使用
## 编译示例文件
- Windows下：`thesis.bat`
- Linux和OS X下： `sh thesis.sh`

## 或者
```bash
make  # 编译tex文件生成pdf
make clean # 删除中间文件
```

## 使用指南
- 模板内常用的一些排版用法可以在`Sample Document.pdf`中找到，建议参考一些`LaTeX`的教程。
- 编辑器可以使用`TeXStudio`
- 如果在`TexStudio`软件中编译不正常，建议通过运行`thesis.bat`脚本编译，待生成对应的辅助文件后将可以使用`TexStudio`编译

# A Bit More
> 感谢[ThuThesis](https://github.com/xueruini/thuthesis/  "ThuThesis")、[zjuthesis](http://code.google.com/p/zjuthesistex/  "zjuthesis")以及[eclipselu](https://github.com/eclipselu/zjuthesis-mphil)，本模板是在他们模板基础上调整的，加入了一些新的宏包，对于一些在论文格式审查过程中出现的问题进行了相应的修改。

# 主要更新
- 图表目录中章节与章节之间无空行
- `itemize`与`enumerate`的使用时，去掉每个item之间多余的空行，去掉item与前后文之间的空行
- 参考文献中对会议论文的引用格式修改，都采用统一的冒号后接页码的格式
- 摘要页码用小写罗马字体，目录页码采用大写罗马字体
- 图标目录中序号与标题之间的大小固定不变，不会因为序号数位的增多而缩小
- 英文字体采用罗马字体，而非宋体
- 增加了开题报告的模板`thesis-proposal.tex`，开题报告的封面在`CoverPage`的文件夹下有`word`版本
- 增加了中英文字数统计的`python`代码文件：`texCount.py`，该文件在[Vespa314](https://github.com/Vespa314/ZJUthesis)的基础上进行了修改，采用`python3.0`编译运行

# 一些遗憾
> 没有完成论文的中英文封面的生成，在`CoverPage`的文件夹下有中英文封面的`word`版本。可以根据需要生成`pdf`后利用`acrobat`软件插入到最终的`pdf`论文中即可。

