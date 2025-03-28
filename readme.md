# WelshWords

A basic command line application, which can be used to train the pronunciation of a set of Welsh words. 

## FUNCTIONALITY:

- The system has two modes, uncontrolled and training. The uncontrolled mode can be used to test the back-end of the system, while the training mode is the intended use-case of the system - To train your pronunciation of a chosen word.
- The system interprets the incoming speech in terms of phonemes/ sounds, and then outputs those sounds as welsh script/text.
- In training, you select a word to practice first, and the detected sounds are checked against the correct pronunciation of the word. The system will let you know if you have pronounced the word correctly or not.

## INSTALLATION:
### Step 1: Installing pip 
[Ensure pip is installed.](https://pip.pypa.io/en/stable/installation/ ) 

### Step 2: Clone the repository/download the files
Clone the repo: `git clone https://github.com/fredRan24/WelshPronunciationTrainer.git`

### Step 3: Set up the virtual environment
To run the system, we need a python virtual environment. 
-	Open the command prompt
-	Navigate to the repo
-	Run: `python -m venv .venv`
-	Activate the environment using:
    o	Windows: `.venv\Scripts\activate.bat`
    o	Other OSes: `source .venv/bin/activate`

### Step 4: Install the dependencies
Run: `pip install -r requirements.txt`

### Step 5: Run the program 
Run: `python main.py`

#### Notes:
-	The first time running the system might take a while, as the model itself may need downloading. 
-	The system requires some form of microphone
-	The system requires an internet connection
