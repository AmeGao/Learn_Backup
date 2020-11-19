
# -*- coding:utf8 -*-
import json
import socket
import threading

def service_client(new_socket, IP):# IP即为容器IP号
    while True:
        # 若大量数据传输过来，超过服务器处理速度，就会“失败”
        try:
            recv_data = new_socket.recv(1024).decode("utf-8")
            if(recv_data !=''):
                print('recv:' + recv_data)  
        except:
            print("fail")
            new_socket.close()
            return
    

def main():
    #  服务器基本功能

    # 创建套接字
    tcp_sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口
    tcp_sever_socket.bind(("", 8885))
    # 准备监听
    tcp_sever_socket.listen(64)

    while True:
        # 等待客户端链接
        print('wating for connecting...')
        new_socket, client_addr = tcp_sever_socket.accept()
        # 为客户端服务
        print('connected.')
        threading.Thread(target=service_client, args=[new_socket, client_addr[0]]).start()


if __name__ == "__main__":
    main()
