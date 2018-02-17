import neovim

from mail_api import MailClient as mail


@neovim.plugin
class NeovimMail(object):

    def __init__(self, nvim):
        self.nvim = nvim

    def echo(self, message):
        self.nvim.command("echo '[NEO-MAIL] {}'".format(message))

    @neovim.command('NeoVimMailBoxList')
    def getMailBoxList(self):
        self.echo(mail.getMailBoxList())
