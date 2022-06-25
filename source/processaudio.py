import ast
from torch import argmax
from transformers import AutoProcessor, AutoModelForCTC
import os

"""  uncomment to use processWavDir()
import librosa 
from pathlib import Path
"""

class WelshAudioProcessor:
    def __init__(self):
        print("Loading Model...")
        self.tokenizer = AutoProcessor.from_pretrained("facebook/wav2vec2-xlsr-53-espeak-cv-ft")
        self.model = AutoModelForCTC.from_pretrained("facebook/wav2vec2-xlsr-53-espeak-cv-ft")
        print("Model Loaded...")
        #get the dictionaries from the files
        self.wel_dict = {}
        self.spa_dict = {}
        self.loadDictionary()

        #set the dictionary to use to the welsh initially
        self.dictionary = self.wel_dict
        
    
    """ IF YOU WANT TO USE THIS FUNCTION IN TESTING, LIBROSA NEEDS TO BE ADDED TO REQUIREMENTS.TXT/imported
    def processWavDir(self, dir_path, romanize=True, showTranslation=False):
        pathlist = Path(dir_path).glob('**/*.wav')
        transcript = ""
        for path in pathlist:
            speech, rate = librosa.load(str(path))
            this_transcript = self.processAudio(audio=speech, romanize=romanize, showTranslation=showTranslation)
            transcript = transcript + this_transcript + "\n"
        return transcript
    """
    
    def processAudio(self, audio, romanize=True, showTranslation=False):
        input_values = self.tokenizer(audio, return_tensors = 'pt', sampling_rate = 16000).input_values
        logits = self.model(input_values).logits
        predicted_ids = argmax(logits, dim =-1)
        #print(len(predicted_ids))
        transcription = self.tokenizer.decode(predicted_ids[0])
        #print("transcription after tokenization is a: " + str(type(transcription)))
        if romanize == True:
            romanized = self.convertIPAToRoman(wordInput=transcription, showTranslation=showTranslation)
            return romanized
        else:
            return transcription

    def convertIPAToRoman(self, wordInput, showTranslation):
        word = wordInput
        word = word.replace(" ", "")
        #stick a space on the end
        #word = word + " "
        for ipa_script, roman_script in self.dictionary.items():
            ipa_str = str(ipa_script)
            word = word.replace(ipa_str, roman_script)
        
        if showTranslation == True:
            merge = wordInput + "  ====>  " + word
            return merge
        else: 
            return word

    def loadDictionary(self):
        cwd = os.getcwd()
        spa = cwd + "\\langs\\spa\\spanish-dictionary.txt"
        wel = cwd + "\\langs\\wel\\welsh-dictionary.txt"

        spa_file = open(spa, "r", encoding='utf-8')
        spa_cont = spa_file.read()
        spa_cont_dict = ast.literal_eval(spa_cont)
        spa_file.close()
        self.spa_dict = spa_cont_dict

        wel_file = open(wel, "r", encoding='utf-8')
        wel_cont = wel_file.read()
        wel_cont_dict = ast.literal_eval(wel_cont)
        wel_file.close()
        self.wel_dict = wel_cont_dict

    def setDictionary(self, lang):
        if lang == "wel":
            self.dictionary = self.wel_dict
        elif lang == "spa":
            self.dictionary = self.spa_dict

