import pyaudio
import numpy as np
from playsound import playsound
import os

class MyRecorder:
    def __init__(self):
        print("Loading Recorder...")
        #Constants:
        self.CHUNKSIZE = 1024
        self.sr = 16000
        self.seconds = 2
        self.frames = []
        recSoundsPath = os.getcwd() + "\\assets\\"
        self.startSoundPath = recSoundsPath + "start.wav"
        self.stopSoundPath = recSoundsPath + "stop.wav"
        print("Recorder Loaded...")

    def record(self):
        #create a pyaudio audio object, and open a stream of type float
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paFloat32, channels=1, rate=self.sr, input=True, frames_per_buffer=self.CHUNKSIZE)
        
        #give audible feedback that recording will begin
        playsound(self.startSoundPath)
        #give visual feedback that recording will begin
        print("\n                    Recording...")

        #stream audio as chunks. (16kHz/1024=chunksPerSecond) * NumberOfSecondsToRecordFor
        for _ in range(0, int(self.sr / self.CHUNKSIZE * self.seconds)):
            data = stream.read(self.CHUNKSIZE)
            self.frames.append(np.frombuffer(data, dtype=np.float32))

        #make a numpy.array containing the audio data
        numpyData = np.hstack(self.frames)

        #stop recording, close stream, terminate pyaudio object for now and clear the local frames
        stream.stop_stream()
        stream.close()

        #give audible feedback that recording has ended
        playsound(self.stopSoundPath)
        #give visual feedback that recording has ended
        print("                    Stopping...")

        #terminate object and clear frame data
        audio.terminate()
        self.frames.clear()
        
        #returns the audio as a numpy array, which is what the processor accepts further down the pipeline.
        return numpyData