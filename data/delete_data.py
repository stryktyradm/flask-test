import sqlite3

def delete_record(table_name):
    try:
        sqlite_connection = sqlite3.connect('db.sqlite3')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_delete_query = f"""DELETE FROM {table_name}"""
        cursor.execute(sql_delete_query)
        sqlite_connection.commit()
        print(f"Запись {table_name} успешно удалена")
        delete_table_query = f"""DROP TABLE IF EXISTS {table_name}"""
        cursor.execute(delete_table_query)
        sqlite_connection.commit()
        print(f"Таблица {table_name} успешно удалена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


if __name__ == '__main__':
    delete_record('movies_actors')
