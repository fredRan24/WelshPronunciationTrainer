from interactions import CommandLineInteractions
def main():
    #local variable to show the correct menu the first time around.
    firstLoop = True

    #Load the processor and checker components
    interact = CommandLineInteractions()
    #Setup Complete... Signify Ready
    print("Ready!\n")
    
    while interact.exit == False:
        #if it's the first loop, ask user to select a mode
        if firstLoop:
            interact.languageSelector()
            interact.modeSelector()
            firstLoop = False

        #If Training mode has been selected, show the selected word
        if interact.training:
            interact.printCurrentWord()
        
        #record and process some speech
        transcript = interact.recordAndProcess()
        
        #If we are training do the check step
        if interact.training:
            transcript = interact.check(transcript)
        
        #output trnscript / checker output
        print("\n                    " + str(transcript))
        
        #show repeat menu
        interact.repeatMenu()

if __name__ == "__main__":
    main()

