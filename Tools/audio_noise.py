
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

if __name__ == "__main__":
    audio_noise_thread_executor()