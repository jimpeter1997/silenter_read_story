# makefile

## 常用符合总结

###  =   :=   ?=  +=  四者的区别
- =   是最基本的赋值
- :=  覆盖之前的赋值
- ?=  如果之前没有被赋值过,那就赋值等号后面的值
- +=  添加等号后面的值

### "@" 符号的使用
    通常makefile会将其执行的命令行在执行前输出到屏幕上
    如果将'@'添加到命令行前,这个命令将不会被make回显出来

### '-'  符号的使用
    通常删除,创建文件如果碰到文件不存在或者已经创建,
    那么希望忽略掉这个错误,继续执行,就可以在命令前添加'-'

    -rm  dir;
    -mkdir aaadir;

### '$'符号的使用
    主要扩展打开makefile中定义的变量

### '$$'符号的使用
    '$$' 主要扩展打开makefile中定义的shell变量

    for example:
    ```bash
    @for dir in $(subdirs);do\
    @echo -------compiling $$dir-----------; \

    $(MAKE) -C ; \

    done
    ```
    以上 subdirs 属于makefile中定义的变量, 使用$
    dir则属于makefile中定义的shell变量,使用$$
