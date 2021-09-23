from googletrans import Translator
import pywhatkit 
text='HAHAHAHAHA'
translator = Translator(service_urls=['translate.googleapis.com'])
out=translator.translate(text, dest='ml')
print(out)