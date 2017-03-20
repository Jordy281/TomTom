import speech_recognition as sr
from Listening import start_listening
from Language_Interpreter import start_interpreting
from Talking import speak

"""
This will be the main script run for TomTom

It will need to 
A) Listen for words
B) Interpret the words
C) Determine if it needs to respond

Nice to Haves:
D) Converse with multiple people
E) Move around

"""

#------------------------------------------------------------------------------------------------------------
# Initialize Recognizer
Recognizer = sr.Recognizer()

#------------------------------------------------------------------------------------------------------------
# Start Listening
# Collects the AudioData Object -> and returns it here
audio = start_listening(sr, Recognizer)

# Send the audio to Language Interpreter
value = start_interpreting(sr, Recognizer, audio)


# Print what was interpreted
if str is bytes:  # this version of Python uses bytes for strings (Python 2)
	print("python 2")
        print(u"You said {}".format(value).encode("utf-8"))
else:  # this version of Python uses unicode for strings (Python 3+)
	print("You said {}".format(value))
	
speak(value)

"""
#speech_engine = pyttsx.init('espeak') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
#speech_engine.setProperty('rate', 150)

import Listening

#recognizer = speech_recognition.Recognizer()

#def listen():
#	with speech_recognition.Microphone() as source:
#		recognizer.adjust_for_ambient_noise(source)
#		audio = recognizer.listen(source)
#
#	try:
#		return recognizer.recognize_sphinx(audio)
		# or: return recognizer.recognize_google(audio)
#	except speech_recognition.UnknownValueError:
#		print("Could not understand audio")
#	except speech_recognition.RequestError as e:
#		print("Recog Error; {0}".format(e))

#	return ""


#speak("I heard you say " + listen())
import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_sphinx(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
"""
