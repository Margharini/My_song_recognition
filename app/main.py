from microphone import record_audio
from fingerprint import generate_fingerprint
from database import match_fingerprints

if __name__ == "__main__":
    y, sr = record_audio(duration=5)

    fingerprints = generate_fingerprint(y, sr)

    song = match_fingerprints(fingerprints)

    if song:
        print("Detected song:", song)
    else:
        print("No match found")
