from psycopg2.extras import execute_values

CREATE_TABLE = "CREATE TABLE IF NOT EXISTS entries (activity TEXT, thoughts TEXT, date TEXT, day INT, github TEXT, demo TEXT);"

ADD_ENTRY = "INSERT INTO entries VALUES (%s, %s, %s, %s, %s, %s);"

SELECT_ENTRIES = "SELECT * FROM entries;"

SELECT_DAY = "SELECT * FROM entries WHERE day = %s;"

SELECT_ALL_DATE = "SELECT * FROM entries WHERE date = %s;"


def create_table(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_TABLE)


def add_entry(connection,
              entry_activity,
              entry_thoughts,
              entry_date,
              entry_day,
              entry_github=None,
              entry_demo=None):
    """Adds entry content and date, as an object, to the entries array"""
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(ADD_ENTRY,
                           (entry_activity, entry_thoughts, entry_date, entry_day, entry_github, entry_demo))


def get_entries(connection, day=None, date=None):
    """Returns entries as an array of objects"""
    with connection:
        with connection.cursor() as cursor:
            if day is not None:
                cursor.execute(SELECT_DAY, (day, ))

            elif date is not None:
                cursor.execute(SELECT_ALL_DATE, (date, ))

            else:
                cursor.execute(SELECT_ENTRIES)
            return cursor.fetchall()
