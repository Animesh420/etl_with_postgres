import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    '''
    Inserts records into Songs and Artists table from a song data file

    Args:
        cur: psycopg2 cursor object
        filepath: filepath to song data file
    Returns:
       None
    Raises:
        SQL Psycopg errors

    '''
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_columns = ["song_id", "title", "artist_id", "year", "duration"]
    song_data = df.loc[0, song_columns].values.tolist()
    song_data[-1] = float(song_data[-1])
    song_data[-2] = int(song_data[-2])
    cur.execute(song_table_insert, song_data)

    # insert artist record
    artist_columns = ["artist_id", "artist_name", "artist_location", "artist_latitude", "artist_longitude"]
    artist_data = df.loc[0, artist_columns].values.tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    '''
    Inserts records into Users, Time and Songplay table from a song data file

    Args:
        cur: psycopg2 cursor object
        filepath: filepath to log data file
    Returns:
       None
    Raises:
        SQL Psycopg errors

    '''
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page'] == 'NextSong']

    # convert timestamp column to datetime
    tc = df['ts'].map(lambda x: pd.Timestamp(x, unit='ms'))

    # insert time data records
    time_df = pd.DataFrame(
        data={
            'start_time': tc,
            'hour': tc.dt.hour,
            'day': tc.dt.day_name(),
            'week': tc.dt.weekofyear,
            'month': tc.dt.month_name(),
            'year': tc.dt.year,
            'weekday': tc.dt.dayofweek
        })

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    cols_in_df = ['userId', 'firstName', 'lastName', 'gender', 'level']
    user_columns = ['user_id', 'first_name', 'last_name', 'gender', 'level']
    mapped_df = df.rename(columns=dict(zip(cols_in_df, user_columns)))
    user_df = mapped_df[user_columns]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():

        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None
            continue

        # insert songplay record
        songplay_data = (pd.Timestamp(row['ts'], unit='ms'),
                         row['userId'],
                         row['level'],
                         songid, artistid,
                         row['sessionId'],
                         row['location'],
                         row['userAgent'])

        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))



def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()