import numpy as np
import librosa
from scipy.signal import find_peaks

def generate_fingerprint(y, sr):
    # STFT
    stft = np.abs(librosa.stft(y, n_fft=2048))

    fingerprints = []

    for time_idx in range(stft.shape[1]):
        spectrum = stft[:, time_idx]
        peaks, _ = find_peaks(spectrum, height=np.max(spectrum)*0.5)

        for peak in peaks:
            hash_value = f"{peak}"
            fingerprints.append((hash_value, time_idx))

    return fingerprints
