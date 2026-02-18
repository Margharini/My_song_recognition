import librosa
from fingerprint import generate_fingerprint
from database import save_fingerprints

if __name__ == "__main__":
    file_path = "C:/Users/User/Desktop/SHAZAM/samples/test.mp3"
    song_name = "Test Song"

    print("Loading audio...")
    y, sr = librosa.load(file_path, mono=True)

    print("Generating fingerprints...")
    fingerprints = generate_fingerprint(y, sr)

    print(f"Generated {len(fingerprints)} fingerprints")

    print("Saving to database...")
    save_fingerprints(song_name, fingerprints)

    print("Done indexing!")
