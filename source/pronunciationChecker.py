from difflib import ndiff
from playsound import playsound
import os

class PronunciationChecker:
    def __init__(self):
        #open the corpus file
        cwd = os.getcwd()
        spa = cwd + "\\langs\\spa\\"
        wel = cwd + "\\langs\\wel\\"
        
        spa_file = open(spa + "spanish-corpus.txt", "r", encoding='utf-8')
        self.spa_corpus = spa_file.read().splitlines()
        spa_file.close()
        self.spa_recordings = spa + "\\spanishrecordings\\"

        wel_file = open(wel + "welsh-corpus.txt", "r", encoding='utf-8')
        self.wel_corpus = wel_file.read().splitlines()
        wel_file.close()
        self.wel_recordings = wel + "\\welshrecordings\\"

        #Currently selected language
        self.lang = "wel"

        #the word to check against
        self.word = ""

    def getCorpus(self):
        if self.lang == "wel":
            return self.wel_corpus
        elif self.lang == "spa":
            return self.spa_corpus

    def setLang(self, lang):
        if lang == "wel":
            self.lang = "wel"
        elif lang == "spa":
            self.lang = "spa"

    def setWord(self, word):
        self.word = word

    def compare(self, wordToCompare):
        if wordToCompare == self.word:
            return "You said ... " + self.word + " ... which is CORRECT!\n\n"
        else:
            #Make a list of the differences
            differences_list = [li for li in ndiff(self.word, wordToCompare) if li[0] != ' ']
            return "You said ... " + wordToCompare + " ... which is incorrect...\n\nThe sounds you made which were werent quite right:\n\n       " + str(differences_list) + "\n\nSounds to not make are denoted with a '+',\nSounds you did not make are denoted with a '-'\n"
    
    def playWord(self):
        if self.lang == "wel":
            path = self.wel_recordings + self.word + ".wav"
        elif self.lang == "spa":
            path = self.spa_recordings + self.word + ".wav"

        if os.path.exists(path):
            playsound(path)
        else:
            print("Could not find the recording for the selected word... Sorry!")