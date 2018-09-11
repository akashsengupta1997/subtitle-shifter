import wx
from srt_shifter import SrtShifter


HEIGHT = 600
WIDTH = 200


class Gui(wx.Frame):
    def __init__(self, title):
        super().__init__(parent=None, title=title, size=(HEIGHT, WIDTH))

        self.srt_shifter = SrtShifter()

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
        self.shiftMagnitudeValue = wx.TextCtrl(self.panel, wx.ID_ANY, size=(120, 23),
                                               value='Shift amount')
        self.shiftedFileNameText = wx.TextCtrl(self.panel, wx.ID_ANY, size=(120, 23),
                                               value='Shifted file name')

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
        self.shiftSizer.Add(self.textConsole, 3, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.shiftSettingsSizer.Add(self.shiftMagnitudeValue, 1,
                                    wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        self.shiftSettingsSizer.Add(self.shiftedFileNameText, 1,
                                    wx.ALIGN_CENTRE_HORIZONTAL | wx.ALL, 5)

        self.panel.SetSizer(self.mainSizer)
        self.SetSizeHints((HEIGHT, WIDTH))  # Set minimum frame size
        self.Centre()

    def on_shift_button(self, e):
        srt_file_path = self.filePicker.GetPath()
        new_file_name = self.shiftedFileNameText.GetValue()
        shift = float(self.shiftMagnitudeValue.GetValue())
        print(type(shift))
        message = self.srt_shifter.shift_srt_file(srt_file_path, new_file_name, shift)
        self.textConsole.SetValue(message)
