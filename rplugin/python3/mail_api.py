import imaplib


class MailClient(object):

    def __init__(self):
        self.server = ''
        self.user = ''
        self.passwd = ''
        connectImap()

    def connectImap(self):
        imc = imaplib.IMAP4_SSL(self.server)
        imc.login(self.user, self.passwd)

    def getMailboxList(self):
        return imc.list()
