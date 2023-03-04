
import threading, os, random

def audio_noise_thread_executor():
    def generator(kwargs):
        print(kwargs)
        while kwargs.get('do', False):
            duration = random.randint(5, 10) / 100
            freq = random.randint(20, 20000)  # Hz
            os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
    data = {'do' : True}
    thread = threading.Thread(target=generator, args=[data])
    thread.start()
    thread.data = data
    return thread

def play_noise_1():
    import numpy as np
    import sounddevice as sd
    import time, pyaudio

    P = pyaudio.PyAudio()
    sps, wm = 44100, .1
    duration_s = 1.5
    while True:
        data =  np.random.uniform(-wm,wm,sps)
        scaled = np.int16(data/np.max(np.abs(data)) * 767)
        stream = P.open(rate=sps, format=pyaudio.paInt16, channels=1, output=True)
        stream.write(scaled.tobytes())
        stream.close()
    P.terminate()

    return sd

if __name__ == "__main__":
    play_noise_1()
