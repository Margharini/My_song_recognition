from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg2://postgres:mp@localhost:5432/shazam")

def save_fingerprints(song_name, fingerprints):
    with engine.connect() as conn:
        for hash_value, time_offset in fingerprints:
            conn.execute(
                text("INSERT INTO fingerprints (song_name, hash, time_offset) VALUES (:song, :hash, :offset)"),
                {"song": song_name, "hash": hash_value, "offset": time_offset}
            )
        conn.commit()

def match_fingerprints(fingerprints):
    with engine.connect() as conn:
        matches = {}

        for hash_value, _ in fingerprints:
            result = conn.execute(
                text("SELECT song_name FROM fingerprints WHERE hash = :hash"),
                {"hash": hash_value}
            )

            for row in result:
                matches[row[0]] = matches.get(row[0], 0) + 1

        if matches:
            return max(matches, key=matches.get)

    return None
