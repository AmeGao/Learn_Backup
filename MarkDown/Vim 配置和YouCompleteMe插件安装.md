# Vim 配置和YouCompleteMe插件安装

## 一、Vim安装和配置

### 简介

Vim是从 [vi](https://baike.baidu.com/item/vi/5043202) 发展出来的一个文本编辑器。代码补全、编译及错误跳转等方便编程的功能特别丰富，在程序员中被广泛使用，和Emacs并列成为类Unix系统用户最喜欢的文本编辑器。

vim的设计理念是命令的组合。用户学习了各种各样的文本间移动/跳转的命令和其他的普通模式的编辑命令，并且能够灵活组合使用的话，能够比那些没有模式的编辑器更加高效的进行文本编辑。同时vim与很多快捷键设置和[正则表达式](https://baike.baidu.com/item/正则表达式)类似,可以辅助记忆。并且vim针对程序员做了优化。[来源百度百科](https://baike.baidu.com/item/VIM/60410?fr=aladdin)

### 安装 vim

安装环境VMware上新安装的Ubuntu18.04的系统。

首先，在shell中输入

```shell
sudo apt install vim  
```
安装完成之后，输入 vim --version，可以看到vim的一系列信息，如下图：

![image-20200417122213171](Vim 配置和YouCompleteMe插件安装/Vim_Version.png)

出现这些信息即安装成功。

### Vim配置

Vim编辑器相关的所有功能开关都可以通过.**vimrc**文件进行设置。

上图中最下面的几行是vim读取配置文件的顺序，首先是安装目录内的vimrc文件，其次是用户主目录中的. vimrc 文件。安装目录内的vimrc文件是Vim编辑器的全局配置，对所有的用户都生效，而用户主界面的.vimrc文件是用户个人的配置，仅对该用户生效。这次配置vim就是配置单个用户的.vimrc文件。

![image-20200417131206369](Vim 配置和YouCompleteMe插件安装/Config_Order.png)

Vim的可选配置有很多，这次的配置信息主要来自 [Vim中文社区](https://github.com/wsdjeg/vim-galore-zh_cn/blob/master/contents/minimal-vimrc.vim)中一份精简的vimrc，加了一点个人习惯的行号和换行。

```shell
set nocompatible

filetype plugin indent on  " Load plugins according to detected filetype.
syntax on                  " Enable syntax highlighting.

set autoindent             " Indent according to previous line.
set expandtab              " Use spaces instead of tabs.
set softtabstop =4         " Tab key indents by 4 spaces.
set shiftwidth  =4         " >> indents by 4 spaces.
set shiftround             " >> indents to next multiple of 'shiftwidth'.

set number
set cursorline
set linebreak
set wrapmargin =2
set backspace   =indent,eol,start  " Make backspace work as you would expect.
set hidden                 " Switch between buffers without having to save first.
set laststatus  =2         " Always show statusline.
set display     =lastline  " Show as much as possible of the last line.

set showmatch
set showmode               " Show current mode in command-line.
set showcmd                " Show already typed keys when more are expected.

set incsearch              " Highlight while searching with / or ?.
set hlsearch               " Keep matches highlighted.

set ttyfast                " Faster redrawing.
set lazyredraw             " Only redraw when necessary.

set splitbelow             " Open new windows below the current window.
set splitright             " Open new windows right of the current window.

set cursorline             " Find the current line quickly.
set wrapscan               " Searches wrap around end-of-file.
set report      =0         " Always report changed lines.
set synmaxcol   =200       " Only highlight the first 200 columns.

set list                   " Show non-printable characters.
if has('multi_byte') && &encoding ==# 'utf-8'
  let &listchars = 'tab:▸ ,extends:❯,precedes:❮,nbsp:±'
else
  let &listchars = 'tab:> ,extends:>,precedes:<,nbsp:.'
endif

" The fish shell is not very compatible to other shells and unexpectedly
" breaks things that use 'shell'.
if &shell =~# 'fish$'
  set shell=/bin/bash
endif

" Put all temporary files under the same directory.
" https://github.com/mhinz/vim-galore#handling-backup-swap-undo-and-viminfo-files
set backup
set backupdir   =$HOME/.vim/files/backup/
set backupext   =-vimbackup
set backupskip  =
set directory   =$HOME/.vim/files/swap//
set updatecount =100
set undofile
set undodir     =$HOME/.vim/files/undo/
set viminfo     ='100,n$HOME/.vim/files/info/viminfo
```

保存.vimrc文件，下次Vim启动时就会生效。

## 二、安装YouCompleteMe插件([参考文章](https://blog.csdn.net/shenlong1356/article/details/91379311?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2))

### 检查用户文件夹

在shell中执行以下命令用于创建文件夹

```shell
mkdir ~/.vim
mkdir ~/.vim/plugged
mkdir ~/.vim/plugin
mkdir ~/.vim/syntax
mkdir ~/.vim/doc
```

plugged 文件夹用于存放从vim-plug官方下载的插件

plugin可以存放网上下载的插件，然后把插件放在里面就可以了

syntax放有关文本语法相关的插件

doc存放说明文档

### 安装插件管理器vim-plug

vim-plug([官网](https://github.com/junegunn/vim-plug))是一个管理插件的插件,他的安装使用非常容易。在shell中输入以下命令：

```shell
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

以上命令成功的前提是安装了curl，若提示未安装，shell中运行：

```shell
sudo apt install curl
```

### 安装插件

使用vim-plug安装插件，需要在Vim的配置文件，即前面配置的.vimrc中声明它们。声明插件的格式如下：

```shell
call plug#begin(PLUGIN_DIRECTORY)
Plug 'name.vim'
"其他插件
call plug#end()
```

这次要安装的是YouCompleteMe插件所以在我的.vimrc文件开头加上

```shell
call plug#begin('~/.vim/plugged')
Plug 'Valloric/YouCompleteMe'
call plug#end()
```

保存后，重新加载 vim

```shell
在shell中输入
vim
然后在vim中输入命令
:PlugStatus
```

可以看到在插件管理界面已有YouCompleteMe插件，但是并未安装。所以接着执行 

```shell
:PlugIstall
```

插件就开始安装。由于这个插件极难安装，中间会出不少错误。并且由于这个系统是新系统，很多需要的配置都没有达到，所以我汇总了一下我遇到的问题：

#### 1. The ycmd server SHUT DOWN

```shell
"解决方法：
cd ~/.vim/plugged/YouCompleteMe 
./install.py
```

#### 2. CMake is required to build ycmd

```shell
"解决方法：
sudo apt install cmake
```

#### 3. Python headers are missing in /usr/include/python3.6m.

```shell
"解决方法：
sudo apt install python3.6-dev
"如果python后的版本号不同，修改版本号运行，如 
sudo apt install python2.7-dev
```

#### 4. No CMAKE_CXX_COMPILER could be found.

```shell
"解决方法：
sudo apt install g++
```

**注意事项 ：**每安装完一个包都应该尝试一下 ~/.vim/plugged/YouCompleteMe 目录下运行 install.py文件。如上即可解决一部分问题。

**参考文档：**https://www.cnblogs.com/zhyantao/p/10424884.html

## 三、运行效果

![image-20200417140958091](Vim 配置和YouCompleteMe插件安装/Run_Example.png)