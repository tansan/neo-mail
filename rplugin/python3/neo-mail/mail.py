import imaplib
import email
import time
from email.header import decode_header, make_header
from email.utils import parsedate


class MailClient(object):

    def __init__(self):
        self.server = 'imap-mail.outlook.com'
        self.user = 'hogehoge@hotmail.co.jp'
        self.passwd = 'xxxxxxxx'
        self.imc = self.connectImap()

    def connectImap(self):
        imc = imaplib.IMAP4_SSL(self.server)
        imc.login(self.user, self.passwd)
        return imc

    def getMailList(self):
        self.imc.select()
        _, data = self.imc.search(None, 'ALL')
        lines = []
        count = 0
        for num in data[0].split():
            if count > 1000:
                break
            try:
                _, data = self.imc.fetch(num, '(RFC822)')
                msg = email.message_from_bytes(data[0][1])
                dat = time.strftime('%Y/%m/%d', parsedate(str(make_header(decode_header(msg['Date'])))))
                frm = str(make_header(decode_header(msg['From'])))
                sbj = str(make_header(decode_header(msg['Subject'])))
                lines.append(dat + "\t" + sbj + "\t(From)" + frm)
            except:
                continue

            count += 1
        return lines
