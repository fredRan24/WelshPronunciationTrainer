import cProfile
from pronunciationChecker import PronunciationChecker
from processaudio import WelshAudioProcessor
from recorder import MyRecorder

class CommandLineInteractions:
    def __init__(self):
        self.training = False
        self.exit = False
        self.checker = PronunciationChecker()
        self.recorder = MyRecorder()
        self.processor = WelshAudioProcessor()

    def modeSelector(self):
        while True:
            #get input for the options [1] = Uncontrolled, [2] = Training
            mode = input("There are two modes to select from:\n\n1. Uncontrolled   ...   Your speech will be recognised in terms of the sounds of the Welsh language.\n2. Training   ...   You can select a word to practice. If you make a mistake, the system will let you know!\n\nPlease enter [1] or [2] to select a mode...\n")
            #If user selects Training
            if mode == "2":
                #update variable to reflect mode
                self.training = True
                #Show the word select menu
                self.wordSelector()
                break
            #if user selects uncontrolled mode
            elif mode == "1":
                #update variable to reflect mode
                self.training = False
                break
            #If not broken, user input did not match an option
            print("That was not one of the options... Try again!\n")
            #loop

    def languageSelector(self):
        while True:
            language = input("Which language would you like to train? \n\n1. Welsh\n2. Spanish\n\nPlease enter [1] or [2] to select a language...\n")
            if language == "1":
                self.processor.setDictionary("wel")
                self.checker.setLang("wel")
                break
            elif language == "2":
                self.processor.setDictionary("spa")
                self.checker.setLang("spa")  
                break                      
            print("That was not one of the options... Try again!\n")


    def wordSelector(self):
        while True:
            print("---------Supported Words---------")

            #iterate through the corpus and output the words next to a number
            corpus = self.checker.getCorpus()
            for index in range(len(corpus)):
                print(str(index+1) + ". " + corpus[index])
            
            #Give selection instructions
            print("\nPlease choose a word from the list by entering the corresponding number...")

            #take user input on which word
            selectedWord = input("\nWhich word would you like to practice?\n")

            #if there is a word
            if len(selectedWord) > 0:
                #convert the input number to an int for comparisons
                selection_int = int(selectedWord)
                #if the input number is not higher than the number of words in the corpus
                if selection_int-1 <= len(corpus)-1:
                    #update the checker's word variable
                    self.checker.word = corpus[selection_int-1]
                    break
            else:
                #the number entered was either too big or too small, so express to user
                print("That was not one of the options... Try again!\n")
                #loop

    def repeatMenu(self):
        while True:
            command = ""
            #if training then show full menu
            if self.training:
                command = input("Press [l] to listen to the correct pronunciation\nPress [r] to try again..\nPress [m] to change mode\nPress [i] to change language\nPress [w] to change word\nPress [d] to reload the dictionary file\nPress [x] to exit\n")
            #else show menu without word selection
            else:
                command = input("Press [r] to try again..\nPress [m] to change mode\nPress [i] to change language\nPress [x] to exit\n")
            
            #if user inputs 'r' - Record Again
            if command == "r":
                break
            #If user inputs 'm' - Allow Mode Selection
            elif command == "m":
                self.modeSelector()
                break
            #If user inputs 'x' - Exit program
            elif command == "x":
                self.exit = True                
                break
            elif command == "d":
                self.processor.loadDictionary()
            elif command == "i":
                self.languageSelector()
                break

            #If training then check for 'w' input
            if self.training:
                #if user inputs 'w' - Allow Word Selection
                if command == "w":
                    self.wordSelector()
                    break
                elif command == "l":
                    self.playSelected()
            
            #if the command was l then we want it to loop again after playing the word
            if command != "l":
                #If not l and not broken by here the input did not match an option
                print("That was not one of the options... Try again!")
                #loop to try again
            
    def printCurrentWord(self):
        print("Training the word " + self.checker.word)

    def check(self, text):
        return self.checker.compare(text)

    def recordAndProcess(self):
        #record some audio and get it as a numpy.array
        numpyData = self.recorder.record()
        #process and get transcript
        transcript = self.processor.processAudio(audio=numpyData, showTranslation=False)
        return transcript

    def playSelected(self):
        self.checker.playWord()

def test():
    #go into training mode
    interact = CommandLineInteractions()
    interact.training = True
    #pick a word
    interact.checker.word = "cefnogaeth"
    #record and process
    out = interact.recordAndProcess()
    #output
    print(out)

if __name__ == "__main__":
    cProfile.run(test())