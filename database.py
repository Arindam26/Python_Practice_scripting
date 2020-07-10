import datetime
import sqlite3

"""title, release_date, watched"""

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS zin (
title TEXT,
release_timestamp REAL,
watched INTEGER);"""
CREATE_USERS_TABLE = """create table if not exists users(
username TEXT primary key
);"""
CREATE_WATCHED_TABLE = """create table if not exists watched(
user_username TEXT,
movie_id INTEGER,
foreign Key(user_username) references users(username),
foreign key(movie_id) references zin(id)
);"""
SET_MOVIE_WATCHED = """update zin set watched = 1 where title = ?;"""
INSERT_MOVIES = """insert into zin(title, release_timestamp) values(?,?);"""
SELECT_ALL_MOVIES = """select * from zin;"""
SELECT_UPCOMING_MOVIES = """select * from zin where release_timestamp > ?;"""
INSERT_WATCHED_MOVIES = """ insert into watched(user_username, movie_id) values(?,?);"""
SELECT_WATCHED_MOVIES = """select * from watched  where watcher_name = ?;"""
DELETE_MOVIE = """delete from  zin where title = ?;"""
INSER_USER = "insert into users values(?);"

connection = sqlite3.connect("moviespractice.db")


def create_table():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)


def add_user(username):
    with connection:
        connection.execute(INSER_USER, (username,))


def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES, (title, release_timestamp))


def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()


def watch_movie(username, movie_id):
    with connection:
        connection.execute(INSERT_WATCHED_MOVIES, (username, movie_id))


def get_watched_movies(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (username,))
        return cursor.fetchall()
