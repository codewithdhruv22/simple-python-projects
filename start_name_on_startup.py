# PYWAKE_FRIEND
from win32com.client import Dispatch

# TTS
def speak(text):
    speak =Dispatch("SAPI.Spvoice")
    speak.Speak(text)

speak("Hi Dhruv Sir!")

# Watch Full Video Tutorial Of This Program On My Youtube Channel
# https://www.youtube.com/channel/UCmOBuijDvNgUMlqpzrwEBcw
