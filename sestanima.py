import googletrans
import speech_recognition as sr 
import time
import webbrowser
from datetime import datetime
from gtts import gTTS
from playsound import playsound
import random
import os






r = sr.Recognizer()

def record():  #sesini kaydetmesi için gerekli fonksiyon
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            speak('anlayamadım')
        except sr.RequestError:
            speak('sistem çalışmıyor')
        return voice




def response(voice):  #yanıtlayabilmesi için gerekli fonksiyon
    if('nasılsın' in voice):
        speak("iyiyim,teşekkürler.")

    elif('Ahu' in voice):
        speak("buyrun.")

    elif('Merhaba' in voice):
        speak("merhaba erol bey.")

    
    elif('adın ne' in voice):
        speak("adım Ahu.")
    
    elif('Seni kim yarattı' in voice):
        speak("yaratıcım erol bey.")

    elif('arama yap' in voice):               #buraya youtube uzantılı opsiyon gelecek.
        speak('ne aramak istiyorsunuz?.')
        search = record()
        if(search == "netflix"):
            url1 = ('https://www.netflix.com')
            webbrowser.get().open(url1)
        
        else:
            url = ('https://www.google.com.tr/search?q='+ search)
            webbrowser.get().open(url)
            speak(search+ ' için bulduklarım')
        
        
        
        
        
        


    

    elif('Photoshop aç' in voice):
        speak('photoshop uygulaması açılıyor.')
        os.startfile('C:\Program Files\Adobe\Adobe Photoshop 2020\Photoshop.exe')

    elif('fotoşop aç' in voice):
        speak('photoshop uygulaması açılıyor.')
        os.startfile('C:\Program Files\Adobe\Adobe Photoshop 2020\Photoshop.exe')

    elif('saat kaç' in voice):
        speak(datetime.now().strftime('%H:%M:%S'))

    




#kapatmak için gerekli komutlar

    elif('kapat' in voice):
        speak("Tamam görüşürüz")
        exit()
    elif('tamamdır' in voice):
        speak("Tamam görüşürüz")
        exit()
    elif('çıkış yap' in voice):
        speak("Tamam görüşürüz")
        exit()
    elif('görüşürüz' in voice):
        speak("Tamam görüşürüz")
        exit()
    elif('teşekkürler' in voice):
        speak("rica ederim.")
    
    


def speak(string):   #konuşması için gerekli fonksiyon
   tts = gTTS(string,lang='tr')
   rand = random.randint(1,10000)
   file = 'audio-'+str(rand)+'.mp3'
   tts.save(file)
   playsound(file)
   os.remove(file)


speak("Erol Bey merhaba,Nasıl yardımcı olabilirim?")

while 1:
    voice = record()
    print(voice)
    response(voice)
   