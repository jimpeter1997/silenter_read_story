### atom 我用的快捷键 ---尽快离开让人厌烦的鼠标

- 打开atom: terminal中直接输入: atom  或者 atom + 文件名/文件夹名
- cmd + 方向键 : 快速让atom到你想要位置
- F11 全屏
- 调出功能栏: alt
- 显示/隐藏目录: ctrl +  \
- 在目录和当前编辑文件之间切换:  alt + \
- 目录展开/关闭:
-- 回车(不会全部展开)
-- ctrl+alt+](全部展开)
-- ctrl+alt+[(全部关闭)
-- ctrl+](下级展开)
-- ctrl+[(闭合)
- 指定跳转到第几行 : ctrl + g


- ctrl + p : 快速打开某个文件
- ctrl + shift + p
- 分屏(有冲突需要自己设置)
    ```bash
    1. 打开ctrl + shift + p , 输入 keymap
    2. 在最下面输入下面内容:
    # 分屏的快捷键映射
    '.editor':
        # 'ctrl-f9':'pane:split-up'  # 我的ctrl＋f9是分屏到下方
        # 'ctrl-f10':'pane:split-down'
        'ctrl-1':'pane:split-left'
        'ctrl-2':'pane:split-right'
        'alt-1':'window:focus-pane-on-left'
        'alt-2':'window:focus-pane-on-right'
    ctrl+1: 左边分屏幕
    ctrl+2: 右边分屏幕
    alt+1: 光标移动到左屏幕
    alt+2: 光标移动到右屏幕   
    ```
- 关闭当前页面: ctrl + w
- 在标签页之间切换: ctrl + tab
- 关闭atom : ctrl + q
