import speech_recognition as sr

def speech_to_text():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("Timeout error")
            return

        try:
            print("Recognizing....")
            
            text = recognizer.recognize_google(audio)
            print("You said:", text)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Error with the request to Google Web Speech API; {0}".format(e))

if __name__ == "__main__":
    speech_to_text()