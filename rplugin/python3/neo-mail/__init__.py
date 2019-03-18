import neovim

from .mail import MailClient


@neovim.plugin
class NeovimMail:

    def __init__(self, nvim):
        self.nvim = nvim
        self.mail = MailClient()

    def output(self, message):
        self.nvim.command('setlocal splitright')
        self.nvim.command('vnew')
        self.nvim.command('setlocal buftype=nofile bufhidden=hide nolist nonumber modifiable nowrap')
        self.nvim.current.buffer.append(message)
        self.nvim.command('setlocal nomodifiable')

    @neovim.command('NeoVimMailList')
    def outputMailList(self):
        self.output(self.mail.getMailList())
