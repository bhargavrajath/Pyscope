import sounddevice as sd
import numpy as np
from matplotlib import pyplot as plt

length = 1 # seconds
fs = 44100
samples = length * fs

sd.default.samplerate = fs
sd.default.channels = 1

data = sd.rec(samples) # numpy array output

sd.wait()

data = data/np.max(data)

f = np.linspace(0,fs*length,int(fs/length))

spectrum = np.fft.fft(data)

plt.semilogx(f,spectrum)
plt.grid(True)
plt.xlabel('Frequency (Hz)')
plt.show()
