WelshWords

A basic command line application, which can be used to train the pronunciation of a set of Welsh words. 

FUNCTIONALITY:

- The system has two modes, uncontrolled and training. The uncontrolled mode can be used to test the back-end of the system, while the training mode is the intended use-case of the system - To train your pronunciation of a chosen word.

- The system interprets the incoming speech in terms of phonemes/ sounds, and then outputs those sounds as welsh script/text.

- In training, you select a word to practice first, and the detected sounds are checked against the correct pronunciation of the word. The system will let you know if you have pronounced the word correctly or not.


INSTALLATION:
Note: This has been tested on Windows 10 machines – Running the system on MacOS or Linux may result in unknown bugs!

Step 1: Installing pip 
You may already have pip installed on your system if you have done any python development in the past, but if you have not got it installed, follow the process here: https://pip.pypa.io/en/stable/installation/ 

Step 2: Clone the repository/download the files
Next, we need to get the files for the developed system. To do this, you can either:
-	Clone the repository from https://gitlab.uwe.ac.uk/aji2-ransome/tamil-speech-to-text-gsdp/-/tree/WelshBranch by following these steps.
-	OR you can simply download the files from the above link instead, by clicking the download button, to the left of the ‘Clone’ button.

Step 3: Set up the virtual environment
To run the system, we need a python virtual environment. 
-	Open the command prompt
    o	cmd.exe on Windows
    o	terminal on MacOS 
-	Navigate to where you have cloned/saved the files in the previous step, inside the command prompt
-	Enter the command: python -m venv .venv
-	Activate the environment using:
    o	Windows: .venv\Scripts\activate.bat
    o	Other OSes: source .venv/bin/activate
-	Now it should show ‘(.venv)’ at the beginning where you enter commands In the command line.

Step 4: Install the dependencies
Next, we need to install the packages the system uses, into this virtual env.
To do this, enter the command:
pip install -r requirements.txt

Step 5: Run the program 
Everything should now be installed, so you can run the program entering to command:
python main.py
-	The first time running the system might take a while, as the model itself may need downloading. 
-	The system requires some form of microphone
-	The system requires an internet connection
