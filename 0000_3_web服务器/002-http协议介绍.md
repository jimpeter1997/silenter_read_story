### http协议： 超文本传输协议，基于tcp协议

浏览器向服务器发送的请求格式：
```
GET / HTTP/1.1
Host: IP
Connection: keep-alive(长链接)
Accept:
Upgrade-Insecure-Requests:
User-Agent:(浏览器版本)
Accept-Encoding: gzip (压缩格式)
Accept-Language: zh-CN（接受的语言）
```
服务器向浏览器发送的返回格式：

```
HTTP/1.1 200 OK  # header

# 一个换行来区分header和body
<h1>hahaha</h1>  # body
```


### web静态服务器-显示固定的页面

```python
import socket


def service_client(new_socket):
    """为这个客户端返回数据""""
    # 1. 接受浏览器发送过来的请求，即http请求
    # GET / HTTP/1.1
    # ...
    request = new_socket.recv(1024)
    # 2. 返回http格式的数据，返回给浏览器
    # 2.1 准备：header
    response = "HTTP/1.1 200 OK \r\n"
    response += "\r\n"
    # 2.2 准备body
    response += "<h1>hahahah</h1>"
    new_socket.send(response.encode("utf-8"))

    # 3. 关闭套接字
    new_socket.close()


def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket,AF_INET, socket.SOCK_STREAM)
    # 先关闭服务器的情况下，由于四次挥手需要等待网络延迟的最长时间的两倍（一般为2-5分钟）：2msl
    # 所以先关闭服务器，会出现第二次启动的时候，报错：端口被占用
    # 添加下面这行代码以后就可以解决这个问题
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2. 绑定
    tcp_server_socket.bind(("", 7890))
    # 3. 变为监听套接字
    tcp_server_socket.listen(128)
    while True:
        # 4. 等待新客户端的链接
        new_socket, client_addr = tcp_server_socket.accept()
        # 5. 为这个客户端服务
        service_client(new_socket)
    # 6. 关闭
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
```


### web静态服务器-显示需要的

根据用户的请求，返回指定的页面

```python
import socket
import re


def service_client(new_socket):
    """为这个客户端返回数据""""
    # 1. 接受浏览器发送过来的请求，即http请求
    # GET / HTTP/1.1
    # ...
    request = new_socket.recv(1024).decode("utf-8")
    print(">>>"*10)
    print(request)
    request_lines = request.splitlines()
    print("")
    print("****"*10)
    print(request_lines)
    # request_lines[0] = "GET /index.html HTTP/1.1"
    res = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    file_name = ""
    if res:
        file_name = ret.group(1)
        print("file_name = ", file_name)
        if file_name == "/":
            file_name = "/index.html"

    try:
        f = open("./html"+file_name, "rb")
    except:
        response = "HTTP/1.1 200 OK \r\n"
        response += "\r\n"
        # 将header发送
        response += "--- file not found ---"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        # 2. 返回http格式的数据，返回给浏览器
        # 2.1 准备：header
        response = "HTTP/1.1 200 OK \r\n"
        response += "\r\n"
        # 将header发送
        new_socket.send(response.encode("utf-8"))
        # 将body发送
        new_socket.send(html_content)



    # 3. 关闭套接字
    new_socket.close()


def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket,AF_INET, socket.SOCK_STREAM)
    # 先关闭服务器的情况下，由于四次挥手需要等待网络延迟的最长时间的两倍（一般为2-5分钟）：2msl
    # 所以先关闭服务器，会出现第二次启动的时候，报错：端口被占用
    # 添加下面这行代码以后就可以解决这个问题
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2. 绑定
    tcp_server_socket.bind(("", 7890))
    # 3. 变为监听套接字
    tcp_server_socket.listen(128)
    while True:
        # 4. 等待新客户端的链接
        new_socket, client_addr = tcp_server_socket.accept()
        # 5. 为这个客户端服务
        service_client(new_socket)
    # 6. 关闭
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
```
### web静态服务器-多进程


### web静态服务器-多线程


### web静态服务器-并发服务器
