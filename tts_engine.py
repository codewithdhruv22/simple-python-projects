from win32com.client import Dispatch

def audiobook(text):
    audiobook = Dispatch("SAPI.Spvoice")
    audiobook.Speak(text)
    
audiobook("This is a book text")
