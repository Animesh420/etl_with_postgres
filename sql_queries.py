# TEMPLATES
prompt_create = '''CREATE TABLE IF NOT EXISTS {} '''
prompt_delete = '''DROP TABLE IF EXISTS {} ;'''
prompt_insert = '''INSERT INTO {} '''

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
songplay_id serial primary key,
start_time timestamp not null,
user_id int not null,
level text,
song_id text not null,
artist_id text not null,
session_id text,
location text not null,
user_agent text
)
""")
̐
user_table_create = (prompt_create.format(USERS) + """(
user_id int not null unique primary key,
first_name text not null,
last_name text,
gender text,
level text
)
""")

song_table_create = (prompt_create.format(SONGS) + """(
song_id text not null unique primary key,
title text not null,
artist_id text not null,
year int,
duration numeric not null
)
""")

artist_table_create = (prompt_create.format(ARTISTS) + """(
artist_id text not null unique primary key,
artist_name text not null,
artist_location text not null,
artist_latitude numeric not null,
artist_longitude numeric not null
)
""")

time_table_create = (prompt_create.format(TIME) + """(
start_time timestamp primary key,
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
VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id)
    DO UPDATE
    SET
    first_name = EXCLUDED.first_name,
    last_name = EXCLUDED.last_name,
    gender = EXCLUDED.gender,
    level = EXCLUDED.level
""")

song_table_insert = (prompt_insert.format(SONGS) + """
(song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id)
    DO UPDATE
    SET
    title = EXCLUDED.title,
    artist_id = EXCLUDED.artist_id,
    year = EXCLUDED.year,
    duration = EXCLUDED.duration
""")

artist_table_insert = (prompt_insert.format(ARTISTS) + """
(artist_id , artist_name , artist_location , artist_latitude , artist_longitude )
VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id)
    DO UPDATE
    SET
    artist_name = EXCLUDED.artist_name,
    artist_location = EXCLUDED.artist_location,
    artist_latitude = EXCLUDED.artist_latitude,
    artist_longitude = EXCLUDED.artist_longitude
""")

time_table_insert = (prompt_insert.format(TIME) + """
(start_time ,hour ,day ,week ,month ,year ,weekday )
VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING
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

create_table_queries = [
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create]
drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop]
