import sqlite3
conn = sqlite3.connect('click_time_stamp.db')
c = conn.cursor()
def time_stamp_func(instance_stamp):
    c.execute('''CREATE TABLE IF NOT EXISTS time_stamp (Time TEXT)''')
    c.execute('INSERT INTO INTO time_stamp(?);', (instance_stamp))
    c.execute('SELECT Time FROM time_stamp WHERE time = ?', instance_stamp)
print c.fetchone()
    print(t_stamp)
conn.commit()
conn.close()    
