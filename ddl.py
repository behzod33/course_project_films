import pandas as pd
import duckdb

genres = pd.read_csv('source/genres.csv')
movies = pd.read_csv('source/movies.csv')
screenings = pd.read_csv('source/screenings.csv')
theaters = pd.read_csv('source/theaters.csv')

with duckdb.connect("my.db") as duck:
    try:
        duck.register("temp_genres", genres)
        duck.register("temp_movies", movies)
        duck.register("temp_screenings", screenings)
        duck.register("temp_theaters", theaters)
        
        duck.query("CREATE TABLE genres AS SELECT * FROM temp_genres")
        duck.query("CREATE TABLE movies AS SELECT * FROM temp_movies")
        duck.query("CREATE TABLE screenings AS SELECT * FROM temp_screenings")
        duck.query("CREATE TABLE theaters AS SELECT * FROM temp_theaters")
        print('Таблицы успешно созданы и данные загружены!')
    except Exception as e:
        print(f'Ошибка: {e}')

