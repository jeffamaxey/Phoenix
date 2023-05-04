#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import wx.adv

phoenix = ("""\
A phoenix is a mythical bird with a colorful plumage and a tail of gold and scarlet
(or purple and blue, according to some sources). It has a 500 to 1,000 year life-cycle,
near the end of which it builds itself a nest of myrrh twigs that then ignites; both nest
and bird burn fiercely and are reduced to ashes, from which a new, young phoenix or phoenix
egg arises, reborn anew to live again. The new phoenix is destined to live as long as its old
self. """)

class SampleBanners(wx.Panel):
    def __init__(self, parent):
        # ... create the frame itself ...
        wx.Panel.__init__(self, parent)

        pnxBmp = wx.Bitmap('bitmaps/phoenix_top.png')
        bmpsz = pnxBmp.GetSize()

        # Create and initialize the banner.
        whitePanel = wx.Panel(self, -1, size=(-1, bmpsz[1]))
        whitePanel.SetBackgroundColour(wx.WHITE)

        # Create and initialize the 1st banner and define a bitmap.
        banner1 = wx.adv.BannerWindow(whitePanel, dir=wx.BOTTOM)
        banner1.SetBitmap(pnxBmp)

        whiteSizer = wx.BoxSizer(wx.HORIZONTAL)
        whiteSizer.Add(banner1, 1)
        whitePanel.SetSizer(whiteSizer)

        # Create and initialize the 2nd banner and define the gradient text.
        banner2 = wx.adv.BannerWindow(self, dir=wx.TOP)
        banner2.SetGradient(start='#FF8000', end='#FFFFFF')
        banner2.SetText("Phoenix", phoenix)

        # Layout
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(whitePanel, 0, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, 5)
        vsizer.Add(banner2, 1, wx.EXPAND | wx.BOTTOM | wx.LEFT | wx.RIGHT, 5)

        self.SetSizer(vsizer)



class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        banners = SampleBanners(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(banners, 0, wx.EXPAND)

        text = wx.StaticText(self, -1, overview)
        sizer.Add(text, 0, wx.EXPAND|wx.ALL, 15)

        self.SetSizer(sizer)




def runTest(frame, nb, log):
    return TestPanel(nb, log)


#---------------------------------------------------------------------------


overview = """\
This sample displays two banner windows, one with an image, and one with text and
a colour gradient background.

Banner windows can be used to present some overview of the current window contents
to the user in an aesthetically pleasant way. They are typically positioned along
the left or top edge of the window (although this class also supports right-aligned
and bottom-aligned banners) and show either a bitmap with a logo or a few lines of
text on a gradient-filled background.
"""


if __name__ == '__main__':
    import sys,os
    import run
    run.main(['', os.path.basename(sys.argv[0])] + sys.argv[1:])

