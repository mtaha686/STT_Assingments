import sqlite3

conn = sqlite3.connect('video_rental.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS videos
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT,
              director TEXT,
              year INTEGER,
              rented INTEGER)''')


def search_video(title, director, year):
    c.execute("SELECT * FROM videos WHERE title=? AND director=? AND year=?",
              (title, director, year))
    video_records = c.fetchall()
    return video_records


with open("expOut_movies.txt", "r") as expected_output_file:
    expected_output_lines = expected_output_file.readlines()

with open("test_search_log.txt", "w") as log_file:
    for expected_output_line in expected_output_lines:
        expected_output_line = expected_output_line.strip()
        details = expected_output_line.split(",")
        title = details[0]
        director = details[1]
        year = int(details[2])

        search_results = search_video(title, director, year)
        expected_records = expected_output_line.split(";")

        verdict = "True" if all(
            record in expected_records for record in search_results) else "False"

        log_file.write(f"Movie: {title}, {director}, {year}\n")
        log_file.write(f"Expected Output: {expected_output_line}\n")
        log_file.write(f"Verdict: {verdict}\n\n")

conn.close()
