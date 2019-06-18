import ctypes
import datetime
import win32com.client as wincl
import time

speak = wincl.Dispatch("SAPI.SpVoice")
SPI_SETDESKWALLPAPER = 20
MessageBox = ctypes.windll.user32.MessageBoxW
day = datetime.datetime.today().weekday()
#day = 5  #set Static day(testing)

#print(day)

# Not all of these are used these are some options for formating msg boxes
MB_OK = 0x0
MB_OKCXL = 0x01
MB_YESNOCXL = 0x03
MB_YESNO = 0x04
MB_HELP = 0x4000
ICON_EXLAIM = 0x30
ICON_INFO = 0x40
ICON_STOP = 0x10


# Monday
if day == 0:
  ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,0, "Backgrounds/Monday.bmp" , 0)
  MessageBox(None, 'Tis pre-pre-Wednesday!', 'Lit Alert', MB_YESNO | ICON_INFO)

# Tuesday
elif day == 1:
  ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,0, "Backgrounds/Tuesday.bmp" , 0)
  MessageBox(None, 'Tis pre-Wednesday!', 'Lit Alert', MB_YESNO | ICON_INFO)

# Wednesday
elif day == 2:
  ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,0, "Backgrounds/Wednesday.bmp" , 0)
  MessageBox(None, 'AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH', 'IT IS WEDNESDAY MY DUDES!', MB_YESNO | ICON_EXLAIM)

# Thursday
elif day == 3:
  ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,0, "Backgrounds/Thursday.bmp" , 0)
  MessageBox(None, 'Tis the Pre-Pre-Weekend My Dudes!', 'Lit Alert', MB_YESNO | ICON_INFO)

# Friday
elif day == 4:
  ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,0, "Backgrounds/Friday.bmp" , 0)
  MessageBox(None, 'Tis the Pre-Weekend My Dudes!', 'Lit Alert', MB_YESNO | ICON_INFO)

# Saturday
elif day == 5:
  ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,0, "Backgrounds/Saturday.bmp" , 0)
  MessageBox(None, 'Tis the PRO-Day My Dude!', 'PRO Alert', MB_YESNO | ICON_INFO)

# Sunday
elif day == 6:
  ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,0, "Backgrounds/Sunday.bmp" , 0)
  MessageBox(None, 'God: Why are you at work on the lord\'s day?', 'Holy MSG', MB_YESNO | ICON_INFO)