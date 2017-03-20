#LiveSpeech

#It’s an iterator class for continuous recognition or keyword search from a microphone.

from pocketsphinx import LiveSpeech
for phrase in LiveSpeech(): print(phrase)

#An example of a keyword search:

#from pocketsphinx import LiveSpeech

#speech = LiveSpeech(lm=False, keyphrase='forward', kws_threshold=1e+20)
#for phrase in speech:
#    print(phrase.segments(detailed=True))

#With your model and dictionary:

#import os
#from pocketsphinx import LiveSpeech, get_model_path

#model_path = get_model_path()

#speech = LiveSpeech(
#    verbose=False,
#    sampling_rate=16000,
#    buffer_size=2048,
#    no_search=False,
#    full_utt=False,
#    hmm=os.path.join(model_path, 'en-us'),
#    lm=os.path.join(model_path, 'en-us.lm.bin'),
#    dic=os.path.join(model_path, 'cmudict-en-us.dict')
#)

#for phrase in speech:
#    print(phrase)


