# fastDFS安装

https://github.com/jimpeter1997/fastdfs-nginx

## 初始状态
用scp上传文件

```bash
[root@localhost bakcup_fastDFS]# ll
total 2012
-rw-r--r--. 1 root root 913965 4月  29 15:51 fastdfs-master.zip
-rw-r--r--. 1 root root  22492 4月  29 15:51 fastdfs-nginx-module-master.zip
-rw-r--r--. 1 root root 308105 4月  29 15:51 libfastcommon-master.zip
-rw-r--r--. 1 root root 804164 4月  29 15:51 nginx-1.6.2.tar.gz
```

## 安装依赖
```bash
yum  install -y  libevent  #FastDFS依赖libevent库 libevent-2.0.21-4.el7.x86_64
yum -y install gcc
yum install -y pcre pcre-devel
yum install -y zlib zlib-devel
yum install -y openssl openssl-devel
# 没有make的需要安装一下make
yum install -y make

```

## 创建对应文件夹

```bash
#存放对应追踪器,存储节点,和日志数据
mkdir -p /fastDFS/fastdfs/tracker
mkdir -p /fastDFS/fastdfs/storage
mkdir -p /fastDFS/fastdfs/logs
```

## 安装依赖

```bash
cd /fastDFS/backup_fastDFS
unzip libfastcommon-master   # 解压到当前文件夹
cd libfastcommon-master
./make.sh
./make.sh install
```

## 安装fastdfs
```bash
unzip fastdfs-master.zip
cd fastdfs-master
./make.sh
./make.sh install
cd /fastDFS/bakcup_fastDFS/fastdfs-master/conf
cp * /etc/fdfs

# 配置启动tracker
#进入/etc/fdfs/文件夹
cd /etc/fdfs/
vim tracker.conf
#找到base_path修改如下
base_path = /fastDFS/fastdfs/tracker
#修改后启动tracker
fdfs_trackerd /etc/fdfs/tracker.conf start
#使用如下命令查看,出现tracker相关数据即可
ps -ef | grep fdfs

# 配置启动storage
#配置storage(即刚刚配置tracker的同级/etc/fdfs)
vim storage.conf
#修改
#日志目录(# the base path to store data and log files)
base_path=/fastdfs/storage
#存储目录( # store_path#, based on 0, to configure the store paths to store files)
store_path0=/fastdfs/storage  
#tracker节点,在这里配自己服务器的外网ip,只配置一个ip的话,另一个最好注释掉
tracker_server=192.168.1.4:22122
#启动storage
fdfs_storaged /etc/fdfs/storage.conf start
#同tracker的查看方式,使用命令看看是否有storage的服务
ps -ef | grep fdfs
```
