from lesson_07.lesson_07_task_01.context_db_manager import DBContextManager

if __name__ == '__main__':
    db = "DB_for_CM.db"
    with DBContextManager(db) as conn:
        cursor = conn.cursor()

        sql_req = "INSERT INTO test_table(INFORMATION) VALUES ('set_data1');"
        cursor.execute(sql_req)
        sql_req = "INSERT INTO test_table(INFORMATION) VALUES ('set_data2');"
        cursor.execute(sql_req)
        sql_req = "INSERT INTO test_table(INFORMATION) VALUES ('set_data3');"
        cursor.execute(sql_req)
        sql_req = "INSERT INTO test_table(INFORMATION) VALUES ('set_data4');"
        cursor.execute(sql_req)
        conn.commit()
        print(cursor.fetchall())

        sql_req = "SELECT * FROM test_table;"
        cursor.execute(sql_req)
        print(cursor.fetchall())
