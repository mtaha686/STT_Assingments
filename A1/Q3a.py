import sqlite3

conn = sqlite3.connect('video_rental.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS videos
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT,
              director TEXT,
              year INTEGER,
              rented INTEGER)''')


def insert_video(title, director, year):
    rented = 0
    c.execute("INSERT INTO videos (title, director, year, rented) VALUES (?, ?, ?, ?)",
              (title, director, year, rented))
    conn.commit()
    print("Video record inserted successfully.")


with open("input_movies.txt", "r") as input_file, open("expOut_movies.txt", "r") as expected_output_file:
    input_lines = input_file.readlines()
    expected_output_lines = expected_output_file.readlines()

with open("test_movies.txt", "w") as test_file:
    for input_line, expected_output_line in zip(input_lines, expected_output_lines):
        input_line = input_line.strip()
        expected_output_line = expected_output_line.strip()
        # print(expected_output_file)
        details = input_line.split(",")
        title = details[0]
        director = details[1]
        year = int(details[2])
        if input_line == expected_output_line:
            verdict = "Ture"
        else:
            verdict = "False"

        test_file.write(f"input Record: {title}, {director}, {year}\n")
        test_file.write(f"Expected Record: {expected_output_line}\n")
        test_file.write(f"Verdict: {verdict}\n\n")

conn.close()
