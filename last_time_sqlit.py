import sqlite3
conn = sqlite3.connect('click_time_stamp.db')
c = conn.cursor()

def last_time(t_stamp):
    c.execute('''CREATE TABLE IF NOT EXISTS time_stamp (Time TEXT)''')
    c.execute("INSERT INTO time_stamp (Time) VALUES(?)",
             (t_stamp,))
    conn.commit()
    conn.close()  

