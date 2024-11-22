import duckdb

def load_data(table_name):
    try:
        with duckdb.connect('my.db') as duck:
            query = f"SELECT * FROM {table_name}"
            return duck.query(query).to_df()
    except Exception as e:
        print(f"Ошибка при загрузке данных из таблицы '{table_name}': {e}")
        return None
