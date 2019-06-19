import ctypes
import win32com.client as wincl
import random
import datetime
import time

time.sleep(1)  # Waits for the network drives to connect

weekDay = datetime.datetime.today().weekday()
#weekDay = 2 # set Static weekDay(Testing)
#day = 20  # set Static day (Testing)

speak = wincl.Dispatch("SAPI.SpVoice")

# TTS Options for Random Selection
opt = ["Welcome, to the Help Delp!",
       "This is a bunch of Bologna",
       "Can I get Solidworks on me?",
       "Help, I've been migrated!",
       "Remember to sign in with username@umsystem.edu",
       "Hello there!"
       ]

# Wednesday My dudes
if weekDay == 2:
  speak.Speak("IT IS WEDNESDAY MY DUDES!")
  speak.Speak("AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")

else:
  speak.Speak(random.choice(opt))
  #speak.Speak("ITS A 1.1L SINGLE CAM NON HECKING V-TECH BUT HECKING WOOOOOOOOO o o o ")