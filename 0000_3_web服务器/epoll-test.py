import socket
import re
import select


def service_client(new_socket, request):
    """根据路由去读取文件"""
    request_lines = request.splitlines()
    print(">"*30)
    print(request_lines)

    file_name = ""
    res = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if res:
        file_name = res.group(1)
        if file_name == "/":
            file_name = "/index.html"

    try:
        f = open("./html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND \r\n"
        response += "\r\n"
        response += "-----file not found-----"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        response_body = html_content
        response_header = "HTTP/1.1 200 OK \r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"
        response = response_header.encode("utf-8") + response_body
        new_socket.send(response)

def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server_socket.bind(("", 9090))
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)  # 将套接字变为非堵塞
    # 创建epoll对象
    epl = select.epoll()
    # 将监听套接字对应的fd注册到epoll中
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)
    # select.EPOLLIN:表示什么触发事件，select.EPOLLIN有输入的时候触发
    fd_event_dict = dict()
    while True:
        fd_event_list =  epl.poll()  # 默认会堵塞，直到os检测到数据到来，通过事件通知方式，告诉这个程序，程序才会继续执行
        # fd_event_list内容：[(fd,event),...]
        # fd : 套接字对应的文件描述符
        for fd, event in fd_event_list:
            if fd == tcp_server_socket.fileno():
                new_socket, client_addr = tcp_server_socket.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event ==  select.EPOLLIN :
                # 判断已经链接的客户端是否有数据过来
                recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
                if recv_data:
                    service_client(fd_event_dict[fd], recv_data)
                else:
                    # 为什么要在这个地方关闭？
                    # 因为请求结束，那么这里就没有数据了，也表示长链接结束了
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]
            else:
                # 这个已经不会使用到了
                print("重大意外！")
                pass


if __name__ == '__main__':
    main()
