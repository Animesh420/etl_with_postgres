# TEMPLATES
prompt_create = '''CREATE TABLE IF NOT EXISTS {} '''
prompt_delete = '''DROP TABLE IF EXISTS {} ;'''
prompt_insert =  '''INSERT INTO {} '''

# TABLE_NAMES
SONGPLAY = "songplays"
USERS = "users"
SONGS = "songs"
ARTISTS = "artists"
TIME = "time"

# DROP TABLES

songplay_table_drop = prompt_delete.format(SONGPLAY)
user_table_drop = prompt_delete.format(USERS)
song_table_drop = prompt_delete.format(SONGS)
artist_table_drop = prompt_delete.format(ARTISTS)
time_table_drop = prompt_delete.format(TIME)


# CREATE TABLES

songplay_table_create = (prompt_create.format(SONGPLAY) + """ (
songplay_id serial, 
start_time timestamp, 
user_id int, 
level text, 
song_id text, 
artist_id text, 
session_id text, 
location text, 
user_agent text
)
""")

user_table_create = (prompt_create.format(USERS) + """(
user_id int not null unique, 
first_name text, 
last_name text, 
gender text, 
level text
)
""")

song_table_create = (prompt_create.format(SONGS) + """(
song_id text not null unique, 
title text, 
artist_id text, 
year int, 
duration numeric
)
""")

artist_table_create = (prompt_create.format(ARTISTS) + """(
artist_id text not null unique, 
artist_name text, 
artist_location text, 
artist_latitude numeric, 
artist_longitude numeric
)
""")

time_table_create = (prompt_create.format(TIME) + """(
start_time timestamp, 
hour int, 
day text, 
week int, 
month text, 
year int, 
weekday int
)
""")

# INSERT RECORDS

songplay_table_insert = (prompt_insert.format(SONGPLAY) + """  
(start_time, user_id ,level ,song_id ,artist_id ,session_id ,location ,user_agent )
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = (prompt_insert.format(USERS) + """
(user_id, first_name, last_name ,gender ,level )
VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO NOTHING 
""")

song_table_insert = (prompt_insert.format(SONGS) + """
(song_id, title, artist_id, year, duration) 
VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = (prompt_insert.format(ARTISTS) + """
(artist_id , artist_name , artist_location , artist_latitude , artist_longitude )
VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING 
""")

time_table_insert = (prompt_insert.format(TIME) + """
(start_time ,hour ,day ,week ,month ,year ,weekday )
VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
SELECT 
    songs.song_id,
    artists.artist_id 
FROM songs
JOIN artists 
ON songs.artist_id = artists.artist_id
WHERE songs.title = %s and
artists.artist_name = %s and
songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]