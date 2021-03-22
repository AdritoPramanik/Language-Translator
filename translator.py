#Please like and subscribe
#If you have any queries or doubts related to this video, please type your doubt in the comment box.
#I promise to respond to all your comment
#And please do share it with your family and friends
#Name of the channel-Adi's Technical Aid
#Channel link-https://www.youtube.com/channel/UCONkwKyrkLVRWTW4ZZichBw
import googletrans
import speech_recognition as sr
import gtts
import playsound
import os

recognizer = sr.Recognizer()
translator = googletrans.Translator()
inputLanguage = 'en'
outputLanguage = 'es'

try:
    with sr.Microphone() as source:
        print('speak')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=inputLanguage)
        print(text)

except:
    print('couldnt understand, speak again')

translated = translator.translate(text, dest=outputLanguage)
print(translated.text)
convertedAudio = gtts.gTTS(translated.text, lang=outputLanguage)
convertedAudio.save('audio.mp3')
playsound.playsound('audio.mp3')
os.remove('audio.mp3')
# print(googletrans.LANGUAGES)
