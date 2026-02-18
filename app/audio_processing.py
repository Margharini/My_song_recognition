import librosa
import numpy as np
import matplotlib.pyplot as plt


def analyze_audio(file_path):
    # wczytanie pliku (mono)
    y, sr = librosa.load(file_path, mono=True)

    # FFT
    fft = np.fft.fft(y)
    magnitude = np.abs(fft)

    # tylko dodatnie częstotliwości
    frequencies = np.fft.fftfreq(len(magnitude), 1/sr)

    positive_freqs = frequencies[:len(frequencies)//2]
    positive_magnitude = magnitude[:len(magnitude)//2]

    # konwersja na decybele
    magnitude_db = 20 * np.log10(positive_magnitude + 1e-10)

    return positive_freqs, magnitude_db


if __name__ == "__main__":
    file_path = "C:/Users/User/Desktop/SHAZAM/samples/test.mp3"

    frequencies, magnitude_db = analyze_audio(file_path)

    plt.figure(figsize=(12, 6))
    plt.plot(frequencies, magnitude_db)
    plt.title("FFT Spectrum (Magnitude in dB)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.xlim(0, 5000)  # skupiamy się na 0–5kHz
    plt.grid()
    plt.show()
