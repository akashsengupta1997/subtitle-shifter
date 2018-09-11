import wx
from gui import Gui


def main():
    app = wx.App()
    gui = Gui('Subtitle Shifter')
    gui.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()
