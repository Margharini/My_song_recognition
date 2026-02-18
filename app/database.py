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
    hashes = [hash_value for hash_value, _ in fingerprints]

    if not hashes:
        return None

    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT song_name, COUNT(*) as match_count
                FROM fingerprints
                WHERE hash = ANY(:hashes)
                GROUP BY song_name
                ORDER BY match_count DESC
                LIMIT 1
            """),
            {"hashes": hashes}
        )

        row = result.fetchone()
        if row:
            print("Match count:", row[1])
            return row[0]

    return None

