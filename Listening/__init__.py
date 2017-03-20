def start_listening(sr , r):
	#r = n.Recognizer()
	m = sr.Microphone()

	try:
	    print("A moment of silence, please...")
	    with m as source: r.adjust_for_ambient_noise(source)
	    print("Set minimum energy threshold to {}".format(r.energy_threshold))
	    
	    print("Say something!")
	    with m as source: audio = r.listen(source)
	    return audio
	#Need to discover what it passes to sphinx_audio (wav file/ mp3 / raw data)
	except KeyboardInterrupt:
	    pass


