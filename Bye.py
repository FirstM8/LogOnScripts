import ctypes
import win32com.client as wincl
import random

speak = wincl.Dispatch("SAPI.SpVoice")

opt = [
       "Why are you running?",
       "NO...don't leave me.",
       "You'll be back... right?",
       "I cant believe you done this",
       "How could this happen to meeeeeee"
      ]

speak.Speak(random.choice(opt))