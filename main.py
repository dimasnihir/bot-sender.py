import Window
import SenderService

if "__main__" == __name__:
    Window.root.mainloop()
    Sender = SenderService.SenderService('lali_pap30@ukr.net', 'Masya1')
    Sender.login()

