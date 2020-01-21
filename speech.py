import speech_recognition as gd

a = gd.Recognizer()

with gd.Microphone() as source:
    print('Speak Anything : ')
    audio = a.listen(source)

    try:
        text = a.recognize_google(audio)
        print('You said : {}'.format(text))

    except:
        print('Sorry could not recognize your voice !')
        
