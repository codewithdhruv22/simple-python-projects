#pip install googletrans==4.0.0-rc1
#convert languages from one to another using google translate and python

from googletrans import Translator, LANGUAGES
from googletrans.models import Translated

lang = list(LANGUAGES.values())
print("Welcome to Py_Guy Translate")
input_text = input("Please Enter Your Text in english:\n")
out_lang = input("Please enter output language name (ex.-hindi,gujarati,japanese:\n ").lower()
if out_lang not in lang:
    print("Sorry This Language is not available to translate")
else:
    translator = Translator()
    translated = translator.translate(text=input_text, src="english",dest=out_lang)
    translated = str(translated).split(", ")
    converted = translated[2]
    pro = translated[3]
    print(converted)
    print(pro)
    
#To understand this code watch the video tutorial on my youtube channel
#Here - 
