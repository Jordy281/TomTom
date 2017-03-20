import pyttsx

speech_engine = pyttsx.init('espeak') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 150)

"""
Purpose: This uses linux's espeak to read text back to the user and will print the string as verification

input: 
	text - string to read

Output: 
	nothing


"""
def speak(text):
	speech_engine.say(text)
	speech_engine.runAndWait()
	print text


