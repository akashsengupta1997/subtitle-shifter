import wx


HEIGHT = 600
WIDTH = 200


class Gui(wx.Frame):
    def __init__(self, title):
        super().__init__(parent=None, title=title, size=(HEIGHT, WIDTH))

        self.panel = wx.Panel(self)

        # Initialise box to store shift widgets
        shiftBox = wx.StaticBox(self.panel, wx.ID_ANY, "Shift Settings")

        # Initialise widgets
        self.textConsole = wx.TextCtrl(self.panel, wx.ID_ANY,
                                       size=(WIDTH * 0.2, HEIGHT * 0.4),
                                       style=wx.TE_READONLY | wx.TE_MULTILINE,
                                       value='Subtitle Shifter')

        self.filePicker = wx.FilePickerCtrl(self.panel, wx.ID_ANY,
                                            message='Select .srt File')
        self.shiftMagnitudeSpin = wx.SpinCtrl(self.panel, wx.ID_ANY,
                                              max=99999999999)
        self.shiftedFileNameText = wx.TextCtrl(self.panel, wx.ID_ANY,
                                               size=(100,10), value='resync')

        self.shiftButton = wx.Button(self.panel, wx.ID_ANY, label='Shift')

        # Bind shift button to handler
        self.shiftButton.Bind(wx.EVT_BUTTON, self.on_shift_button)

        # Initialise sizers
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.filePickSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.shiftSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.shiftSettingsSizer = wx.StaticBoxSizer(shiftBox, wx.VERTICAL)

        # Add widgets to sizers
        self.mainSizer.Add(self.filePickSizer, 1, wx.EXPAND)
        self.mainSizer.Add(self.shiftSizer, 1, wx.EXPAND)

        self.filePickSizer.Add(self.filePicker, 1, wx.EXPAND | wx.ALL, 3)
        self.shiftSizer.Add(self.shiftSettingsSizer, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL,
                            10)
        self.shiftSizer.Add(self.shiftButton, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 30)
        self.shiftSizer.Add(self.textConsole, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.shiftSettingsSizer.Add(self.shiftMagnitudeSpin, 1, wx.ALIGN_LEFT | wx.ALL,
                                    10)
        self.shiftSettingsSizer.Add(self.shiftedFileNameText, 1, wx.ALIGN_LEFT | wx.ALL,
                                    10)

        self.panel.SetSizer(self.mainSizer)
        self.SetSizeHints((HEIGHT, WIDTH))  # Set minimum frame size
        self.Centre()

    def on_shift_button(self, e):
        pass