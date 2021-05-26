### shadowsocks

## 服务器
```bash
python3 --version
# 确定python版本
pip3 --version
# 确定pip的版本
# 两者都要为3的版本
pip3 install https://github.com/shadowsocks/shadowsocks/archive/master.zip
sserver --version
# 输出带有3.0.0，则正确
cd /home
vim sssconfig.json
# 输入以下内容
‘’‘
{
    "server":"你服务器的IP或者0.0.0.0",
    "server_port":你想要的端口号,
    "local_address":"127.0.0.1",
    "local_port": 1080,
    "password":"足够复杂的密码",
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open":false,
    "workers":1
}

"server":"0.0.0.0",
"server_port":8181,
"local_address":"127.0.0.1",
"local_port": 1080,
"password":"qwe123",
"timeout":300,
"method":"aes-256-cfb",
"fast_open":false,
"workers":1

’‘’
多端口配置

‘’‘
{
 	"server":"my_server_ip",  #填入你的IP地址
	"local_address": "127.0.0.1",
	"local_port":1080,
	"port_password": {
  	    "8381": "foobar1",    #端口号，密码
  	    "8382": "foobar2",
   		"8383": "foobar3",
    	"8384": "foobar4"
	},
 	"timeout":300,
	"method":"aes-256-cfb",
 	"fast_open": false
}
’‘’
ssserver -c /home/sssconfig.json
# 测试一下是否能正常启动
ssserver -c /home/sssconfig.json -d start
# 在后台以守护进程方式启动
```


## 本地电脑
```bash
https://github.com/shadowsocks/shadowsocks-windows/releases
# windows客户端地址
https://github.com/shadowsocks/shadowsocks-qt5/releases
# linux客户端地址
https://www.shadowsocks.org/en/index.html
# 安卓客户端地址，这个地址不翻墙是打不开的
苹果手机可以直接在商城中找到shadowsocks

对于ubuntu： 在相应的页面上下载，后缀为AppImage的文件
直接双击即可，如果提示错误，那么修改文件的权限，让他成为可执行的文件（选中右键也可以修改权限）

在电脑中找到shadowsocks，双击打开
输入你服务器的IP，你设置的端口号，密码，加密方式，即可。


最后一步！！！

在电脑设置中开启全局代理

setting ---> Network ---> Manual

2020.3.28 以上内容均可使用


下面是开机自动运行（可选）： 未测试

vim /lib/systemd/system/shadowsocks.service
# 输入一下内容
‘’‘
[Unit]
Description=Shadowsocks Server
After=network.target

[Service]
ExecStart=/usr/local/bin/ssserver -c /etc/shadowsocks.json
Restart=on-abort

[Install]
WantedBy=multi-user.target
’‘’

systemctl start shadowsocks.service
systemctl enable shadowsocks.service
systemctl status shadowsocks.service




```
