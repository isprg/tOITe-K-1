import pyaudio
import wave
import os
from concurrent.futures import ThreadPoolExecutor
from alsa_error_handler import noalsaerr


class ClsAudioSensor:
    def __init__(self, sChannels, sRate, sUnitSample):
        self.vAudio = []
        self.blRecording = False
        self.format = pyaudio.paInt16
        self.sChannels = sChannels
        self.sRate = sRate
        self.sUnitSample = sUnitSample

        if os.name == 'nt':
            self.audio = pyaudio.PyAudio()
        else:
            with noalsaerr():
                self.audio = pyaudio.PyAudio()

        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=sChannels,
            rate=sRate,
            input=True,
            frames_per_buffer=sUnitSample)

    def __del__(self):
        self.finalize()

    def finalize(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

    def startRecordThread(self):
        self.vAudio = []
        self.blRecording = True
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.executor.submit(self.sample)

    def shutdownRecordThread(self):
        self.executor.shutdown()

    def setRecording(self, blRecording):
        self.blRecording = blRecording

    def getRecording(self):
        return self.blRecording

    def sample(self):
        while self.blRecording:
            vData = self.stream.read(self.sUnitSample)
            self.vAudio.append(vData)
        self.shutdownRecordThread()

    def record(self, strFileName):
        wf = wave.open(strFileName, 'wb')
        wf.setnchannels(self.sChannels)
        wf.setsampwidth(self.audio.get_sample_size(self.format))
        wf.setframerate(self.sRate)
        wf.writeframes(b''.join(self.vAudio))
        wf.close()
