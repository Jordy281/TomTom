"""
Purpose: To take a raw audio input and translate it into text

Input: 
	sr - speech recognition library
	r - recognizer object
	audio - raw audio

Output: 
	String of text containing the translated words

TO DO: 
	Use googles open source library and use a neural network as an engine (as opposed to sphinx/Google)
"""

def start_interpreting(sr, r , audio):
	try:
		#Need to discover what it passes to sphinx_audio (wav file/ mp3 / raw data)
		print("Got it! Now to recognize it...")
	        try:
	            # recognize speech using Google Speech Recognition
	            value = r.recognize_sphinx(audio)
		    return value
	        except sr.UnknownValueError:
	            print("Oops! Didn't catch that")
	        except sr.RequestError as e:
	            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
	
	except KeyboardInterrupt:
	    pass


